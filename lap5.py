
bar = [10, 20, 30]

def foo(arg_list):
    arg_list[0] = 100 # 리스트는 가변형 -> 원본 자체 수정 가능 참조 변수
    
foo(bar)

print(bar)

kin = 3 # 얘는 불변 객체 지역 변수만 바뀌고 원본은 그대로 
def pos(arg):
    arg = 10

pos(kin)
print(kin)