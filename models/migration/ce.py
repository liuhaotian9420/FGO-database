from pydantic import BaseModel, Field
from .statics import  Individuality, Skill, Function, Buff, SkillValue
from typing import List, Optional
from bson import ObjectId


class CraftEssence(BaseModel):
    
    id: Optional[int]
    collection_no: int
    name: str
    name_cn: str
    type:str
    flag:Optional[str]
    rarity: Optional[int]
    cost: Optional[int]
    max_atk: Optional[int]
    skills:Optional[List[Skill]]
    
    