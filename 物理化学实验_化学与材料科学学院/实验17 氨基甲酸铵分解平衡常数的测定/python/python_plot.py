#!/usr/bin/env python
# -*-coding:utf-8 -*-

import os
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress
os.chdir(os.path.split(os.path.realpath(__file__))[0])

# Temperature data (T/K)
T = np.array([293.53, 299.04, 303.98, 308.75, 313.47, 318.77])
# Y-axis data
y = np.array([-5.07, -4.93, -4.75, -4.52, -4.23, -4.05])

# Converting T to 1/T
inv_T = 1 / T

# Performing linear regression
slope, intercept, r_value, p_value, std_err = linregress(inv_T, y)

# Generating points for the regression line
inv_T_line = np.linspace(np.min(inv_T), np.max(inv_T), 500)
y_line = slope * inv_T_line + intercept

# Plotting the data and the linear fit
plt.figure(figsize=(8, 6))
plt.scatter(inv_T, y, color='tab:blue', label='Data points')
plt.plot(inv_T_line, y_line, color='tab:orange', label=f'Fit: y = {slope:.2f}x + {intercept:.2f}')

# Setting plot labels and title
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.xlabel('1/T (1/K)', fontsize=14)
plt.ylabel(r'${lnK^{\ominus}}$', fontsize=14)
plt.legend(fontsize=12)
plt.grid(True)
plt.tight_layout()
plt.savefig("result.jpg", dpi=300)
plt.show()
