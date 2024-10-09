
from sqlalchemy import create_engine, Table,Column, Integer, String, ForeignKey,Boolean,Float,BIGINT
from .base import Base

class SkillSet(Base):
    
    __tablename__ ='skillsets'
    id = Column(Integer, primary_key=True,default='')
    name = Column(String(255), nullable=True,)
    name_cn = Column(String(255), nullable=True,comment='中文名')
    skill_id = Column(Integer, primary_key=True,autoincrement=False)
    skill_name = Column(String(255), nullable=False,primary_key=True)
    skill_type = Column(String(255), nullable=True,index=True)
    skill_no = Column(Integer, index=True, nullable=True, default=-1)
    skill_priority = Column(Integer, index=True, nullable=True, default=-1)
    function_id = Column(Integer, primary_key=True)
    function_type = Column(String(255), nullable=True, index=True)
    function_release_order = Column(Integer, nullable=False, default=0,primary_key=True)
    function_target_type = Column(String(255), nullable=True, index=True)
    function_target_team = Column(String(255), nullable=True, index=True)
    function_quest_traits = Column(String(255),default='', nullable=True, comment='Quest Traits')
    function_target_traits = Column(String(255), default='',nullable=True, comment='技能的目标特性')
    buff_id = Column(Integer,primary_key=True,default=-1)
    buff_release_order = Column(Integer, nullable=False, default=0,primary_key=True)
    buff_name = Column(String(255), nullable=True)
    buff_type = Column(String(255), nullable=True, index=True)
    buff_check = Column(String(255),nullable=True,default='', comment='Buff检查')
    buff_target_traits = Column(String(255), nullable=True,default='', comment='Buff的目标特性')
    turn = Column(Integer, index=True,nullable=True,default=-1)
    count = Column(Integer, index=True,nullable=True,default=-1)
    value = Column(Float, nullable=True,default=-1,comment='技能效果的具体数值,dummy skill 会直接展开')
    userate=Column(Float, nullable=True,default=-1, comment='触发新的技能的概率')
    rate = Column(Float, nullable=True,default=-1)
    max_cooldown = Column(Integer, index=True, nullable=True,default=-1)
    strength_status = Column(Integer, index=True, nullable=True,comment='技能强化状态')