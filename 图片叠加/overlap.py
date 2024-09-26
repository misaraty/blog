#!/usr/bin/env python
# -*-coding:utf-8 -*-

import os
import re
import linecache
import math
import shutil
import numpy as np
# import pandas as pd
# import matplotlib.pyplot as plt
import cv2
os.chdir(os.path.split(os.path.realpath(__file__))[0])
print('copyright by Zhaosheng Zhang (misaraty@163.com)' + '\n' + 'last update: 2022-06-25')

# pip install opencv-python
# 权重越大，透明度越低

x1 = 0.4
x2 = 1-x1

over1 = cv2.addWeighted(cv2.imread('20220625.jpg'), x1, cv2.imread('20220624.jpg'), x2, 0)
cv2.imwrite('./over1.jpg', over1)

over2 = cv2.addWeighted(cv2.imread('over1.jpg'), x1, cv2.imread('20220622.jpg'), x2, 0)
cv2.imwrite('./over2.jpg', over2)

over3 = cv2.addWeighted(cv2.imread('over2.jpg'), x1, cv2.imread('20220620.jpg'), x2, 0)
cv2.imwrite('./over3.jpg', over3)

over4 = cv2.addWeighted(cv2.imread('over3.jpg'), x1, cv2.imread('20220617.jpg'), x2, 0)
cv2.imwrite('./over4.jpg', over4)

over5 = cv2.addWeighted(cv2.imread('over4.jpg'), x1, cv2.imread('20220616.jpg'), x2, 0)
cv2.imwrite('./over5.jpg', over5)































