prime = set()
i = 2
result = []
while i < 100:
    i+=1
    if (len([True for item in prime if i % item == 0])) == 0:
        prime.add(i)
for x in range(1,10001):
    if sum(y for y in range(1,x) if x%y==0) == x:
        result.append(x)
print(sum(result))