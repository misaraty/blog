#!/usr/bin/env python
# -*-coding:utf-8 -*-

import os
import re
import linecache
import math
import random
# import time
# import datetime
import shutil
# import numpy as np
import requests
from lxml import etree
# import matplotlib.pyplot as plt
os.chdir(os.path.split(os.path.realpath(__file__))[0])

 
url = 'https://www.aqistudy.cn/historydata/'

# 头部信息，将该请求伪装成浏览器的请求
# headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'}
headers = {'user-agent': 'Baiduspider+(+http://www.baidu.com/search/spider.htm)'}
# headers = {'user-agent': 'Googlebot/2.1(+http://www.google.com/bot.html)'}
# user_agent_list = [
    # 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36',
    # 'Baiduspider+(+http://www.baidu.com/search/spider.htm)',
    # 'Googlebot/2.1(+http://www.google.com/bot.html)'
# ]
# headers ={
    # 'User-Agent': 'random.choice(user_agent_list)'
# }
# https://developers.whatismybrowser.com/useragents/explore/software_name/baidu-spider/
# https://developers.google.com/search/docs/advanced/crawling/overview-google-crawlers
# https://www.cnblogs.com/byeb/articles/9942858.html

ip_list = [
    '60.167.135.117:1133',
    '116.27.98.201:9999',
    '183.166.21.49:9999'
]
proxies = {
    'http': random.choice(ip_list)
}
# proxies = {
  # 'http': 'http://10.10.1.10:3128',
  # 'https': 'http://10.10.1.10:1080',
# }

# https://gohom.win/2016/01/21/proxy-py/
# https://blog.csdn.net/qq_39610888/article/details/81209647
# https://www.kuaidaili.com/free/

response = requests.get(url=url, headers=headers, proxies=proxies)
response.encoding = 'utf-8'
tree = etree.HTML(response.text)
city = tree.xpath('/html/body/div[3]/div/div[1]/div[2]/div[2]/ul/div[2]/li/a/text()')
print(city)    
    
######    
# https://blog.csdn.net/qq_37251994/article/details/107844882
# https://blog.csdn.net/qq_37251994/article/details/108132122
# https://blog.51cto.com/13760351/2512753

























