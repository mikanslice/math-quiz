things = [{"w":12,"v":40},{"w":7,"v":22},{"w":11,"v":35},{"w":8,"v":25},{"w":9,"v":30},{"w":6,"v":18},{"w":14,"v":48},{"w":5,"v":14},{"w":10,"v":33},{"w":13,"v":42}]
things.sort(key=lambda x: x["w"], reverse=True)
def check(m,v=0,maxi=0):
    if maxi >= len(things):
        return v
    r = {0}
    for i in range(min(m//things[maxi]["w"]+1,2)):
        r.add(check(m-things[maxi]["w"]*i, v=v+things[maxi]["v"]*i, maxi=maxi+1))
    return max(r)
print(check(50))
# this program is too messy because i didn't read the description, "Limit 1 per item."
# But, I don't have enough energy to rewrite the whole thing.