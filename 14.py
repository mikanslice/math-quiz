p = {x: x for x in range(2,10001)}
i = 0
while True:
    i+=1
    p = {k: y for k,item in p.items() if (y := (item//2 if(item%2==0) else item*3+1)) != 1}
    if len(p) < 2:
        break
print(next(iter(p)))
