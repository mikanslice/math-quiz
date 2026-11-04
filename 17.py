map = []
for i in range(9):
    map.append([j for j in input().strip()])
node = [{"c":[0,0],"d":"x"}]

reached = False
while not reached:
    
# Notice: Regen Node, NOT reusable