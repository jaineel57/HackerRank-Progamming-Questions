def check(x):
    nstr = str(x)
    d = len(nstr)
    val = pow(x,2)
    snstr = str(val)
    a = len(snstr)
    if(a > 1):
        l = int(snstr[0:(a-d)])
        r = int(snstr[(a-d):])
        sum = l + r
        if ( sum == x):
            return True
        
        
def kaprekarNumbers(array):
    final = []
    for i in array:
        if( check(i) == True and i > 3):
            final.append(i)
        elif(i == 1):
            final.append(i)
    if (len(final) == 0):
        print("INVALID RANGE")
    else:
        print(' '.join(map(str, final)))
        

p = int(input())
q = int(input())
array = []
for i in range(p,q+1):
    array.append(i)
    i = i + 1
kaprekarNumbers(array)
