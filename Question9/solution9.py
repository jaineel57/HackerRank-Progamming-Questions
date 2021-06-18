import itertools
def alt(b):
    for j in range(len(b) - 2):
            if (b[j] != b[j+2]):
                return False
    if (b[0] == b[1]):
        return False
    return True
def test(t,m,n):
    c = []
    for i in t:
        if (( i == m) or (i == n)):
            c.append(i)
    return c


def alternate(s,n):
    se = list(set(s))
    s = list(s)
    temp = list(itertools.combinations(se,2))
    check = []
    for x in temp:
        b = test(s,x[1],x[0])
        if (alt(b)):
            check.append(len(b))
    if ( len(check) == 0):
        return 0
    else:
        return max(check)

n = int(input())
s = input()
print(alternate(s,n))
