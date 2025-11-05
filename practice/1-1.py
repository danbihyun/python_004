import numpy as np

arr1 = np.arange(1, 21)
print(f"1 ~ 20까지의 배열\n", arr1)

arr2 = np.zeros((3, 4))
print(f"\n0으로 채워진 3 x 4 배열\n", arr2)

arr3 = np.ones((5, 5))
print(f"\n1로 채워진 5 x 5 배열\n", arr3)

arr4 = np.full((2, 3), 10)
print(f"\n10으로 채워진 2 x 3 배열\n", arr4)