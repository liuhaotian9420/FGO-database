'''
对于游戏内的基础数据进行处理
SKills
Buffs
Functions
'''

def lst_to_str(lst,key):
    return ','.join(str(d.get(key)) for d in lst) if lst and key in lst else ''
    

def process_buff(data):
    
    id = data.get('id')
    name = data.get('name')
    type = data.get('type')
    traits = lst_to_str(data.get('tvals',[]),'name')
    checks = (
            lst_to_str(data.get('check_self',[]),'name')
             +lst_to_str(data.get('check_op',[]),'name')
             )
    return {
        'buff_id':id,
        'buff_name':name,
        'buff_type':type,
        'buff_target_traits':traits,
        'buff_check':checks        
    }

def process_skillvalue(data:list[dict],level=-1)-> dict:
    level_data = data[level]
    rate = level_data.get('rate')
    value = level_data.get('value')
    turn = level_data.get('turn')
    count = level_data.get('count')
    userate = level_data.get('userate')
    
    return {
        'rate':rate,
        'value':value,
        'turn':turn,
        'count':count,
        'userate':userate,
    }
    
    
def process_function(data):
    
    id = data.get('id')
    type = data.get('function_type')
    target_type = data.get('target_type')
    target_team = data.get('target_team')
    traits = lst_to_str(data.get('trait_values',[]),'name')
    
    return {
        'function_id':id,
        'function_type':type,
        'function_target_type':target_type,
        'function_target_team':target_team,
        'function_target_traits':traits,  
    }
    
    
def process_skill(data):

    id = data.get('id')
    servant_id = data.get('servant_id')
    skill_no = data.get('skill_no')
    name = data.get('name')
    skill_type = data.get('skill_type')
    skill_priority = data.get('skill_priority')
    strength_status = data.get('strengthStatus')
    cooldown = data.get('cooldown')
    
    return {
        'skill_id':id,
        'skill_no':skill_no,
        'skill_name':name,
        'skill_type':skill_type,
        'skill_priority':skill_priority,
        'strength_status':strength_status,
        'max_cooldown':cooldown,
    }
    
def process_noblephantasm(data):
    
    id = data.get('id')
    name = data.get('name')
    skill_type = data.get('effects')[-1] 
    strength_status = data.get('strength_status')
    max_cooldown = -1
    return {
        'skill_id':id,
        'skill_name':name,
        'skill_no':-1,
        'skill_type':skill_type,
        'strength_status':strength_status,
        'max_cooldown':max_cooldown,
    }