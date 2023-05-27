# cook your dish here
T = int(input())

for i in range(T) :
    Y_1, X_1, Y_2, X_2 = [int(x) for x in input().split()]
    ans = 0
    while Y_1 <= Y_2 :
        #c = ans
        ans += (Y_1)*(Y_1 + 1)//2 + (Y_1)*(X_1 - 1) + (X_1 - 1)*(X_1 - 2)//2 
        #print(ans - c)
        Y_1 += 1 
    
    
    X_1 += 1   
    while X_1 <= X_2 :
        #c = ans
        ans += (Y_2)*(Y_2 + 1)//2 + (Y_2)*(X_1 - 1) + (X_1 - 1)*(X_1 - 2)//2 
        X_1 += 1
        #print(ans - c) 
    print(ans)
        
        
        