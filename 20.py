import math
nums = [i**3 for i in range(100)]
r = 0
i = 0
p = set()
already = set()
for anum in nums:
    for bnum in nums:
        if anum < bnum:
            break
        if (tmp:=anum + bnum) <= 1000000:
            if tmp in p and tmp not in already:
                r+=1
                already.add(tmp)
            else:
               p.add(tmp)
print(r)