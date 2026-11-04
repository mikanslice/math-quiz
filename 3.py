num = [1]
for j in range(100):
    tmp = 0
    for i, item in enumerate(num):
        tmp, num[i] = divmod(tmp+item*2, 10)
    if tmp != 0:
        num.append(1)
print(sum(num))