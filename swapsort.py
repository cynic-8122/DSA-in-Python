def sort(arr):
    x = 0
    darr = []
    
    for i in range(0, len(arr)) :
        minindex = i
        a = i + 1
        while(a<len(arr)):
            if(arr[a]<arr[minindex]):
                minindex = a
            a += 1
        if(i != minindex):
            arr[i],arr[minindex]=arr[minindex],arr[i]
            x += 1
            darr.append(i)
            darr.append(minindex)
            
            if(arr == sorted(arr)):
                break
        
    print(x)
    for i in range(len(darr)):
        print(darr[i], end = " ")
      
n = int(input())
arr = list(map(int, input().split()))
sort(arr)