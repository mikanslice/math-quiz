tmp = 12345678
num = []
while tmp != 0:
    tmp,b = divmod(tmp,2)
    num.append(b)
print(len([i for i in num if i == 1]))
