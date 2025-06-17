H, M = map(int,input("시간 입력: ").split())

M1 = M - 45

if M1 < 0:
    H = M - 1
    M1 = M1 + 60
    if H < 0:
        H = H + 24

print(H , M1)