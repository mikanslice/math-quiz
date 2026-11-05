map = []
for i in range(9):
    map.append([j for j in input().strip()])
nodes = [{"c":[0,0],"d":-1}]
diffs = [[0,1],[-1,0],[0,-1],[1,0]]
reached = False
turn = 0
min = -1
while not reached:
    turn += 1
    tmpnode = []
    if len(nodes) < 1:
        break
    for node in nodes:
        c = node["c"]
        d = node["d"]
        for i in range(4):
            if i == d:
                continue
            p = [c[0]+diffs[i][0],c[1]+diffs[i][1]]
            if 0 <= p[0] < len(map[0]) and 0<= p[1] < len(map) and ((q:=map[p[1]][p[0]])=="." or q == "G"):
                if q == "G":
                    min = turn
                    reached=True
                    break
                map[p[1]][p[0]] = turn
                tmpnode.append({"c":p,"d":(i+2)%4})
            else:
                continue
    nodes.clear()
    nodes.extend(tmpnode)
if min < 1:
    print("Couldn't reached")
else:
    print(min)
"""
for j in map:
    print("".join(" "+str(k) if k=="#" or k=="S" or k == "G" or k//10 == 0 else str(k) for k in j))
"""
