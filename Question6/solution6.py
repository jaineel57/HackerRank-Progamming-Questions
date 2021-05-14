def howManyGames(p,d,m,s):
    count = 0
    array = []
    for i in range(p,m,-d):
        array.append(i)
    n = len(array)
    val = int(s/m)
    #print(val)
    for i in range(val-n):
        array.append(m)
    #print(array)
    total = 0
    for x in array:
        total = total + x
        if (total<=s):
            count = count + 1
    print(count)
p,d,m,s = input().split()
p = int(p)
d = int(d)
m = int(m)
s = int(s)
howManyGames(p,d,m,s)