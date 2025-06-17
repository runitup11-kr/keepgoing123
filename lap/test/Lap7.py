


def contains(arg_list,arg_target):
    
    for i in arg_list: # 리스트 안에 원소를 하나씩 확인
        if i == arg_target: # 만약 내가 찾는 원소와 같다면??
            return True # 사실
    return False # 아니면 거짓
    
    

print(contains([1,2,3,4],3))
print(contains([1,2,3,4],8))