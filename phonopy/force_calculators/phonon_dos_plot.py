#!/usr/bin/env python
# -*- coding:utf-8 -*-
import os
import re
import linecache
import math
import numpy as np
from scipy import optimize
from matplotlib import pyplot as plt
os.chdir(os.path.split(os.path.realpath(__file__))[0])

a1 = np.loadtxt('total_dos.dat', skiprows=1)
a2 = a1[:, 0]*33.35641  # x
a3 = a1[:, -1]  # y

plt.xlabel('Frequency (cm$^-$$^1$)')
plt.ylabel('Density of states')
plt.xlim(0, max(a2))
plt.ylim(0, max(a3) * 1.2)
plt.plot(a2, a3, 'r-')
plt.savefig('raman.jpg', dpi=300)
plt.show()
