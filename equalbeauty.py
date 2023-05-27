# cook your dish here
T = int(input())

for i in range(T):
    N = int(input())
    arr = [int(x) for x in input().split()]
    arr.sort()
    l = 0
    r = N - 1
    #print(arr)
    ans = float('inf')
    while l <= r :       
        mid = (l + r)//2
        diff1 = arr[mid - 1] - arr[0]
        diff2 = arr[-1] - arr[mid]
        if diff1 == diff2 :
            ans = 0
            break
        
        elif diff1 > diff2 :
            ans = min(ans, diff1 - diff2)
            r = mid - 1 
            
        else :
            ans = min(ans, diff2 - diff1)
            l = mid + 1 
            
    print(min(ans, (arr[-1] - arr[0] - arr[-2] + arr[1])))
        
        