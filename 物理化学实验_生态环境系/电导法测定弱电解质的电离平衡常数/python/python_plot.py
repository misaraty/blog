#!/usr/bin/env python
# -*-coding:utf-8 -*-

import os
import numpy as np
import matplotlib.pyplot as plt
os.chdir(os.path.split(os.path.realpath(__file__))[0])

# 数据
data = [
    [9.676E-6, 415.87433],
    [1.497E-5, 672.01069],
    [2.05E-5, 981.46341],
    [2.48E-5, 1216.93548],
    [2.85E-5, 1410.87719],
    [3.42E-5, 1470.76023]
]

x, y = zip(*data)

# 拟合数据
coefs = np.polyfit(x, y, 1)
fit_func = np.poly1d(coefs)

# 绘图
plt.scatter(x, y, color='tab:blue', label='Data Points')
plt.plot(x, fit_func(x), color='tab:red', label=f'Fit: y = {coefs[0]:.4f}x + {coefs[1]:.4f}')
plt.xlabel(r'$c \times \frac{\Lambda_m}{c^{\ominus}}$')
plt.ylabel(r'$\frac{1}{\Lambda_m}$')
plt.legend()
plt.grid(True)

# 保存到本地
plt.tight_layout()
plt.savefig("result.jpg", dpi=300)
plt.show()


















