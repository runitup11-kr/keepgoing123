# 함수 정의
# - > 자기만의 함수를 만들고 싶을때
def bar():
    print("hello")


bar()


def get_input_num():
    msg = "정수 입력: "
    input_value = int(input(msg))
    
    if input_value < 0:
        print("0과 양의 정수만 입력하세요")
        return
    
    return input_value

#value = get_input_num()
#print(value,type(value))