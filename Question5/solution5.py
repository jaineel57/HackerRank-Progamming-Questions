def function(arr,n):
    array = []
    for i in range(0,n):
        for j in range(i+1,n):
            if ( arr[i] == arr[j]):
                add = j - i 
                array.append(add)
    if (array == []):
        print('-1')
    else:
        print(min(array))
    
n = int(input())
arr = list([int(x) for x in input().split()])
function(arr,n)