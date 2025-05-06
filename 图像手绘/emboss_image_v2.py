import cv2
import numpy as np
import os
os.chdir(os.path.split(os.path.realpath(__file__))[0])

def emboss_image_cv(img_path, save_path, depth=10):
    gray = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE).astype('float')
    grad_y, grad_x = np.gradient(gray)
    grad_x *= depth / 100.
    grad_y *= depth / 100.
    A = np.sqrt(grad_x**2 + grad_y**2 + 1)
    uni_x, uni_y, uni_z = grad_x / A, grad_y / A, 1. / A

    dx, dy, dz = np.cos(np.pi / 2.2) * np.cos(np.pi / 4), \
                 np.cos(np.pi / 2.2) * np.sin(np.pi / 4), \
                 np.sin(np.pi / 2.2)

    b = 255 * (dx * uni_x + dy * uni_y + dz * uni_z)
    b = np.clip(b, 0, 255).astype('uint8')
    cv2.imwrite(save_path, b)

if __name__ == '__main__':
    for file in os.listdir('./pic'):
        if file.lower().endswith(('.jpg', '.png')):
            emboss_image_cv(f'./pic/{file}', f'./pic/{file.split(".")[0]}_cv.jpg')
