def check(p=[]):
    r = 0
    tmp = set()
    pos = len(p)

    fin = pos==8
    if fin:
        return 1

    for index, pt in enumerate(p):
        tmp.add(pt+(pos-index))
        tmp.add(pt-(pos-index))
        tmp.add(pt)
    for i in [j for j in range(8) if j not in tmp]:
        tmpp = p.copy()
        tmpp.append(i)
        r += check(p=tmpp)
    return r
print(check())
