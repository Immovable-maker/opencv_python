import numpy as np

# 0부터 3까지의 배열 만들기
array1 = np.arange(4)
print(array1)

array2 = np.zeros(shape=(4, 4), dtype=float)
print(array2)

array3 = np.ones(shape=(4, 4), dtype=str)
print(array3)

# 랜덤
array4 = np.random.randint(0, 10, (3, 3))
print(array4)

# 표준 정규 분포
array5 = np.random.normal(0, 1, (3, 3))
print(array5)

# array 합성 (차원이 다르면 안되지 밑의 코드는 못써
# array6 = np.concatenate([array1, array2])

# 1행짜리 다른 shape으로 만들기
array7 = array1.reshape((2, 2))
print(array7)

array8 = np.arange(4).reshape(1, 4)
print(array8)

array9 = np.arange(8).reshape(2, 4)
print(array9)

# 행을의미함 axis 0은, 행을 기준으로 더함
array10 = np.concatenate([array8, array9], axis=0)

# 열을 의미하고 한마디로 세로로 자른다는뜻 2,2 와 2,2 행렬로 나오겠지
left, right = np.split(array9, [2], axis=1)
print(left)
print(right)  # shape는 2,2 로 나오겠지
