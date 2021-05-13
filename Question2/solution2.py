from collections import Counter
def equalizeArray(arr):
    n = len(arr)
    ans = max([arr.count(i) for i in arr])
    print(n-ans)


n = int(input())
arr = list([int(x) for x in input().split()])
equalizeArray(arr)