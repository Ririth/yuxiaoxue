# -*- coding: utf-8 -*-
# @Time : 2021/5/3 下午6:50
# @Author : yuxiaoxue
# @File : interfaceDemo.py

import requests
import json


url = 'http://l-horizon2.beta.p1.11bee.com:8087/honeycomb/bag/tab/find'
data = {
    'pageIndex': 1,
    'pageSize': 10
}

resp = requests.post(url,data)
result = json.loads(resp.text)
# print(result)

# data = result['data']
msg = result['message']
assert msg == '操作成功','操作失败'
# print('111',data)
# print(len(data))


