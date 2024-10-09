'''
计算器相关
'''

from data.basics import *


def grailed_atk(rarity:int,atk:int,grailed_level:int)-> int:
    
    max_atk = ATK_MAX_BASE[str(rarity)] 
    min_atk = ATK_MIN_BASE[str(rarity)] 
    tendancy = ( atk / max_atk)
    level_adjust = round((grailed_level-1) / (MAX_LEVEL[str(rarity)]-1),3)
    new_atk = tendancy* (min_atk + (max_atk - min_atk) * level_adjust)
    return int(new_atk)
