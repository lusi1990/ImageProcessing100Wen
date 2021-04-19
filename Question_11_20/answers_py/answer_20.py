import cv2
import numpy as np
import matplotlib.pyplot as plt

# Read image
img = cv2.imread("imori.jpg").astype(np.float)
img.ravel()
# Display histogram
plt.hist(img.ravel(), bins=255,  range=(0, 255))
# plt.savefig("out.png")
plt.show()
