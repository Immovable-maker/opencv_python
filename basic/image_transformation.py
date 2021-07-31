# 이미지 늘리거나 줄일때 생각해봐 그 이미지를 어떻게 늘리겠어 사이 픽셀값에서 그 색깔이나 그런것들은 추정을 해줘야겠지
# 그 방식이 interpolation이야 수치해석 때 배우는 cubic(삼차함수로 맞추는거) area, linear, Bilinear등 방법은 많아

import cv2
import numpy as np
import matplotlib.pyplot as plt

# resize 스케일과 이미지 interpolation 방법만 넣어주면 됨
img = cv2.imread("cat.jpg", cv2.IMREAD_COLOR)
plt.imshow(img)
plt.show()
# expand 주로 cubic(3차식 복원) 방법을 사용함
expand_img = cv2.resize(img, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)
plt.imshow(cv2.cvtColor(expand_img, cv2.COLOR_BGR2RGB))
plt.show()
# shrink 주로 area interpolation 방법을 사용함
shrink_img = cv2.resize(img, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)
plt.imshow(cv2.cvtColor(shrink_img, cv2.COLOR_BGR2RGB))
plt.show()

# warpaffine (위치, 회전 등등 존재) 간단한 변환 행렬 M 예시로 해보자

height, width = img.shape[:2]  # 후에도 굉장히 많이 쓸것, 순서도 조심 height는 행개수
Matrix_move = np.float32([[1, 0, 50], [0, 1, 100]])
img2 = cv2.warpAffine(img, Matrix_move, (width, height))
plt.imshow(img2)
plt.show()

# getRotationMatrix2D notion에 적어놓은 회전 행렬 식을 알아서 만들어줌
# 그 대신 중심, 각도,scale이 param으로 필요하겠지

Matrix_rotate = cv2.getRotationMatrix2D((0, 0), 30, 1)
img3 = cv2.warpAffine(img, Matrix_rotate, (width, height))
plt.imshow(cv2.cvtColor(img3, cv2.COLOR_BGR2RGB))
plt.show()
