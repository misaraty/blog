using Printf
using Plots
using LsqFit
using LaTeXStrings

# 数据
data = [
    9.676E-6  415.87433;
    1.497E-5  672.01069;
    2.05E-5   981.46341;
    2.48E-5  1216.93548;
    2.85E-5  1410.87719;
    3.42E-5  1470.76023
]

x = data[:, 1]
y = data[:, 2]

# 定义拟合模型
@. model(x, p) = p[1] * x + p[2]

# 初始参数猜测
p0 = [1.0, 1.0]

# 使用最小二乘法拟合数据
fit = curve_fit(model, x, y, p0)

# 获取拟合参数
coefs = fit.param

# 格式化拟合参数为字符串
coefs_str = string(@sprintf("%.4f", coefs[1]), "x + ", @sprintf("%.4f", coefs[2]))

# 绘图
scatter(x, y, color=:blue, label="Data Points", grid=true)
plot!(x, model(x, coefs), color=:red, label="Fit: y = $coefs_str", grid=true)
xlabel!(L"c \times \frac{\Lambda_m}{c^{\ominus}}")
ylabel!(L"\frac{1}{\Lambda_m}")

# 保存到本地
savefig("C:\\Users\\lenovo\\Desktop\\result.png")

# 显示图形
display(current())

