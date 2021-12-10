#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os
import shutil
os.chdir(os.path.split(os.path.realpath(__file__))[0])

n = 72  # poscar number

for i in range(1, n + 1):
    i = '%03d' % i
    if os.path.isdir(i):
        shutil.rmtree(i)
    if os.path.isdir(i):
        os.rmdir(i)
    elif os.path.isdir(i) == False:
        os.mkdir(i)

for i in range(1, n + 1):
    i = '%03d' % i
    shutil.copy('POTCAR', i)
    shutil.copy('KPOINTS', i)
    shutil.copy('INCAR', i)
    shutil.copy('POSCAR-' + i, i+'/POSCAR')

print('over.')
