import random



number = random.randint(1, 100)


while True:
    count = int(input("1부터 100사이의 숫자를 맞춰 보세요: "))
    if count > number:
        print("더 작은 숫자입니다")
    elif count < number:
        print("더 큰 숫자입니다 ")
    else:
        print("정답!")
        break
    