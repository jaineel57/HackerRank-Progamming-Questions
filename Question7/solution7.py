def chocolateFeast(n,c,m):
    ccount = int(n/c)
    wcount = ccount
    while ( wcount >= m):
        a = int((wcount)%(m))
        wcount = int((wcount-a)/m)
        ccount = ccount + wcount
        wcount = a + wcount
    print(ccount)
        
        
        
for _ in range(int(input())):
    n,c,m = input().split()
    chocolateFeast(int(n),int(c),int(m))