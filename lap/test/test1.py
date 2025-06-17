print("정수 10개를 입력하세요: ")

num = []
for i in range(1, 11):
    num.append(input(f"{i}번째 정수: "))
print(f"[원본 리스트]{num}\n")
print(f"1. 처음 5개 원소:{num[:5]}\n")
print(f"2. 뒤에서 3개 원소:{num[-3:]}")
print(f"3. 짝수 인덱스 원소:{num[::2]}")
print(f"4. 거꾸로 뒤집은 리스트:{num[::-1]}")