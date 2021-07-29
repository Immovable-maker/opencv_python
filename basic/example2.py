import numpy as np

# 기본 연산 중 곱하기 먼저 해보기

array = np.random.randint(0, 10, 4, dtype=int)
print(array)
print(array * 2)

# 서로 다른 형태의 numpy 연산 >>> 행 우선으로 연산하게 됨 >>> broadcasting이라고함 >> 배열의 형태를 동적으로 바꿔주는것
# 없는 쪽을 늘림 오호라 항상 기억해라
array1 = np.arange(4).reshape(2, 2)
array2 = np.arange(2)

# array2 = np.arange(2).reshape(2, 1) 이것도 되긴함

array3 = array1 + array2
print(array3)
print(array3.shape)
print(array3.dtype)
print(array3.size)

# 마스킹 연산
array4 = np.arange(16).reshape(4, 4)
print(array4)
# 10보다 작은거 True 만들기
array5 = array4 < 10
print(array5)
# array 4에서 True 인것들 100으로 만들기
array4[array5] = 100
print(array4)
# 여러 집계함수
array6 = np.arange(16).reshape(4, 4)
print("최소{}", np.min(array6))
print("최대{0}", np.max(array6))
print("합계{0}", np.sum(array6))

# 열에대해서 다더하는것도 가능 걍 니가 생각하는 거 거의다됨 가로로라는거??
print("합계{0}", np.sum(array6, axis=0))


# 내가 만든 array에 대해 파일로 저장할 수 도 있음
array_save = np.arange(16).reshape(4, 4)
array_save2 = np.arange(10)
np.savez('saved_test.npz', array_save, array1= array_save, array2= array_save2)


load_data = np.load("saved_test.npz")
result1 = load_data["array1"]
result2 = load_data["array2"]
print(result1)
print(result2)

