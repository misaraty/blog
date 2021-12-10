#!/usr/bin/env python
# -*-coding:utf-8 -*-

import os
import re
import linecache
import math
import time
import shutil
# import numpy as np
from pyecharts import options as opts
from pyecharts.charts import Map
os.chdir(os.path.split(os.path.realpath(__file__))[0])

a1 = [
'海口'
,'拉萨'
,'丽水'
,'惠州'
,'深圳'
,'珠海'
,'舟山'
,'厦门'
,'黄山'
,'福州'
,'中山'
,'贵阳'
,'肇庆'
,'南宁'
,'江门'
,'雅安'
,'台州'
,'张家口'
,'东莞'
,'衢州'
,'石家'
,'包头'
,'安阳'
,'临汾'
,'太原'
,'邢台'
,'运城'
,'哈尔滨'
,'邯郸'
,'唐山'
,'咸阳'
,'渭南'
,'呼和浩特'
,'西安'
,'焦作'
,'鹤壁'
,'保定'
,'晋城'
,'沈阳'
,'淄博'
,'阳泉'
]
a2 = [
 -25
,-24
,-23
,-22
,-21
,-20
,-19
,-18
,-17
,-16
,-15
,-14
,-13
,-12
,-11
,-10
,-9
,-8
,-7
,-6
,25
,25
,24
,23
,22
,21
,19
,19
,17
,17
,16
,15
,14
,13
,12
,11
,10
,9
,8
,7
,6
]

output = (
    Map()
    .add("污染指数", zip(a1, a2), "china-cities", label_opts=opts.LabelOpts(is_show=False),is_map_symbol_show=False)
    .set_global_opts(
        title_opts=opts.TitleOpts(title="2020年4月生态环境部通报"),
        visualmap_opts=opts.VisualMapOpts(min_=-25, max_=25)
        )
    .render("重点城市环境空气排名.html")
)
