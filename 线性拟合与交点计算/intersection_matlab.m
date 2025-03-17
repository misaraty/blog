% 数据
x1 = [0.002, 0.0024, 0.0036, 0.005, 0.0062, 0.0071];
y1 = [159.3, 181.4, 271, 361, 426, 475];

x2 = [0.01, 0.0114, 0.0126, 0.0136, 0.0146];
y2 = [588, 638, 698, 734, 773];

% 线性拟合
p1 = polyfit(x1, y1, 1);
p2 = polyfit(x2, y2, 1);

% 直线方程
f1 = @(x) p1(1)*x + p1(2);
f2 = @(x) p2(1)*x + p2(2);

% 计算交点
A = [p1(1), -1; p2(1), -1];
b = [-p1(2); -p2(2)];
intersect = A\b;

intersect_x = intersect(1);
intersect_y = intersect(2);

% 生成拟合曲线数据
x_fit = linspace(min([x1, x2]), max([x1, x2]), 100);
y_fit1 = f1(x_fit);
y_fit2 = f2(x_fit);

% 颜色设定（与 Python tab 颜色相似）
color1 = [0.1216, 0.4667, 0.7059];  % tab:blue
color2 = [1.0000, 0.4980, 0.0549];  % tab:orange
intersect_color = [0.8353, 0.0588, 0.1569]; % red

% 绘图
figure('Position', [100, 100, 800, 600], 'Color', 'w'); % 增大图片尺寸
hold on;
plot(x1, y1, 'o', 'MarkerSize', 8, 'DisplayName', 'Data 1', 'Color', color1, 'LineWidth', 1.5);
plot(x2, y2, 'o', 'MarkerSize', 8, 'DisplayName', 'Data 2', 'Color', color2, 'LineWidth', 1.5);
plot(x_fit, y_fit1, '-', 'DisplayName', sprintf('Fit 1: y=%.2fx+%.2f', p1(1), p1(2)), 'Color', color1, 'LineWidth', 2);
plot(x_fit, y_fit2, '-', 'DisplayName', sprintf('Fit 2: y=%.2fx+%.2f', p2(1), p2(2)), 'Color', color2, 'LineWidth', 2);
scatter(intersect_x, intersect_y, 100, 'filled', 'MarkerFaceColor', intersect_color, 'DisplayName', ...
    sprintf('Intersection (%.4f, %.1f)', intersect_x, intersect_y));

% 轴标签与图例
xlabel('x', 'FontName', 'LXGW ZhenKai', 'FontSize', 16, 'FontWeight', 'bold');
ylabel('y', 'FontName', 'LXGW ZhenKai', 'FontSize', 16, 'FontWeight', 'bold');
title('线性拟合交点计算', 'FontName', 'LXGW ZhenKai', 'FontSize', 18, 'FontWeight', 'bold');
legend('show', 'FontName', 'LXGW ZhenKai', 'FontSize', 14);
grid on;

% 自动调整布局
set(gca, 'FontName', 'LXGW ZhenKai', 'FontSize', 14, 'LineWidth', 1.2);
set(gca, 'Box', 'on');

% 获取当前脚本所在目录
script_path = fileparts(mfilename('fullpath'));
save_path = fullfile(script_path, 'intersection_matlab_plot.jpg');

% 保存图像
print(gcf, save_path, '-djpeg', '-r300');  % 300dpi JPG
disp(['图像已保存至: ', save_path]);
