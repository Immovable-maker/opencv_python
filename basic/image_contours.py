# 이미지에서 컨투어 찾으려면 mode정해주어야 하고
# 입력이미지는 grayscale threshold로 이미지 전처리 필요

import cv2
import matplotlib.pyplot as plt

img = cv2.imread("hand_writing.jpg")
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # flag 지금 이상함
ret_max, img_thres = cv2.threshold(img_gray, 127, 255, 0)

plt.imshow(img)
plt.show()
