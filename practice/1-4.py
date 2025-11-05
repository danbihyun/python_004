import numpy as np

scores = np.array([85, 92, 78, 90, 88, 76, 95, 89])

total = np.sum(scores)   # 합계
avg = np.mean(scores)    # 평균
std = np.std(scores)     # 표준편차

print(f"평균:", avg)
print(f"\n최고점:",np.max(scores))
print(f"\n최저점:", np.min(scores))
print(f"\n표준편차:", std)
print(f"\n총점:", total)