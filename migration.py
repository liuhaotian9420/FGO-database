from scripts.etl import *
from scripts.connection import fetch_mongo_data

import concurrent.futures
import pymysql
import logging
import threading


from models.warehouse.base import *
from tqdm import tqdm    
from scripts.utils import mysql_operation


logger = logging.getLogger(__name__)
logger.setLevel('INFO')

handler = logging.FileHandler('servants_detail.log')
handler.suffix = '%Y-%m-%d'
handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(levelname)s : %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)



@mysql_operation()
def migrate_servant_data(session,documents):

    # 从者数据    
    for doc in tqdm(documents):
       servant = etl_servant_data_to_mysql(doc)
       cards =  etl_card_data_to_mysql(doc)
       skillsets = etl_skillset_data_to_mysql(doc)
       session.merge(servant)
       for c in cards:
            session.merge(c)
    #    for skillset in skillsets:
    #         session.merge(skillset)

@mysql_operation()
def migrate_craft_essence_data(session, documents):       
    # 礼装数据
    for doc in tqdm(documents):
        ce = etl_craft_essence_data_to_mysql(doc)
        ce_skillset = etl_craft_essence_skill_data_to_mysql(doc)
        session.merge(ce)
        for skillset in ce_skillset:
            session.merge(skillset)

if __name__ == "__main__":
    mongo_data = fetch_mongo_data('servants')
    migrate_servant_data(mongo_data)
    # craft_essences = fetch_mongo_data('craft_essence')        
    # migrate_craft_essence_data(craft_essences)
