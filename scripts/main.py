import json
import concurrent.futures
from scripts.utils import mysql_operation
from sqlalchemy.orm import sessionmaker,scoped_session
from sqlalchemy import text
from models.warehouse.base import *
from sqlalchemy import exc
from tenacity import retry, wait_exponential, stop_after_attempt
import pymysql
from tqdm import tqdm    
import logging
import threading

engine_uri = 'mysql+pymysql://developer:VhUdQSBX8H3NmTA@118.195.250.136:14306/fgo'

# MySQL connection string

logger = logging.getLogger(__name__)
logger.setLevel('INFO')

handler = logging.FileHandler('servants_detail.log')
handler.suffix = '%Y-%m-%d'
handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(levelname)s : %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)

# Lock for serializing access to potentially conflicting operations
lock = threading.Lock()

def retry_if_integrity_error(exception):
    return isinstance(exception, pymysql.err.IntegrityError)


def add_new_servant_with_retry(session, servant_data):
    return add_new_servant(session, servant_data['id'])


        
def init_craft_essences_to_db(ces,max_threads=3):
    with concurrent.futures.ThreadPoolExecutor(max_workers=max_threads) as executor:
        list(tqdm(executor.map(process_craft_esssence, ces), total=len(ces)))    

def init_servants_to_db(svts,max_threads=4):
    with concurrent.futures.ThreadPoolExecutor(max_workers=max_threads) as executor:
        list(tqdm(executor.map(process_servant, svts[200:]), total=len(svts[200:])))
    