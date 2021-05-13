def taumBday(b,w,bc,wc,z):
    if ( bc == wc):
        cost = (b*bc) + (w*wc)
        print(cost)
    elif ( bc > wc):
        if ( bc == wc + z):
            cost = (b*bc) + (w*wc)
            print(cost)
        elif ( bc > wc + z):
            val = (wc + z)
            cost = (b*val) + (w*wc)
            print(cost)
        else:
            cost = (b*bc) + (w*wc)
            print(cost)
    elif (wc > bc):
        if ( wc == bc + z):
            cost = (b*bc) + (w*wc)
            print(cost)
        elif(wc > bc + z):
            val = (bc + z)
            cost = (b*bc) + (w*val)
            print(cost)
        else:
            cost = (b*bc) + (w*wc)
            print(cost)
            
            
for _ in range(int(input())):
    b,w = input().split()
    bc,wc,z = input().split()
    taumBday(int(b),int(w),int(bc),int(wc),int(z))