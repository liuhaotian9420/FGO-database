'''
MongoDB 的数据向 Mysql 迁移的处理脚本
'''
from pymongo import MongoClient
from models.warehouse.skillset import SkillSet
from models.warehouse.servants import Servant,ServantCard
from models.warehouse.ce import CraftEssence,CraftEssenceSkill
from data.basics import ATK_MAX_BASE,CLASS_ATK_RATE
from scripts.data_process import process_skill,process_noblephantasm
from scripts.data_process import process_buff,process_function,process_skillvalue
import numpy as np

def etl_servant_data_to_mysql(document,model=Servant):
    
    id = document.get('id')
    collection_no = document.get('collection_no') 
    name = document.get('name')
    name_cn = document.get('name_cn')
    class_name = document.get('class_name')
    rarity = document.get('rarity')
    attack = document.get('max_atk')
    hp = document.get('max_hp')
    tendancy = round(attack / ATK_MAX_BASE[str(rarity)],2)
    star_absorb_rate = document.get('star_absorb')
    star_gen_rate = document.get('star_gen')
    attribute = document.get('attribute')
    class_mod = CLASS_ATK_RATE[class_name]/1000
    traits =','.join(t['name'] for t in  document.get('traits'))
    
    return Servant(
        id=id,
        collection_no=collection_no,
        name=name,
        name_cn=name_cn,
        class_name=class_name,
        rarity=rarity,
        attack=attack,
        hp=hp,
        tendancy=tendancy,
        star_absorb_rate=star_absorb_rate,
        star_gen_rate=star_gen_rate,
        attribute=attribute,
        class_mod=class_mod,
        traits=traits,
    )
    
    
def etl_card_data_to_mysql(document,model=ServantCard):
    
    servant_id = document.get('id')
    cards = document.get('cards')
    result = []
    for idx,c in enumerate(cards):
        card_id = str(servant_id)+'_'+str(idx+1)
        card_type = c.get('card_type')
        card_np = c.get('np_rate')
        card_hits = len(c.get('hits_distribution'))
        hits  = [str(h) for h in c.get('hits_distribution')]
        acc_hits = [str(h) for h in np.cumsum(np.array(c.get('hits_distribution')))]
        card_dist = ','.join(hits)
        card_dist_acc = ','.join(acc_hits)
        result.append(ServantCard(
            card_id=card_id,
            servant_id=servant_id,
            card_type=card_type,
            card_np=card_np,
            card_hits=card_hits,
            card_dist=card_dist,
            card_dist_acc=card_dist_acc,
        )
        )
    return result


def etl_skill_data_to_mysql():
    pass

def etl_craft_essence_data_to_mysql(document,model=CraftEssence):
    
    id = document.get('id')
    collection_no = document.get('collection_no') 
    name = document.get('name')
    name_cn = document.get('name_cn')
    cost = document.get('cost')
    flag = document.get('flag')
    max_atk = document.get('max_atk')
    return CraftEssence(
        id=id,
        collection_no=collection_no,
        name=name,
        name_cn=name_cn,
        cost=cost,
        flag=flag,
        max_atk=max_atk,
    )
    
def etl_craft_essence_skill_data_to_mysql(document,model=CraftEssenceSkill):
    
    id = document.get('id')
    name = document.get('name')
    name_cn = document.get('name_cn')
    skillset_entries = []
    for skill in document.get('skills'):
        common_skill_fields = process_skill(skill)
        common_skill_fields.pop('skill_no', None)
        common_skill_fields.pop('skill_priority',None)
        common_skill_fields.pop('max_cooldown',None)
        
        for func_idx,function in enumerate(skill.get('functions',[])):
            common_function_fields = process_function(function)
            common_function_fields.pop('function_target_team',None)
            common_function_fields['function_release_order'] = func_idx + 1
            basic_entry = {**common_skill_fields,**common_function_fields}
            skillvalue = process_skillvalue(function.get('skillvalues',[]))
            basic_entry.update(skillvalue)
            if not function.get('buffs'):
                skillset_entries.append(CraftEssenceSkill(
                    id = id,
                    name = name,
                    name_cn = name_cn,
                    **basic_entry))
            for buff_idx,buff in enumerate(function.get('buffs',[])):
                skillset_entry = {**basic_entry,**process_buff(buff),**{'buff_release_order':buff_idx + 1}}
                skillset_entries.append(CraftEssenceSkill(
                    id = id,
                    name = name,
                    name_cn = name_cn,
                    **skillset_entry))

    return skillset_entries
    

def etl_skillset_data_to_mysql(document,model=SkillSet):
    
    id = document.get('id')
    name = document.get('name')
    name_cn = document.get('name_cn')
    skillset_entries = []
    for skill in document.get('skills') + document.get('passive'):
        common_skill_fields = process_skill(skill)
        for func_idx,function in enumerate(skill.get('functions',[])):
            common_function_fields = process_function(function)
            common_function_fields['function_release_order'] = func_idx + 1
            basic_entry = {**common_skill_fields,**common_function_fields}
            skillvalue = process_skillvalue(function.get('skillvalues',[]))
            basic_entry.update(skillvalue)
            
            if not function.get('buffs'):
                skillset_entries.append(SkillSet(id = id, name = name, name_cn = name_cn, **basic_entry))
            
            for buff_idx,buff in enumerate(function.get('buffs',[])):
                skillset_entry = {**basic_entry,**process_buff(buff),**{'buff_release_order':buff_idx + 1}}
                skillset_entries.append(SkillSet(
                    id = id,
                    name = name,
                    name_cn = name_cn,
                    **skillset_entry))
                   
    for np in document.get('td',[]):
            
        common_np_field = process_noblephantasm(np)
        for func_idx,function in enumerate(np.get('functions',[])):
            common_function_fields = process_function(function)
            common_function_fields['function_release_order'] = func_idx + 1
            basic_entry = {**common_np_field,**common_function_fields}
            skillvalue = process_skillvalue(function.get('skillvalues',[]))
            basic_entry.update(skillvalue)
            
            if not function.get('buffs'):
                skillset_entries.append(SkillSet(id = id, name = name, name_cn = name_cn, **basic_entry))
            
            for buff_idx,buff in enumerate(function.get('buffs',[])):
                skillset_entry = {**basic_entry,**process_buff(buff),**{'buff_release_order':buff_idx + 1}}
                skillset_entries.append(SkillSet(
                    id = id,
                    name = name,
                    name_cn = name_cn,
                    **skillset_entry))
                
    return skillset_entries


    
                
        
    