import numpy as np

arr1 = np.array([1, 2, 3, 4, 5])
arr2 = np.array([10, 20, 30, 40, 50])

print(f"두 배열의 합\n", arr1 + arr2)
print(f"\n두 배열의 곱\n", arr1 * arr2)
print(f"\narr1의 각 요소에 10을 더하기\n", arr1 + 10)
print(f"\narr2의 각 요소를 2로 나누기\n", arr2 / 2)