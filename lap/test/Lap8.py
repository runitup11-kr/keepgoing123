

def calculate_average(*args):
    count = len(args)
    total = sum(args)
    average = total / count 
    
    return {"입력 개수":count,
            "총합":total,
            "평균":average}


print(calculate_average(70,80,90,100,200))    