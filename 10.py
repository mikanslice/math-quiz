def three(p):
    if p == 3:
        return 1, 1, 2
    a, b, c = three(p-1)
    return b,c,a+b+c
d, e, f = three(30)
print(d+e+f)