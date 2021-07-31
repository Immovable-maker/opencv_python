import cv2
import numpy as np
import matplotlib.pyplot as plt

# line, rectangel, circle, polylines, putText 도 있음
img = np.full((512, 512, 3), 255, np.uint8)
img1 = cv2.line(img, pt1=(0, 0), pt2=(255, 255), color=(255, 0, 0), thickness=3)
img2 = cv2.rectangle(img, pt1=(300, 300), pt2=(450, 450), color=(255, 0, 0), thickness=-1)
img3 = cv2.circle(img, (255, 255), radius=30, color=(255, 0, 0), thickness=3)
points_polyline = np.array([[5, 5], [138, 250], [483, 444], [400, 150]])
img4 = cv2.polylines(img, [points_polyline], True, (0, 0, 255), thickness=4)  # 꼭짓점들(리스트 안에 리스트?), 닫혀있냐 여부,
# 텍스트도 넣을 수 있음
plt.imshow(img1 + img2 + img3 + img4)  # saturation이나 modulo 계산이 필요없을때는 걍 이렇게 해도 상관 없을 듯
plt.show()
