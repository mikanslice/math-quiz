def arsum(p, q):
    r = []
    tmp = 0
    lp = len(p)
    lq = len(q)
    for i in range(max(lp,lq)):
        total = (p[i] if i < lp else 0) + (q[i] if i < lq else 0) + tmp
        tmp, s = divmod(total,10)
        r.append(s)
    if tmp > 0:
        r.append(tmp)
    return r
    
i = 2
a, b = [1], [1]
while True:
    i+=1
    a, b = b, arsum(a,b)
    if len(b) >= 100:
        break

print(i)


