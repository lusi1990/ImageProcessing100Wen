"""
todo install,基础操作 等
OpenCV is BGR, Pillow is RGB

When reading a color image file, OpenCV imread() reads as a NumPy array ndarray of row (height) x column (width) x color (3).
The order of color is BGR (blue, green, red).
"""

import cv2
import numpy as np

# function: BGR -> RGB
from PIL import Image


def BGR2RGB(img):
    b = img[:, :, 0].copy()
    g = img[:, :, 1].copy()
    r = img[:, :, 2].copy()

    # RGB > BGR
    img[:, :, 0] = r
    img[:, :, 1] = g
    img[:, :, 2] = b

    return img


# Read image
img = cv2.imread("../imori.jpg")

im_pillow = np.array(Image.open('data/src/lena.jpg'))

# BGR -> RGB
img_rgb = BGR2RGB(img)
print('use BGR2RGB')
cv2.imshow("BGR2RGB", img_rgb)
cv2.waitKey(0)

print('use opencv')
img = cv2.imread("../imori.jpg")
im_rgb2 = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
cv2.imshow("result", im_rgb2)
cv2.waitKey(0)
cv2.destroyAllWindows()
