import cv2
import numpy as np

# Using 'value' pointer is unsafe and deprecated. Use NULL as value pointer. To fetch trackbar value setup callback.
# 무슨 오류인지 잘 모르겠음
def change_color(pos):
    # 변화를 감지하는 것임 그러니까 이 함수안에 cv2.imshow()가 없다면 그냥 트랙바만 있고 r,g,b 변수 값만 바뀌는
    # 프로그램이 되는 거임 x값은 함수 내의 getTrackbarPos 로 전달될 Trackbar의 위치를 의미함
    r = cv2.getTrackbarPos("R", "Image")
    g = cv2.getTrackbarPos("G", "Image")
    b = cv2.getTrackbarPos("B", "Image")
    img[:] = [b, g, r]
    print(r)
    cv2.imshow("Image", img)


img = np.zeros((600, 400, 3), np.int8)
cv2.namedWindow("Image")

cv2.createTrackbar("R", "Image", 0, 255, change_color)
cv2.createTrackbar("G", "Image", 0, 255, change_color)
cv2.createTrackbar("B", "Image", 0, 255, change_color)

cv2.imshow("Image", img)
cv2.waitKey(0)
