from sqlalchemy import create_engine, Table,Column, Integer, String, ForeignKey,Boolean,Float,BIGINT
from .base import Base

class Servant(Base):
    
    __tablename__ ='servants'
    
    id = Column(Integer, primary_key=True,autoincrement=False)
    collection_no = Column(Integer,index=True)
    name = Column(String(255))
    name_cn = Column(String(255),comment='从者的中文名')
    class_name = Column(String(255),index=True,comment='从者职介')
    rarity = Column(Integer,index=True,comment='从者的稀有度')
    attack = Column(Integer, comment='从者满级的攻击力')
    hp = Column(Integer,comment='从者满级的生命值')
    tendancy = Column(Float,comment = '从者的攻防倾向')
    star_absorb_rate = Column(Integer, comment='暴击星集中度')
    star_gen_rate = Column(Integer, comment='星集中度')
    class_mod = Column(Integer, comment='职介系数')
    attribute = Column(String(255), comment='从者阵营')
    traits = Column(String(1000), comment='从者的特性')

class ServantCard(Base):
    
    __tablename__ ='servant_cards'
    
    card_id = Column(String(255), primary_key=True,)
    servant_id = Column(Integer,)
    card_type = Column(String(255), index=True)
    card_np = Column(Integer, comment='指令卡的 NP值')
    card_hits = Column(Integer, comment='指令卡的 hit 数')
    card_dist =  Column(String(255), comment='指令卡的 hit')
    card_dist_acc = Column(String(255), comment='指令卡累计hit比率')




    


