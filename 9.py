prime = set()
i = 2
r = 0
while i < 10000:
    i+=1
    if (len([True for item in prime if i % item == 0])) == 0:
        prime.add(i)
        if i-2 in prime:
            r += 1
print(r)