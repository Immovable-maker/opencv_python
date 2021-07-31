import numpy as np

# Numpy 원소 오름차순 정렬
array = np.array([5, 9, 3, 10, 1])
array.sort()
print(array)

# 행 기준 더 큰 행이 밑으로 오게 만드는 그런
array2 = np.array([[5, 9, 3, 10, 1], [4, 6, 7, 1, 3]])
print(array2)
array2 = np.sort(array2, axis=0)
# array2.sort(axis=0) 우와 이거랑 위에꺼는 똑같음
print(array2)

# 균일한 간격 데이터 생성
array3 = np.linspace(0, 10, 2)
print(array3)

# 난수의 재연 (실행할때마다 결과 때 동일하게 하기)
np.random.seed(1)  # 우와 그냥 숫자마다 다음에 1을 다시 부르면 동일 하게 나오네
print(np.random.randint(0, 10, (2, 4)))

# Numpy 배열 객체 복사 왜냐하면 복사를 안하면 그냥 바꿀때 전에 하던거에도 영향을 미칠 때가 있음, 파이썬은 객체 참조 방식이기때문에 그럼
# 아마 메모리 아이디도 똑같을 거임 새로 부여한게 아니라 같은걸 쳐다보게 만든거임
array4 = np.arange(10)
array5 = array4
print(id(array4), id(array5))
array5[0] = 99
print(array4)

# 중복된 원소 제거
array6 = np.array([1, 1, 1, 3, 4, 5, 66])
array6 = np.unique(array6)
print(array6)
