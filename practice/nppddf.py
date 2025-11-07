import numpy as np
import pandas as pd

students = pd.DataFrame({
    "name" : np.random.choice(["Kim", "Park", "Lee", "Na", "Jung", "Seo"], 101),
    "age" : np.random.randint(20, 65, 101),
    "city" : np.random.choice(["Seoul", "Jeju", "Daegu", "Gwangju", "Busan", "Ulsan", "Incheon", "Daejeon"], 101),
    "score" : np.random.randint(1, 21, 101) * 5,
})

# CSV로 저장
students.to_csv('students.csv', index=False, encoding='utf-8-sig')
print("저장 완료!")

# 다시 읽기
loaded = pd.read_csv('students.csv', encoding='utf-8-sig')
print("\n읽어온 데이터:\n", loaded)