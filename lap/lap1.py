
bar = {"std1" : 10, "std2": 20, "std3": 30}



#print(bar.pop("std4",False))
#print(bar)



#keys = bar.keys()

#if "std1" in keys:
#    print("True")
#else:
 #   print("false")
 
#for key, item in bar.items():
#    print(f"key: {key}, Item: {item}") 키 값 아이템 값 둘다

#for item in bar.values():
 #   print(f"Item: {item}") 아이템 값만 출력

def prt(**kwargs):
    for key in kwargs.keys():
        print(f"key: {key}") #키 값만 출력
        
prt(**bar)