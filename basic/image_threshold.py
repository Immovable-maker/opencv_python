# threshold 허용치 임계값 넘으면 어떤거 할 지 type을 정할수 있음
# 어떤 threshold 값 기준으로 그것보다 크면 max_value(우리가 설정하는값), 작으면 0
# thresh 값 max_value값 과 type을 정해서 그게 나오게 할지 아닐지 저 세값 또는 현재 픽셀값을 나오게 하는 여러가지 type존재

import cv2
import matplotlib.pyplot as plt

img = cv2.imread("cat.jpg", cv2.COLOR_BGR2GRAY)
print(img.shape)
images = []
# 1,2 번이 그레이스케일로 값을 받았으니 색깔이 하나밖에 안나오지 type은 후에 검색하든지 할것

# 임계보다 크면 max_val, 나머지는 0
threshold_used, thres_type_BIN = cv2.threshold(img, 127, 0, cv2.THRESH_BINARY)
# 크면 0 나머지는 max_val
maybe_same, thres_type_BIN_INV = cv2.threshold(img, 127, 0, cv2.THRESH_BINARY_INV)
# 크면 threshold값, 나머지는 그대로
_, thres_type_TRUNC = cv2.threshold(img, 127, 0, cv2.THRESH_TRUNC)
# 크면 그대로 나머지는 0
_, thres_type_TOZERO = cv2.threshold(img, 127, 0, cv2.THRESH_TOZERO)
# 크면 0 나머지는 그대로
_, thres_type_TOZERO_INV = cv2.threshold(img, 127, 0, cv2.THRESH_TOZERO_INV)
# Otsu 알고리즘이나 triangle 알고리즘도 존재
print(threshold_used)
print(maybe_same)

images.append(thres_type_BIN)
images.append(thres_type_BIN_INV)
images.append(thres_type_TRUNC)
images.append(thres_type_TOZERO)
images.append(thres_type_TOZERO_INV)

for image in images:
    plt.imshow(image)
    plt.show()

'''adaptive한 임계점 이것도 max_value, type이 존재할 것임'''
# MEAN 한 임계점은 전체 픽셀 의 평균값을 threshold로
# GAUSSIAN 141 474 141 의 필터를 입혀서 필터링한 값을 threshold로 하는 것이 그것
img1 = cv2.imread("hand_writing.jpg", cv2.COLOR_BGR2GRAY)

threshold_used1, img_thres_BIN = cv2.threshold(img1, 127, 255, cv2.THRESH_BINARY)
# 맨 뒤 두개 파라미터는 block size(그 커널 가로세로 크기) , C는 가중 평균값에서 뺼값
img_adap_thres_GAUSSIAN = cv2.adaptiveThreshold(img1, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 21, 3)

cv2.imshow("test", cv2.resize(img1, None, fy=0.15, fx=0.2, interpolation=cv2.INTER_AREA))

# 여기 밑에서 왜 GRAYSCALE인데 cvtColor를 해줘야만 grayscale로 나오는지 잘 모르겠음
plt.imshow(img)
plt.show()

plt.imshow(img_thres_BIN)
plt.show()

plt.imshow(img_adap_thres_GAUSSIAN)
plt.show()
