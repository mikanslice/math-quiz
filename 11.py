num = [500,100,50,10,5,1]
def makenum(n, max = 0): #Notice: MAX is INDEX
    if n == 0:
        return 1
    else:
        t=0
        if len(num) > max + 1:
            th = n//num[max]
            for i in range(0,th+1):
                t += makenum(n-i*num[max], max=max+1)
            return t
        else:
            return 1
print(makenum(1000))