from pydantic import BaseModel, Field
from typing import List, Optional
from bson import ObjectId
from .statics import Individuality,SkillValue,Buff,Function,Skill


    
class Card(BaseModel):
    
    
    card_type:str
    np_rate:float
    hits_distribution:Optional[List[int]]

class NoblePhantasm(BaseModel):
    
    id: Optional[int]
    name:Optional[str]
    card:Card
    effects:Optional[List[str]]
    strength_status:int
    individualities:Optional[List[Individuality]]
    functions:Optional[List[Function]]

class Servant(BaseModel):
    
    id:Optional[int]
    collection_no:int
    name:str
    name_cn:str
    class_name:str
    rarity:int
    max_atk:int
    max_hp:int
    star_absorb:int
    star_gen:int
    attribute:str
    cards:Optional[List[Card]]
    traits:Optional[List[Individuality]]
    skills:Optional[List[Skill]]
    passive:Optional[List[Skill]]
    td:Optional[List[NoblePhantasm]]
    
    
    
    