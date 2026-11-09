import copy
map = []
for i in range(9):
    map.append([int(j) for j in input().strip()])

def check(m,p):
    if p > 80:
        return True, m
    res = []
    y,x = divmod(p,9)
    pp = m[y][x]
    al = pp != 0
    exc = set()
    px = x//3
    py = y//3
    for i in range(9):
        ty, tx = divmod(i,3)
        tpx = px*3+tx
        tpy = py*3+ty
        if tpx != x or tpy != y:
            exc.add(m[tpy][tpx])
        if i != x:
            exc.add(m[y][i])
        if i != y:
            exc.add(m[i][x])
    exc.discard(0)
    for j in range(1, 10):
        if j in exc or (al and j != pp) :
            continue
        tmp = copy.deepcopy(m)
        tmp[y][x] = j
        able, rm = check(tmp, p+1)
        if able:
            res.extend(rm)
            break
    return len(res) != 0, res
a,b = check(map,0)

for k in b:
    print("".join(str(l) for l in k))