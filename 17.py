def check(p=[]):
    r = 0
    tmp = set()
    pos = len(p)

    fin = pos==8
    if fin:
        return 1

    for index, pt in enumerate(p):
        tmp.add(pt-index+pos-1)
        tmp.add(pt-index-pos+1)
        tmp.add(pt)
        if len(p) == 2 and p[1] == 5:
            print(p,pt,index,pt-index+pos-1,pt-index-pos+1)
    for i in [j for j in range(8) if j not in tmp]:
        tmpp = p.copy()
        tmpp.append(i)
        r += check(p=tmpp)
    return r
print(check())