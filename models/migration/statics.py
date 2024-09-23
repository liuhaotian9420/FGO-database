from pydantic import BaseModel, Field
from typing import List, Optional
from bson import ObjectId


class Individuality(BaseModel):
    
    id: Optional[str] = Field(None, alias='_id')
    name: str
    
    
class SkillValue(BaseModel):
    
    rate:int = Field(-1, alias='Rate')
    value: int = Field(-1, alias='Value')
    turn: int = Field(-1, alias='Turn')
    count:int = Field(-1, alias='Count')
    userate: int
    value2: int
    
class Buff(BaseModel):
    
    id:Optional[int] = Field(None, alias='_id')
    name:str
    type:str
    vals: Optional[List[Individuality]] 
    tvals: Optional[List[Individuality]]
    max_rate: int = Field(-1, alias='maxRate')
    check_self:Optional[List[Individuality]] 
    check_op: Optional[List[Individuality]]


class Function(BaseModel):
    
    id: Optional[int] = Field(None,alias='_id')
    function_type:str
    target_type:str
    target_team:str
    trait_values:Optional[List[Individuality]]
    buffs:Optional[List[Buff]]
    skillvalues: Optional[List[SkillValue]]
    
class Skill(BaseModel):
    
    id: Optional[int] = Field(None, alias='_id')
    servant_id: Optional[str] = Field(None, alias='svtId')
    skill_no:Optional[int] = Field(None, alias='skillNo')
    name: str
    skill_type:str
    strength_status:int = Field(0, alias='strengthStatus')
    priority: int = Field(0, alias='priority')
    cooldown:int = Field(-1, alias='cooldown')
    functions: Optional[List[Function]] = Field(None, alias='functions')
    