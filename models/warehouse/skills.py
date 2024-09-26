from .base import Base
from sqlalchemy import Column, Integer, String 


class NoblePhantasm(Base):
    
    __tablename__ ='noble_phantasms'
    
    noble_phantasm_id = Column(Integer, primary_key=True, autoincrement=False)
    servant_id = Column(Integer, primary_key=True, autoincrement=False)
    strength_status = Column(Integer, comment='宝具是否强化',primary_key=True)
    noble_phantasm_name = Column(String(255))
    servant_name = Column(String(255),index=True)
    type = Column(String(255), index=True)
    card_type = Column(String(255),index=True)

    

class Skill(Base):
    
    __tablename__='skills'
    
    skill_id = Column(Integer, primary_key=True,autoincrement=False)
    skill_name = Column(String(255))
    skill_type = Column(String(255),index=True)
    