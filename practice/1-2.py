import numpy as np

arr = np.array([[1, 2, 3, 4],
                [5, 6, 7, 8],
                [9, 10, 11, 12]])


print(f"\n첫 번째 행\n", arr[0])

print(f"\n마지막 열\n", arr[:, -1])

print(f"\n값 7 출력\n", arr[1, 2])

print(f"\n2행 2열부터 3행 3열까지 출력\n", arr[1:, 1:-1])