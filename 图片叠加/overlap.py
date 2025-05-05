import os
import cv2

# 设置工作目录为当前脚本所在目录
os.chdir(os.path.dirname(os.path.abspath(__file__)))
print('copyright by Zhaosheng Zhang (misaraty@163.com)\nlast update: 2022-06-25')

# 混合权重
x1 = 0.9
x2 = 1 - x1

# 要叠加的图像列表（从最新到最旧）
image_files = [
    '20220625.jpg',
    '20220624.jpg',
    '20220622.jpg',
    '20220620.jpg',
    '20220617.jpg',
    '20220616.jpg',
]

# 初始化融合图像
final_img = None

for img_file in image_files:
    if not os.path.exists(img_file):
        print(f"[警告] 找不到文件：{img_file}")
        continue

    img = cv2.imread(img_file)
    if img is None:
        print(f"[错误] 无法读取图像：{img_file}")
        continue

    if final_img is None:
        final_img = img.copy()
    else:
        final_img = cv2.addWeighted(final_img, x1, img, x2, 0)

# 保存最终融合图像
if final_img is not None:
    cv2.imwrite('final.jpg', final_img)
    print('已保存最终融合图像：final.jpg')
else:
    print('未生成任何融合图像。')
