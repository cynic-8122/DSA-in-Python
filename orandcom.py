# cook your dish here
T = int(input())

for i in range(T):
    
    X = int(input())
    
    
    temp = bin(X)
    temp = str(temp)
    temp = temp[2:]
    count1 = 0
    count0 = 0 
    arr1 = []
    arr = []
    for i in range(len(temp)-1, -1, -1):
        t = temp[i]
        if t == '1':
            count1 += 1
            arr.append(i)
            
        if t == '0':
            count0 += 1
            arr1.append(i)
            
        if count1 >=2 :
            break
        
    if count1 >= 2 :
        A = X 
        p = len(temp) - arr[0] - 1 
        B = X^(1<<(p))
        q = len(temp) - arr[1] - 1 
        C = X^(1<<(q))
        
        
    elif count0 >= 2:
        A = X 
        p = len(temp) - arr1[0] - 1 
        B = X^(1<<(p))
        q = len(temp) - arr1[1] - 1 
        C = X^(1<<(q))
        
    elif X == 3:
        A = X 
        B = 1 
        C = 2
        
    elif X == 2:
        A = 2
        B = 3
        C = 4
        
    else:
        A = 1  
        B = 3
        C = 5
        
    print(A, B, C)
    
        