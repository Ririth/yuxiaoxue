# -*- coding: utf-8 -*- 
# @Time : 2021/4/17 下午8:37 
# @Author : yuxiaoxue
# @File : saveMovieCommets.py
import pandas as pd
import requests
import json
from fake_useragent import UserAgent

# 获取页面内容
def get_page(url):
    headers = {
        'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit'
                      '/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1',
        'accept': '*/*'
    }
    try:
        r = requests.get(url,headers = {"user-agent":UserAgent().random})
        r.raise_for_status()
        return r.text
    except requests.HTTPError as e:
        print(e)
    except requests.RequestException as e:
        print(e)
    except:
        print("出错了")

# 解析接口返回数据
def parse_data(html):
    json_data = json.loads(html)['cmts']
    comments = []
    # 解析数据并存入数组
    try:
        for item in json_data:
            comment = []
            comment.append(item['nickName']) # 昵称
            comment.append(item['cityName'] if 'cityName' in item else '') # 城市
            comment.append(item['content'].strip().replace('\n', '')) # 内容
            comment.append(item['score']) # 星级
            comment.append(item['startTime'])
            comment.append(item['time']) # 日期
            comment.append(item['approve']) # 赞数
            comment.append(item['reply']) # 回复数
            if 'gender' in item:
                comment.append(item['gender'])  # 性别
            comments.append(comment)
        return comments
    except Exception as e:
        print(comment)
        print(e)

# 保存数据，写入 csv
def save_data(comments):
    filename = 'comments.csv'
    dataObject = pd.DataFrame(comments)
    dataObject.to_csv(filename, mode='a', index=False, sep=',', header=False, encoding='utf_8_sig')

if __name__ == '__main__':
    url = 'https://m.maoyan.com/mmdb/comments/movie/1299372.json?_v_=yes&offset=15&startTime=2021-04-17'
    url = 'https://m.maoyan.com/mmdb/comments/movie/1299372.json?_v_=yes&offset=15&startTime=0'
    result = get_page(url)
    print(result)
    comments = parse_data(result)
    print(comments)
    save_data(comments)