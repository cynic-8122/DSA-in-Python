def wiggly(arr, n):
    
    flag = True
    for i in range(n-1):
        
        if flag is True:
           
            if arr[i] > arr[i+1]:
                arr[i],arr[i+1] = arr[i+1],arr[i]
            
        else:    
            if arr[i] < arr[i+1]:
                arr[i],arr[i+1] = arr[i+1],arr[i]
        flag = bool(1 - flag)
    print(arr)

arr = [int(x) for x in input().split()]
wiggly(arr, len(arr))
