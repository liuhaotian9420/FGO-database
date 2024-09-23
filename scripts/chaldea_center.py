'''
从 Chaldea-center 当中下载汉化的数据
'''
import requests
import json

entry_point = 'https://raw.githubusercontent.com/chaldea-center/chaldea-data/main/mappings/{file_name}.json'

servant_names = entry_point.format(file_name='svt_names')
ce_names = entry_point.format(file_name='ce_names')


def reprocess_chaldea_center_data(data):
    return {original_name:(chaldea_name.get('CN',None) or chaldea_name.get('TW',None)) for original_name, chaldea_name in data.items()}

def download_chaldea_center_data(url):
    
    response = requests.get(url)
    file_name = url.split('/')[-1]
    with open(f'data/{file_name}.json', 'w', encoding='utf-8') as f:
        json.dump(reprocess_chaldea_center_data(response.json()), f, ensure_ascii=False)
        

if __name__ == '__main__':
    download_chaldea_center_data(servant_names)
    download_chaldea_center_data(ce_names)