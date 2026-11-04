num = [500,100,50,10,5,1]
def makenum(n, max = 0): #Notice: MAX is INDEX
    t = 0
    for i in range(len(num)-max):
        if (y:= n - num[i+max]) < 0:
            continue
        elif y == 0:
            t += 1
        else:
            t += makenum(y, max=i)
    return t
print(makenum(50))