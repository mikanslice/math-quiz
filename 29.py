a = 987654321
b = 123456789
while b != 0:
    a,b=b,a%b
print(a)