
# iteration : 순회
bar = [10 , 20 , 30, 40 , 50]

for val in bar:
    print(val)

idx = 0
for val in bar:
    print(f"{idx} index : {val}")
    idx += 1
    
for idx, val in enumerate(bar):
    print(f"{idx} index : {val}")

# unpacking
pos , kin , sol = [2, 3 , 4 ]
print(pos,kin,sol)
# 0 index 10