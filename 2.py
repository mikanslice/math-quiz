prime = set()
i = 2
while len(prime) < 100:
    i+=1
    if (len([True for item in prime if i % item == 0])) == 0:
        prime.add(i)
print(i)