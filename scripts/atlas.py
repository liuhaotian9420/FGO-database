'''
从 atlas-academy 中下载基础礼装相关数据
'''
import requests
import json
from utils import check_cache, add_cache

basic_servants = 'https://api.atlasacademy.io/export/JP/basic_servant_lang_en.json'
basic_ces = 'https://api.atlasacademy.io/export/JP/basic_equip_lang_en.json'


def download_data(url):
    file_name = url.split('/')[-1]
    with open(f'data/{file_name}', 'w', encoding='utf-8') as f:
        response = requests.get(url)
        json.dump(response.json())
        

def lookup_function(function_id):
    url = 'https://api.atlasacademy.io/basic/JP/function/{function_id}'
    cache = check_cache(url.format(function_id=function_id))
    if not cache:
        response = requests.get(url.format(function_id=function_id))
        if response.status_code == 200:
            # add_cache(response.json(), url.format(function_id=function_id))
            return response.json()
        else:
            raise Exception('Failed to fetch function data:',response.status_code,'-',response.text)
    return cache
