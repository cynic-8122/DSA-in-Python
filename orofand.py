
T = int(input())

for i in range(T) :
    N, Q = [int(x) for x in input().split()]
    arr = [int(x) for x in input().split()]
    ans = 0
    for j in range(N) :
        ans = ans|arr[j]
    
    print(ans)    
    
    for j in range(Q) :
        X, V = [int(x) for x in input().split()]
        ans = (ans^arr[X - 1])|V
        print(ans)

    
        
        
        
    
    