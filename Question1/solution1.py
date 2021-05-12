def gridChallenge(b):
    n = len(b)
    m = len(b[0])
    for j in range(m):
        for i in range(n-1):
            if b[i][j] > b[i+1][j]:
                return False
    return True



for _ in range(int(input())):
    n = int(input())
    b = []
    for _ in range(n):
        b.append(sorted(input()))
    if (gridChallenge(b)):
        print('YES')
    else:
        print('NO')

    
