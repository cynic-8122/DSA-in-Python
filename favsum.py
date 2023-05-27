def Bisect_right(arr, x, left, right) :
    while left <= right :
        mid = left + (right - left) //2
        if arr[mid] <= x :
            left = mid + 1
            ans = mid
        else:
            right = mid - 1
    
    return ans
            
 
t = int(input())
for i in range(t) :
    n, x = input().split()
    n = int(n)
    x = int(x)
    arr = list(map(int, input().split()))
    arr.sort()
    m = Bisect_right(arr, x, 0, len(arr))
    sum_arr = sum(arr[:m])
    answer = (x*(x + 1)//2) - 2*(sum_arr)
    print(answer)