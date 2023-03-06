# -*- coding: UTF-8 -*-
'''
@Project ：猿人学 
@File    ：asd.py
@IDE     ：PyCharm 
@Author  ：karease
@Date    ：2023/2/17 12:27 
'''

import requests

url = 'https://www.42verse.shop/market'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'
}

response = requests.get(url = url,headers = headers)
print(response.text)