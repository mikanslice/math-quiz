prime = set()
i = 2
while i < 20:
    i+=1
    if (len([True for item in prime if i % item == 0])) == 0:
        prime.add(i)

r = {}
for j in range(2,21):
    num = {}
    for k in prime:
        while (y:=j % k) == 0:
            j = j//k
            if k in num:
                num[k] += 1
            else:
                num[k] = 1
    for m, l in num.items():
        if m not in r:
            r[m] = l
        else:
            r[m] = max(r[m],num[m])

p=1
for n, o in r.items():
    p*=n**o
    
print(p)