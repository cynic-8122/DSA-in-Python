# cook your dish here
T = int(input())

for i in range(T) :
    N, R = [int(x) for x in input().split()]
    arr1 = [int(x) for x in input().split()]
    arr2 = [int(x) for x in input().split()]
    relax_arr = []
    tension_arr = []
    for j in range(N - 1) :
        relax = arr1[j + 1] - arr1[j]
        relax = R*(relax)
        tension_arr.append(arr2[j] - relax)
    
    tension_arr.append(arr2[N - 1])
   
    for j in range(1, N) :
        tension_arr[j] += tension_arr[j - 1]
    
    print(f"tension_arr = {tension_arr}")    
    print(max(tension_arr))
        
        
        
        
    
    
    