from .base import Base
from sqlalchemy import Column, Integer, String


class Function(Base):
    
    __tablename__ = 'functions'
    
    function_id = Column(Integer, primary_key=True,autoincrement=False)
    function_type = Column(String(255),index=True)
    function_target_type = Column(String(255),index=True)
    function_target_team = Column(String(255),index=True)
    function_quest_vals = Column(String(255))


class Buff(Base):
    
    __tablename__ = 'buffs'
    
    buff_id = Column(Integer, primary_key=True,autoincrement=False)
    buff_name = Column(String(255),index=True)
    buff_type = Column(String(255), index=True)
    related_target_trait = Column(String(255), index=True)
    related_self_trait = Column(String(255), index=True)
    related_individuality = Column(String(255), index=True)
