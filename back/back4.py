

x = int(input("숫자 입력: "))
y = int(input("숫자 입력: "))


if x > 0 and y > 0:
    print("1")
elif x < 0 and y > 0:
    print("2")
elif x < 0 and y < 0 :
    print("3")
else:
    print("4")