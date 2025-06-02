
import random #랜덤 숫자를 사용하기위한 변수


number = random.randint(1, 100) # 1부터 100 사이의 숫자를 임의로 선정

count = 10 # 시도 할 횟수

while count <= 10:
    count1 = int(input("1부터 100까지의 숫자를 맞춰 보세요!: "))
    count -= 1
    if count > number:
        print("더 작은 숫자입니다")
    elif count < number:
        print("더 큰 숫자입니다")
    else:
        print("정답")
        
    if count == 0:
        print(f"모든 기회를 사용하였습니다. 정답은 {number}입니다")
    else:
        print(f"정답이 아닙니다! 남은 기회 {count}")
    

    
        
            
        