from models.migration.servant import *
from models.migration.ce import *
from models.migration.statics import *
from pymongo import MongoClient
import json

# inserting to MongoDB
# MongoDB connection
client = MongoClient('mongodb://localhost:27017')  # Adjust the URI as needed
db = client['fgo']
collection = db['servants']


'''
从 atlas-academy 中下载基础礼装相关数据
'''
import requests
import json
import time
from tqdm import tqdm
from pprint import pprint

basic_servants = 'https://api.atlasacademy.io/export/JP/basic_servant_lang_en.json'
basic_ces = 'https://api.atlasacademy.io/export/JP/basic_equip_lang_en.json'
nice_servants = 'https://api.atlasacademy.io/nice/JP/svt/{svt_id}?lang=en'
nice_ces = 'https://api.atlasacademy.io/nice/JP/equip/{ce_id}?lang=en'
nice_skills = 'https://api.atlasacademy.io/nice/JP/skill/{skill_id}?lang=en'


basic_servants = requests.get(basic_servants).json()
basic_ces = requests.get(basic_ces).json()

with open('data/svt_names.json.json','r',encoding='utf-8') as f:
    translate = json.load(f)
with open('data/ce_names.json.json','r',encoding='utf-8') as f:
    ce_translate = json.load(f)



def process_function_data(function,default_level = 0):
    buffs = []
    chained_skill = set()
    for buff in function['buffs']:
        buffs.append(Buff(
            id=buff['id'],
            name=buff['name'],
            type=buff['type'],
            max_rate=buff['maxRate'],
            vals = buff['vals'],
            tvals = buff['tvals'],
            check_self=buff['ckSelfIndv'],
            check_op=buff['ckOpIndv'],
        ))
    skillvalues = []
    if default_level:
        levels = [function['svals'][default_level-1]]
    else:
        levels = function['svals']
    for skv in levels:
        if skv.get('Value2',-1)>=1 and skv.get('Value',None):
            chained_skill.add((skv.get('Value'),skv.get('Value2')))
        skillvalues.append(SkillValue(
            Rate=skv.get('Rate',-1),
            Value=skv.get('Value',-1),
            Value2=skv.get('Value2',-1),
            Turn=skv.get('Turn',-1),
            Count=skv.get('Count',-1) ,
            Userate=skv.get('Userate',-1)
        ))
    
    return Function(
                    id=function['funcId'],
                    function_type=function['funcType'],
                    target_type=function['funcTargetType'],
                    target_team=function['funcTargetTeam'],
                    quest_values = function['funcquestTvals'],
                    trait_values=function['functvals'],
                    buffs = buffs,
                    skillvalues=skillvalues        
    ),chained_skill
        
def extract_skills(skills,default_level = 0):
        # 技能组
        active_skills = []
        for sk in skills:
            auxiliary_skills = set()
            functions = []
            for func in sk['functions']:
                if func['funcTargetTeam'] == 'enemy':
                    continue # 不记录敌方数据
                function_data,chained_skill = process_function_data(func,default_level=default_level)
                functions.append(function_data)
                if chained_skill:
                    auxiliary_skills.update(chained_skill)

            active_skills.append(Skill(
                id=sk['id'],
                servant_id=sk['svtId'],
                skill_no=sk['num'],
                name=sk['name'],
                skill_type=sk['type'],
                strengthStatus=sk['strengthStatus'],
                priority=sk['priority'],
                cooldown=sk['coolDown'][-1],
                functions=functions
            ))
            new_skills = []
            for aux,level in auxiliary_skills:
                nice_skill_data = requests.get(nice_skills.format(skill_id=aux)).json()
                if nice_skill_data.get('detail','')=='Skill not found':
                    continue
                nice_skill_data.update({'svtId':sk['svtId'],"num":-1,'type':'chained','name':sk['name']})
                try:
                    new_skills = extract_skills([nice_skill_data],default_level=level)
                except Exception as e:
                    print(f'Error fetching skill {sk['id']} {aux}: {e}')
                    raise Exception(f'Error fetching skill {aux}: {e}')
                
            active_skills.extend(new_skills)
        
        return active_skills
        
def extract_td(td):
        tds = []
        for t in td:
            auxiliary_skills = []
            functions = []
            for func in t['functions']:
                function_data, chained_skill = process_function_data(func)
                functions.append(function_data)
                if chained_skill:
                    auxiliary_skills.append(chained_skill)
                                
            tds.append(NoblePhantasm(
                id = t['id'],
                name = t['name'],
                card = Card(card_type=t['card'], np_rate=t['npGain']['np'][0], hits_distribution=t['npDistribution']),
                effects=t['effectFlags'],
                strength_status=t['strengthStatus'],
                individualities=[Individuality(id=indv['id'],name=indv['name'])
                                for indv in t['individuality']],
                functions = functions
            ))
        return tds

def process_servant_json(servant_data):
    # 卡组属性
    source_deck = servant_data['cards']
    deck = []
    for card in source_deck:
        distribution = servant_data['hitsDistribution'][card]
        np_rate = servant_data['noblePhantasms'][0]['npGain'][card][0]
        deck.append(Card(card_type=card, np_rate=np_rate, hits_distribution=distribution) if distribution else Card(card_type=card, np_rate=np_rate))

    # 特性
    traits = []
    for trait in servant_data['traits']:
        traits.append(Individuality(name=trait['name'],id=trait['id']))

    svt = Servant(
        id = servant_data['id'],
        collection_no = servant_data['collectionNo'],
        name = servant_data['name'],
        name_cn = translate[servant_data['originalName']],
        # 其他属性
        class_name=servant_data['className'],
        rarity=servant_data['rarity'],
        max_atk=servant_data['atkMax'],
        max_hp=servant_data['hpMax'],
        star_absorb=servant_data['starAbsorb'],
        star_gen=servant_data['starGen'],   
        attribute=servant_data['attribute'],    
        cards=deck,
        traits=traits,    
        skills=extract_skills(servant_data['skills']),
        passive=extract_skills(servant_data['classPassive']),
        td = extract_td(servant_data['noblePhantasms']))
    
    return svt

def process_ce_json(ce_data):
    ce_id = ce_data['id']
    ce_name = ce_data['name']
    ce_collection_no = ce_data['collectionNo']
    ce_name_cn = ce_translate[ce_data['originalName']]
    type = ce_data['type']
    flag = ce_data['flag']
    rarity = ce_data['rarity']
    cost = ce_data['cost']
    max_atk = ce_data['atkMax']
    skills = []
    for sk in ce_data['skills']:
        functions = []
        auxiliary_skills = set()
        for func in sk['functions']:
            function_data, chained_skill = process_function_data(func)
            functions.append(function_data)
            if chained_skill:
                auxiliary_skills.update(chained_skill)
        
        for aux, level in auxiliary_skills:
            nice_skill_data = requests.get(nice_skills.format(skill_id=aux)).json()
            if nice_skill_data.get('detail','')=='Skill not found':
                continue
            nice_skill_data.update({'svtId':sk['svtId'],"num":-1,'type':'chained',})
            try:
                skills.extend(extract_skills([nice_skill_data],default_level=level))
            except Exception as e:
                print(f'Error fetching skill {ce_id} {aux}: {e}')
                raise Exception(f'Error fetching skill {aux}: {e}')  
        skills.append(Skill(
            id=sk['id'],
            skill_no=sk['num'],
            servant_id=sk['svtId'],
            name=sk['name'],
            skill_type=sk['type'],
            strengthStatus=sk['strengthStatus'],
            priority=sk['priority'],
            cooldown=sk['coolDown'][-1],
            functions=functions
        ))
    return CraftEssence(
        id=ce_id,
        collection_no=ce_collection_no,
        name=ce_name,
        name_cn=ce_name_cn,
        type=type,
        flag=flag,
        rarity=rarity,
        cost=cost,
        max_atk=max_atk,
        skills=skills
        
    )

def update_servants(basic_servants,collection):
    for svt in tqdm(basic_servants):
        svt_id = svt['id']
        svt_name = svt['name']
        try:
            nice_servants_data = requests.get(nice_servants.format(svt_id=svt_id)).json()
            svt_data = process_servant_json(nice_servants_data)
            collection.update_one({"_id": svt_data.id}, {"$set": svt_data.dict(by_alias=True)}, upsert=True)  # Insert if not found
        except IndexError:
            print(svt_id,svt_name)
            continue
        except Exception as e:
            print(svt_id,svt_name, e)
            raise Exception("Failed to update servant", svt_id, svt_name)
        time.sleep(0.1)  # To avoid hitting the rate limit    


collection = db['craft_essence']
def update_craft_essence(basic_ces,collection):
    for ce in tqdm(basic_ces):
        ce_id = ce['id']
        ce_name = ce['name']
        flag = ce['flag']
        if flag not in ['svtEquipEvent', 'svtEquipEventReward', 'normal']:  
            continue
        try:
            nice_ces_data = requests.get(nice_ces.format(ce_id=ce_id)).json()
            ce_data = process_ce_json(nice_ces_data)
            collection.update_one({"_id": ce_data.id}, {"$set": ce_data.dict(by_alias=True)}, upsert=True)  # Insert if not found
        except IndexError:
            print(ce_id,ce_name)
            continue
        time.sleep(0.15)  # To avoid hitting the rate limit


collection = db['servants']

# 读取已有的数据
def update_skills():
    svts = collection.find({})
    skill_collection = db['skills']
    for svt in tqdm(svts):
        skills = svt['skills']+svt['passive']
        for skill in skills:
            skill_doc = {
                "id":skill['id'],
                "servant_id":skill['servant_id'],
                "skill_no":skill['skill_no'],
                "name":skill['name'],
                "skill_type":skill['skill_type'],
                "strength_status":skill['strengthStatus'],
                "cooldown" : skill['cooldown'],
                "functions" : skill['functions']}
            skill_collection.update_one({"_id":ObjectId(),"skill_id": skill_doc['id'],"servant_id":skill['servant_id'],"strength_status":skill['strengthStatus']}, {"$set":skill_doc}, upsert=True)  # Insert if not found
    
    
    
def update_functions(collection):
    skills = collection.find({})
    function_collection = db['functions']
    skill_collection = db['skills']
    for sk in skills:
        funcs = sk['functions']
        for func in funcs:
            func_doc = {
                "id":func['id'],
                "function_type":func['function_type'],
                "target_type":func['target_type'],
                "target_team":func['target_team'],
            }
            function_collection.update_one({"_id":ObjectId(),"function_id": func_doc['id']}, {"$set":func_doc}, upsert=True)  # Insert if not found
            
    
    
if __name__ == "__main__":
    update_servants(basic_servants,db['servants'])    