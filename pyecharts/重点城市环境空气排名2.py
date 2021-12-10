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
'北京',
'上海',
'广东省'
]
a2 = [
1,
2,
3
]

output = (
    Map()
    .add("污染指数", zip(a1, a2), "china",is_map_symbol_show=False)
    .set_global_opts(
        title_opts=opts.TitleOpts(title="2020年4月生态环境部通报"),
        visualmap_opts=opts.VisualMapOpts(min_=1, max_=3)
        )
    .render("重点城市环境空气排名2.html")
)
