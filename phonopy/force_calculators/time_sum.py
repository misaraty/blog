#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os
import re
import linecache
import math
os.chdir(os.path.split(os.path.realpath(__file__))[0])

n = 72  # poscar number

b1 = []
for i in range(1, n + 1):
    i = '%03d' % i
    a1 = linecache.getlines('./' + i + '/OUTCAR')[-11]
    a2 = a1.strip().split(' ')[-1]
    b1.append(float(a2))
b2 = sum(b1)
b2 = float(b2) / 60 / 60
print('Total Time: ' + str(b2))
print('over.')

# a = open('OUTCAR')
# b = open('energy', 'w+')
# for line in a:
# line = line.rstrip()
# if not re.search('  energy  without entropy', line):
# continue
# print(line, file=b)
# b.close()
# a.close()
