% 数据
data = [
    2.28, 2.57322;
    4.07, 2.55218;
    6.68, 2.3263;
    8.82, 2.0661;
    10.82, 1.891;
    12.82, 1.74641;
    14.82, 1.59127;
    17.08, 1.41342;
    19.06, 1.2596;
    22.05, 1.02461;
    25.06, 0.78116;
    28.03, 0.53708;
    31.1, 0.28141;
    34.05, 0.01292;
    37.05, -0.27181;
    40.2, -0.57982;
];

% 提取x和y
x = data(:, 1);
y = data(:, 2);

% 使用MATLAB的polyfit进行线性拟合
coefs = polyfit(x, y, 1);
fit_values = polyval(coefs, x);

% 绘图
figure;
scatter(x, y, 'blue', 'DisplayName', 'Data Points');
hold on;
plot(x, fit_values, 'red', 'DisplayName', sprintf('Fit: y = %.4fx + %.4f', coefs(1), coefs(2)));
xlabel('t/min');
ylabel('ln(\alpha-\alpha_{\infty})/°');
legend;
grid on;

% 保存为300dpi的图像
print('C:\Users\lenovo\Desktop\pic2.jpg','-djpeg','-r300');
