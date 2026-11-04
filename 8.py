import math
r = 0
i = 0
while r < 2:
    i+=1
    max = math.floor(math.sqrt(i//2+1))
    able = 0
    for j in range(1,max+1):
        for k in range(1, j+1):
            if i == j**3 + k**3:
                if able > 0:
                    r+=1
                    continue
                able+=1
print(i)