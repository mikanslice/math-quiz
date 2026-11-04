def counter(a: int) -> int:
    if a < 1: return 0
    i = 0
    a, b = divmod(a, 5)
    while b == 0:
        i+=1
        a, b = divmod(a, 5)
    return i
result = []
for i in range(1, 101):
    if (y:= counter(i)) > 0:
        result.append(y)
print(sum(result))