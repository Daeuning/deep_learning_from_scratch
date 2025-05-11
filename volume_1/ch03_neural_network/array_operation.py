import numpy as np

# 1차원 배열
A = np.array([1, 2, 3, 4])
print(A)
print(np.ndim(A)) # 배열의 차원을 계산 -> 1
print(A.shape) # 배열의 형상을 계산, 항상 튜플로 반환한다 -> (4,)

# 2차원 배열
B = np.array([[1, 2], [3, 4], [5, 6]])
print(B)
print(np.ndim(B)) # 2
print(B.shape) # (3,2)