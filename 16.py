i = 10
r = 0
fact = [1,1,2,6,24,120,720,5040,40320,362880]
while fact[9]*(digits:=len(str(i))) > 10**digits:
    if sum(fact[int(item)] for item in str(i)) == i:
        r+=i
    i+=1
print(r)