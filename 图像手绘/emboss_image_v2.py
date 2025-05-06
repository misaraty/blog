import cv2
import numpy as np
import os
os.chdir(os.path.split(os.path.realpath(__file__))[0])

def emboss_image_cv(img_path, save_path, depth=10):
    """
    对输入图像进行浮雕效果处理并保存
    参数:
        img_path: 输入图像路径
        save_path: 处理后图像的保存路径
        depth: 浮雕深度参数（数值越大，立体感越强）
    """
    # 读取图像并转换为灰度图像，转为 float 类型便于后续计算
    gray = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE).astype('float')

    # 计算图像的梯度，得到水平和垂直方向的变化率
    grad_y, grad_x = np.gradient(gray)

    # 调整梯度值的强度以控制浮雕深度
    grad_x *= depth / 100.
    grad_y *= depth / 100.

    # 计算单位法向量分量（x, y, z）
    A = np.sqrt(grad_x**2 + grad_y**2 + 1)
    uni_x, uni_y, uni_z = grad_x / A, grad_y / A, 1. / A

    # 设置光照方向：俯视角（elevation）和方位角（azimuth），单位为弧度
    dx = np.cos(np.pi / 2.2) * np.cos(np.pi / 4)  # x方向光照强度
    dy = np.cos(np.pi / 2.2) * np.sin(np.pi / 4)  # y方向光照强度
    dz = np.sin(np.pi / 2.2)                     # z方向光照强度

    # 根据法向量与光照方向的点积计算光照强度（浮雕效果图）
    b = 255 * (dx * uni_x + dy * uni_y + dz * uni_z)

    # 将结果限制在 [0, 255] 范围内，并转换为 uint8 类型以便保存为图像
    b = np.clip(b, 0, 255).astype('uint8')

    # 保存浮雕处理后的图像
    cv2.imwrite(save_path, b)

if __name__ == '__main__':
    # 遍历 './pic' 目录下的图像文件，对 .jpg 和 .png 格式文件应用浮雕效果
    for file in os.listdir('./pic'):
        if file.lower().endswith(('.jpg', '.png')):
            input_path = f'./pic/{file}'
            output_path = f'./pic/{file.split(".")[0]}_cv.jpg'
            emboss_image_cv(input_path, output_path)
