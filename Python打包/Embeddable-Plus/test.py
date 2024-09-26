#!/usr/bin/env python
# -*-coding:utf-8 -*-

import os
import re
import linecache
import math
# import time
# import datetime
import shutil
import numpy as np
import matplotlib.pyplot as plt
os.chdir(os.path.split(os.path.realpath(__file__))[0])

a=[0.000455,0.00235,0.0567,0.0468,0.00466,0.00653]
b=np.sqrt(a)*1000
print(b)

a2=[1,2,3,4,5]
a3=[100,120,30,300,500]

plt.xlabel('x')
plt.ylabel('y')
# plt.xlim(-4, 4)  # x显示区间
# plt.ylim(0, 200)  # y显示区间
plt.plot(a2, a3, 'r-', label='XXX')
plt.legend(loc='best', fontsize=12)
plt.savefig('dos.jpg', dpi=300)  # 屏幕显示pic，可注释
plt.show()

os.system("pause")





















