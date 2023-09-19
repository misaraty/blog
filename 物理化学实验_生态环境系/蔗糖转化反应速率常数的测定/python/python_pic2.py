import numpy as np
import matplotlib.pyplot as plt

# 数据
data = """
2.28    2.57322
4.07    2.55218
6.68    2.3263
8.82    2.0661
10.82   1.891
12.82   1.74641
14.82   1.59127
17.08   1.41342
19.06   1.2596
22.05   1.02461
25.06   0.78116
28.03   0.53708
31.1    0.28141
34.05   0.01292
37.05   -0.27181
40.2    -0.57982
"""

# 解析数据
lines = data.strip().split("\n")
x, y = zip(*[map(float, line.split()) for line in lines])

# 使用numpy进行线性拟合
coefs = np.polyfit(x, y, 1)
fit_func = np.poly1d(coefs)

# 绘图
plt.scatter(x, y, color='tab:blue', label='Data Points')
plt.plot(x, fit_func(x), color='tab:red', label=f'Fit: y = {coefs[0]:.4f}x + {coefs[1]:.4f}')
plt.xlabel('t/min')
plt.ylabel(r'ln($\alpha$-$\alpha_{\infty}$)/°')
plt.legend()
plt.grid(True)

# 保存为300dpi的图像
plt.tight_layout()
plt.savefig("C:\\Users\\lenovo\\Desktop\\pic2.jpg", dpi=300)

# 显示图形
plt.show()
