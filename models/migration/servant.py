from pydantic import BaseModel, Field
from typing import List, Optional
from bson import ObjectId
from statics import Individuality,SkillValue,Buff,Function,Skill


    
class Card(BaseModel):
    
    id: Optional[str] = Field(None,alias='_id')
    card_type:str
    np_rate:float=Field(0,alias='npRate')
    hits_distribution:Optional[List[int]]

class NoblePhantom(BaseModel):
    
    id: Optional[int] = Field(None,alias='_id')
    card:Card
    effects:Optional[List[str]]
    strength_status:int = Field(0,alias='strengthStatus')
    individualities:Optional[List[Individuality]]
    functions:Optional[List[Function]]

class Servant(BaseModel):
    
    id:Optional[str] = Field(None,alias='_id')
    collection_no:str=Field(None,alias='collectionNo')
    name:str=Field(None,alias='Name')
    name_cn:str
    class_name:str=Field(None,alias='className')
    rarity:int=Field(None,alias='rarity')
    np_rate:float=Field(None,alias='npRate')
    max_atk:int=Field(None,alias='atkMax')
    max_hp:int=Field(None,alias='hpMax')
    star_absorb:int=Field(None,alias='starAbsorb')
    star_gen:int=Field(None,alias='starGen')
    attribute:str
    traits:Optional[List[Card]]
    skills:Optional[List[Skill]]
    passive:Optional[List[Skill]]
    td:Optional[List[NoblePhantom]]
    
    
    
    