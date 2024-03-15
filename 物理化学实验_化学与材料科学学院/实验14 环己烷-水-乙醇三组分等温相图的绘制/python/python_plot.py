#!/usr/bin/env python
# -*-coding:utf-8 -*-

import os
import numpy as np
import matplotlib.pyplot as plt
import mpltern
os.chdir(os.path.split(os.path.realpath(__file__))[0])
plt.rcParams['font.sans-serif'] = ['Microsoft Yahei']

# Data points for the ternary plot
data_points = np.array([
    [0.4028, 0.0259, 0.5714],
    [0.3181, 0.0695, 0.6124],
    [0.2557, 0.0887, 0.6556],
    [0.2169, 0.1170, 0.6660],
    [0.1666, 0.1541, 0.6794],
    [0.1386, 0.1906, 0.6708],
    [0.1053, 0.2461, 0.6486],
    [0.0770, 0.3117, 0.6112],
    [0.0531, 0.3684, 0.5785],
    [0.0385, 0.3966, 0.5649]
])

# Creating subplot with ternary projection
ax = plt.subplot(projection="ternary")
# Plotting the data points and the fitted curve
ax.scatter(data_points[:, 2], data_points[:, 0], data_points[:, 1], color='tab:blue', label='Data Points')
data_points_2 = np.vstack(([1, 0, 0], data_points, [0, 1, 0]))
ax.plot(data_points_2[:, 2], data_points_2[:, 0], data_points_2[:, 1], color='tab:orange', label='Parabola-like Curve')

# Total composition point O and E normalized to fraction
O = np.array([0.3033, 0.3895, 0.3072])
E = np.array([50.12, 49.88, 0]) / (50.12 + 49.88)
# Plotting points O and E
ax.scatter(*O, color='tab:green', label='O (Total composition)')
ax.scatter(*E, color='tab:purple', label='E')
# Annotating points E and O with their labels and coordinates
ax.text(O[2], O[0]+0.05, f'O {O}', horizontalalignment='left', verticalalignment='center', transform=ax.transAxes, color='tab:green')
ax.text(E[2]+0.45, E[0]+0.05, f'E {E}', horizontalalignment='right', verticalalignment='center', transform=ax.transAxes, color='tab:purple')
# ax.set_title('请同学们自行画出HG连接线！',color='tab:red')

# Label settings
ax.set_tlabel("C(乙醇)")
ax.set_llabel("A(环己烷)")
ax.set_rlabel("B(水)")
ax.grid(True)

# Finalizing and saving the figure
plt.tight_layout()
# plt.legend()
plt.savefig("result.jpg", dpi=300)
plt.show()
