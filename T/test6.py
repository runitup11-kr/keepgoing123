# is_valid = False
# while not is_valid:
#     input_value = int(input("정수 입력: "))
    
#     if input_value > 0:
#         is_valid = True
#     else:
#         print("양의 정수를 입력하세요")
        
        

while True:
    input_value = int(input("정수 입력: "))
    
    #양의 정수인 경우, 반복 종료
    if input_value > 0:
        break
    
    print("양의 정수를 입력하세요")

print("bar")