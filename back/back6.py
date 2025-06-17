a , b = map(int,input("시간 입력: ").split())

c = int(input("요리 시간: "))


if b + c < 60:
    print(a , b + c)
elif b + c >= 60: 
    if a +((b+c)//60) >= 24: 
        print(a +((b+c)//60)-24,(b+c)% 60) 
    elif a +((b+c)//60) < 24:
        print(a +((b+c)//60),(b+c)% 60)