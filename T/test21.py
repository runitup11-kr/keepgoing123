bar = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
del bar[3]
print(bar)

bar.pop()
print(bar)

bar.remove(8)
print(bar)

bar.remove(10)







bar = [10, 20, 30, 40, 50]

try:
    bar.remove(50)
except Exception:
    print("찾는 값이 없습니다.")