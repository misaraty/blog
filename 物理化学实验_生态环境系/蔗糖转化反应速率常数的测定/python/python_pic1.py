import matplotlib.pyplot as plt

# 数据
data = """
2.28    9.684
4.07    9.411
6.68    6.816
8.82    4.47
10.82   3.202
12.82   2.31
14.82   1.486
17.08   0.686
19.06   0.1
22.05   -0.638
25.06   -1.24
28.03   -1.713
31.1    -2.099
34.05   -2.411
37.05   -2.662
40.2    -2.864
45.03   -3.107
50.05   -3.278
55.02   -3.391
"""

# 解析数据
lines = data.strip().split("\n")
x, y = zip(*[map(float, line.split()) for line in lines])

# 绘图
plt.scatter(x, y, color='tab:blue', label='Data Points')
plt.xlabel('t/min')
plt.ylabel(r'$\alpha$' + '/°')
plt.legend()
plt.grid(True)

# 保存为300dpi的图像
plt.tight_layout()
plt.savefig("C:\\Users\\lenovo\\Desktop\\pic1.jpg", dpi=300)

# 显示图形
plt.show()
