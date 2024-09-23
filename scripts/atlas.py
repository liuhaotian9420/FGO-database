'''
从 atlas-academy 中下载基础礼装相关数据
'''
import requests
import json

basic_servants = 'https://api.atlasacademy.io/export/JP/basic_servant_lang_en.json'
basic_ces = 'https://api.atlasacademy.io/export/JP/basic_equip_lang_en.json'


def download_data(url):
    file_name = url.split('/')[-1]
    with open(f'data/{file_name}', 'w', encoding='utf-8') as f:
        response = requests.get(url)
        json.dump(response.json())

if __name__ == '__main__':
    download_data(basic_servants)
    download_data(basic_ces)