year = int(input("년도 입력: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("1")
else:
    print("0")