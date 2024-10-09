from .base import Base
from sqlalchemy import Column, Integer, String,Float


class CraftEssence(Base):
    
    __tablename__ = 'craft_essences'
    id = Column(Integer, primary_key=True,autoincrement=False)
    collection_no = Column(Integer, index=True)
    name = Column(String(255))
    name_cn = Column(String(255), default='',comment='中文名')
    cost =  Column(Integer,index=True)
    max_atk = Column(Integer, index=True)
    flag = Column(String(255),index=True)

class CraftEssenceSkill(Base):
    
    __tablename__ = 'craft_essence_skills'
    
    id = Column(Integer, primary_key=True,autoincrement=False)
    name = Column(String(255))
    name_cn = Column(String(255), default='',comment='中文名')
    skill_id = Column(Integer, primary_key=True, autoincrement=False)
    skill_name = Column(String(255), comment='技能名')
    skill_type = Column(String(255), comment='技能类型')
    strength_status = Column(Integer, default=-1)
    function_id = Column(Integer, primary_key=True, autoincrement=False)
    function_type = Column(String(255), default='')
    function_target_type = Column(String(255), default='',index=True)
    function_release_order = Column(Integer, default=-1,primary_key=True)
    function_quest_traits = Column(String(255), default='')
    function_target_traits = Column(String(255), default='')
    buff_id = Column(Integer,primary_key=True,default=-1)
    buff_release_order = Column(Integer, nullable=False, default=0,primary_key=True)
    buff_name = Column(String(255), nullable=True)
    buff_type = Column(String(255), nullable=True, index=True)
    buff_check = Column(String(255),nullable=True,default='', comment='Buff检查')
    buff_target_traits = Column(String(255), nullable=True,default='', comment='Buff的目标特性')
    turn = Column(Integer,default=-1)
    count = Column(Integer,default=-1)
    value = Column(Float, default=-1)
    userate = Column(Float, default=-1)
    rate = Column(Float, default=-1)
    