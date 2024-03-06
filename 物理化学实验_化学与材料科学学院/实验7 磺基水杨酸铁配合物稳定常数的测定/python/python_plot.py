#!/usr/bin/env python
# -*-coding:utf-8 -*-

import os
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
from scipy.interpolate import make_interp_spline
os.chdir(os.path.split(os.path.realpath(__file__))[0])

# Data points
x_R = np.array([0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0])
A = np.array([0, 0.102, 0.185, 0.267, 0.342, 0.398, 0.338, 0.256, 0.183, 0.109, 0])

# Smooth curve
x_R_smooth = np.linspace(x_R.min(), x_R.max(), 300)
spl = make_interp_spline(x_R, A, k=3)  # B-spline of order 3
A_smooth = spl(x_R_smooth)

# Identifying the peak and its coordinates from the smooth curve
peak_idx = np.argmax(A_smooth)
peak_x, peak_y = x_R_smooth[peak_idx], A_smooth[peak_idx]

# Linear regression on both sides of the peak - using original data points for regression
# Identifying nearest original data points around the peak for linear fitting
left_side_x = x_R[x_R < peak_x]
left_side_y = A[x_R < peak_x]

right_side_x = x_R[x_R > peak_x]
right_side_y = A[x_R > peak_x]

# Linear regression on both sides
slope_left, intercept_left, _, _, _ = stats.linregress(left_side_x, left_side_y)
slope_right, intercept_right, _, _, _ = stats.linregress(right_side_x, right_side_y)

# Calculating the intersection point using the left extension
A_1 = slope_left * peak_x + intercept_left

# Plotting the results
plt.figure()
plt.plot(x_R_smooth, A_smooth, '-', label='Smooth Data', color='tab:blue')
plt.plot(x_R, slope_left * x_R + intercept_left, '--', label='Left extension', color='tab:red')
plt.plot(x_R, slope_right * x_R + intercept_right, '--', label='Right extension', color='tab:green')
plt.plot(peak_x, peak_y, 'o', label='$b$', color='tab:purple')
plt.plot(peak_x, A_1, 'o', label='$a$', color='tab:orange')

# Adding labels, legend, and grid
plt.xlabel('$x_R$', fontname='Microsoft YaHei', fontsize=14)
plt.ylabel('$A$', fontname='Microsoft YaHei', fontsize=14, style='normal')
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.legend(fontsize=12)
plt.grid(True)

# Adding vertical and horizontal lines for points a and b with annotations
plt.axvline(x=peak_x, color='tab:purple', linestyle='--')
plt.axhline(y=peak_y, color='tab:purple', linestyle='--')
plt.axvline(x=peak_x, color='tab:orange', linestyle='--')
plt.axhline(y=A_1, color='tab:orange', linestyle='--')

# Annotations for x and y values at points a and b
plt.text(peak_x, -0.05, f'{peak_x:.2f}', ha='center', color='tab:purple')
plt.text(1.05, peak_y, f'A2={peak_y:.2f}', va='center', color='tab:purple')
plt.text(peak_x, -0.1, f'{peak_x:.2f}', ha='center', color='tab:orange')
plt.text(1.05, A_1, f'A1={A_1:.2f}', va='center', color='tab:orange')

# Equation display
eq_left = f'y = {slope_left:.2f}x + {intercept_left:.2f}'
eq_right = f'y = {slope_right:.2f}x + {intercept_right:.2f}'
plt.text(0.5, 0.45, eq_left, ha='center', color='tab:red')
plt.text(0.5, 0.40, eq_right, ha='center', color='tab:green')

# Final touches and save figure
plt.tight_layout()
plt.savefig("result.jpg", dpi=300)
plt.show()
