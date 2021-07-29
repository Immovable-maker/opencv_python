# 이미지 늘리거나 줄일때 생각해봐 그 이미지를 어떻게 늘리겠어 사이 픽셀값에서 그 색깔이나 그런것들은 추정을 해줘야겠지
# 그 방식이 interpolation이야 수치해석 때 배우는 cubic(삼차함수로 맞추는거) area, linear, Bilinear등 방법은 많아

import cv2
import matplotlib as plt
# resize,

img = cv2.imread("ir.jpg", cv2.IMREAD_COLOR)
plt.imshow("ir", img, cv2.COLOR_BGR2RGB)