import cv2
import numpy as np
import matplotlib.pyplot as plt

# cv2.add Saturation 연산 0보다 작으면 0 255보다 크면 255로 표현
# np.add는 Modulo 연산을 수행하고 256은 0 257은 1로 표현 확인하려면 np 같은거 좀 봐야될듯
img1 = cv2.imread("fresh.jpg")  # matplotlib에서는 RGB로 값을 받아야해서
img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)
img1 = img1[:5184, :3456, :]

img2 = cv2.imread("cat.jpg")
img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)

print(img1.shape)
print(img1.dtype)

print(img2.shape)
print(img2.dtype)

result = cv2.add(img1, img2)
plt.imshow(result)
plt.show()

result2 = np.add(img1, img2)
plt.imshow(result2)
plt.show()