#!/usr/bin/env python
# -*-coding:utf-8 -*-

import os
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress
os.chdir(os.path.split(os.path.realpath(__file__))[0])

# Concentration data c (mg·L^-1)
c = np.array([5, 10, 15, 20, 25, 30])
# Absorbance data A
A = np.array([0.021, 0.034, 0.042, 0.054, 0.067, 0.086])

# Performing linear regression
slope, intercept, r_value, p_value, std_err = linregress(c, A)

# Generating points for the regression line
inv_T_line = np.linspace(np.min(c), np.max(c), 500)
y_line = slope * inv_T_line + intercept

# Plotting the data and the linear fit
plt.figure(figsize=(8, 6))
plt.scatter(c, A, color='tab:blue', label='Data points')
plt.plot(inv_T_line, y_line, color='tab:orange', label=f'Fit: y = {slope:.6f}x + {intercept:.6f}')

# Setting plot labels and title
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.xlabel('c(mg·L$^{-1}$)', fontsize=14)
plt.ylabel('A', fontsize=14)
plt.legend(fontsize=12)
plt.grid(True)
plt.tight_layout()
plt.savefig("result.jpg", dpi=300)
plt.show()
