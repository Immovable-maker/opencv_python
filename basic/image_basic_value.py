import cv2

img = cv2.imread("cat.jpg", cv2.IMREAD_COLOR)  # Numpy 객체로 만드는 함수
# imshow, imwrite(이미지를 파일로 저장), waitKey(키보드 입력을 처리하는 함수 0넣으면무한대기 키입력하면 ascii 반환)
# destoryAllWidows 창 닫기
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 아래 방법 개느림
# for i in range(100):
#     for j in range(100):
#         img[i, j] = [0, 0, 0]

# 슬라이싱 방법이 훠어어얼씬 빠름, ROI도 나름대로 잘라서 활용은 가능 (슬라이싱)
img[:100, :100] = [0, 0, 0]
# 색깔 원하는거 없애보자 블루 삭제
img[:, :, 0] = 0
# 그린 삭제
img[:, :, 1] = 0

cv2.imshow("cat", img)
cv2.waitKey(0)
print(cv2.waitKey(0))
cv2.destroyAllWindows()

# 아무 키나 눌렀을때 누르기 전 등장한 컬러 이미지에 대한 정보들 나오게!
print(img[0, 0])  # x, y 축에서의 값
print(img.shape)
print(img.dtype)
print(img.size)

cv2.imshow("ir2", img_gray)
cv2.waitKey(0)
print(cv2.waitKey(0))
cv2.destroyAllWindows()
