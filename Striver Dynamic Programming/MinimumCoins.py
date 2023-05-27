def Helper(num, x, i):
    if x == 0:
        return 0
    
    if i >= len(num):
        return float('inf')
        
    ans1 = float('inf')
    if num[i] <= x:
        ans1 = 1 + Helper(num, x-num[i], i)
    ans2 = Helper(num, x, i+1)
    
    return min(ans1, ans2)

num = [int(x) for x in input().split()]
x = int(input())

print(Helper(num, x, 0))