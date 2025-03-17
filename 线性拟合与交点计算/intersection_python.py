import numpy as np
import matplotlib.pyplot as plt
import os
os.chdir(os.path.split(os.path.realpath(__file__))[0])
plt.rcParams['font.sans-serif'] = ['LXGW ZhenKai']

# 数据
x1 = np.array([0.002, 0.0024, 0.0036, 0.005, 0.0062, 0.0071])
y1 = np.array([159.3, 181.4, 271, 361, 426, 475])

x2 = np.array([0.01, 0.0114, 0.0126, 0.0136, 0.0146])
y2 = np.array([588, 638, 698, 734, 773])

# 线性拟合
coef1 = np.polyfit(x1, y1, 1)
coef2 = np.polyfit(x2, y2, 1)

# 直线方程
f1 = np.poly1d(coef1)
f2 = np.poly1d(coef2)

# 计算交点
A = np.array([[coef1[0], -1], [coef2[0], -1]])
b = np.array([-coef1[1], -coef2[1]])
intersect_x, intersect_y = np.linalg.solve(A, b)

# 生成拟合曲线数据
x_fit = np.linspace(min(x1.min(), x2.min()), max(x1.max(), x2.max()), 100)
y_fit1 = f1(x_fit)
y_fit2 = f2(x_fit)

# 绘图
plt.figure(figsize=(6, 4), dpi=300)
plt.title('线性拟合交点计算')
plt.plot(x1, y1, 'o', label='Data 1', color='tab:blue')
plt.plot(x2, y2, 'o', label='Data 2', color='tab:orange')
plt.plot(x_fit, y_fit1, '-', label=f'Fit 1: y={coef1[0]:.2f}x+{coef1[1]:.2f}', color='tab:blue')
plt.plot(x_fit, y_fit2, '-', label=f'Fit 2: y={coef2[0]:.2f}x+{coef2[1]:.2f}', color='tab:orange')
plt.scatter(intersect_x, intersect_y, color='red', zorder=3, label=f'Intersection ({intersect_x:.4f}, {intersect_y:.1f})')

# 轴标签与图例
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)
plt.tight_layout()

# 保存图像
plt.savefig('intersection_python_plot.jpg', dpi=300)
plt.show()

# 输出交点坐标
(intersect_x, intersect_y)


