import math
prime = set()
i = 1
result = []
max = math.floor(math.sqrt(100000))
while i < max:
    i+=1
    if (len([True for item in prime if i % item == 0])) == 0:
        prime.add(i)
p = 0
for k in range(10,100):
    for l in range(10):
        t = k*1000+l*100+(k%10)*10+k//10
        isDividable = False
        for s in prime:
            if t%s==0:
                isDividable = True
                break
        if not isDividable:
            p+=1
print(p)