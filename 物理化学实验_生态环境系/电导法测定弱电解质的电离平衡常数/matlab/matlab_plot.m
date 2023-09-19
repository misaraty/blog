% 数据
data = [
    9.676E-6, 415.87433;
    1.497E-5, 672.01069;
    2.05E-5, 981.46341;
    2.48E-5, 1216.93548;
    2.85E-5, 1410.87719;
    3.42E-5, 1470.76023
];

x = data(:, 1);
y = data(:, 2);

% 拟合数据
fit_result = polyfit(x, y, 1);
fit_x = linspace(min(x), max(x), 100);  % 为拟合线生成x值
fit_y = polyval(fit_result, fit_x);

% 绘图
figure;
scatter(x, y, 'b', 'DisplayName', 'Data Points');
hold on;
plot(fit_x, fit_y, 'r', 'DisplayName', sprintf('Fit: y = %.4fx + %.4f', fit_result(1), fit_result(2)));
xlabel('c \times \Lambda_m / c^\o');
ylabel('1/\Lambda_m');
legend();
grid on;

% 保存到本地
filename = 'C:\Users\lenovo\Desktop\result.jpg';
print(gcf, '-djpeg', sprintf('-r%d', 300), filename);

