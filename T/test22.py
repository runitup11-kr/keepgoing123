

import random
import math

n = int(input("\n리스트 개수 입력(5 - 20): "))

if n < 5 or n> 20:
    print("오류")
else:
    data = [random.randint(1,100) for _ in range(n)]
    
    # 평균
    total = 0
    for val in data:
        total += val
    mean = total / n
    # 편차
    deviations = []
    for val in data:
        deviations.append(val - mean)
        
    # 분산
    variance = 0
    for d in deviations:
        variancer += d**2
    variance /= n
    
    # 표준편차
    std_dev = math.sqrt(variance)
    
    #출력
    print("\n 생성된 리스트:",data)
    