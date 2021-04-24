# -*- coding: utf-8 -*- 
# @Time : 2021/4/17 下午10:19 
# @Author : yuxiaoxue
# @File : saveAnjvke.py

import requests
from fake_useragent import UserAgent
import json

def get_page(url):
    try:
        data = requests.get(url,headers = {"user-agent":UserAgent().random})
        data.raise_for_status()
        return data.text
    except:
        print("出错了")

def parse_data(html):
    json_data = json.loads(html)['house_list_vo']
    houses = []
    try:
        for items in json_data:
            print('111')
    except:
        print("出错了")




if __name__=='__main__':
    url = 'https://beijing.anjuke.com/esf-ajax/property/info/pc/area/business/?city_id=14&page_size=10&area_id=642&from=SearchBar&page=1&select_type=0'
    result = get_page(url)
    print(result)

