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
    for i in [j for j in range(8) if j not in tmp]:
        tmpp = p.copy()
        tmpp.append(i)
        if len(tmpp) == 3 and tmpp[1] == 5 and tmpp[2] == 4:
            print(tmpp,tmp)
        r += check(p=tmpp)
    return r
print(check())