import os
from urllib.parse import urlparse
import json

from sqlalchemy import create_engine, inspect,func
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import SQLAlchemyError
from functools import wraps
from pymysql import err
from collections import defaultdict
from models.warehouse.base import Base

engine_uri = 'mysql+pymysql://developer:dick920815@129.211.170.79:3306/fgo'

# MySQL connection string
mysql_engine = create_engine(engine_uri,pool_size=25, max_overflow=30)
mysql_session = sessionmaker(bind=mysql_engine)

Base.metadata.create_all(mysql_engine)

def mysql_operation(messages=None):
    if messages is None:
        messages = {}
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            session = mysql_session()
            try:
                result = func(session, *args, **kwargs)
                session.commit()
                return result
            except SQLAlchemyError as e:
                session.rollback()
                error_type = type(e).__name__
                if error_type == 'IntegrityError':
                    raise err.IntegrityError(f"IntegrityError in {func.__name__}: {str(e)}")
                custom_message = messages.get(error_type, f"Error in {func.__name__}")
                raise Exception(f"{custom_message}: {str(e)}") from e
            finally:
                session.close()
        return wrapper
    return decorator


def check_cache(url,cache_dir='cache'):
    parsed_url = urlparse(url)
    filename = '_'.join(parsed_url.path.split('/'))
    if os.path.isfile(os.path.join(cache_dir,filename+'.json')):
        with open(os.path.join(cache_dir,filename+'.json'),'r') as f:
            return json.load(f)
    else:
        return None
    
def add_cache(data,url,cache_dir='cache'):
    parsed_url = urlparse(url)
    filename = '_'.join(parsed_url.path.split('/'))
    with open(os.path.join(cache_dir,filename+'.json'),'w') as f:
        json.dump(data,f,indent=4)
        

def reverse_list_mapping(mapping:defaultdict[str,list[str]]):
    '''
    reverse key and value in a defaultdict
    '''
    new_dict = defaultdict(list)
    for k, v in mapping.items():
        for val in v:
            new_dict[val].append(k)
    return new_dict
        
        
    