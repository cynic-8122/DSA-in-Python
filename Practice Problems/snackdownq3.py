# cook your dish here
def convert(lst):
      
    return ' '.join(map(str, lst))

def merge(arr1, arr2):
    sorted_arr = []
    i = 0
    j = 0
    while i < len(arr1) and j < len(arr2) :
        if arr1[i][0] <= arr2[j][0]:
            sorted_arr.append(arr1[i])
            i += 1 
            
        else :
            sorted_arr.append(arr2[j])
            j += 1 
            
    while i < len(arr1):
        sorted_arr.append(arr1[i])
        i += 1 
        
    while j < len(arr2):
        sorted_arr.append(arr2[j])
        j += 1 
        
    return sorted_arr
    
def mergesort(arr, left, right):
    if left > right :
        return
    if left == right :
        return [arr[left]]
        
    mid = (left + right)//2 
    left = mergesort(arr, left, mid)
    right = mergesort(arr, mid+1, right)
    
    return merge(left, right)
    
    
T = int(input())

for i in range(T) :
    N = int(input())
    arr = [int(x) for x in input().split()]
    ans_arr = [0]*N 
    max_arr = -float('inf')
    for i in range(N):
        max_arr = max(max_arr, arr[i])
        arr[i] = [arr[i], i]
        
    temp_arr = mergesort(arr, 0, N-1)
    check = 0
    for i in range(N) :
        idx = temp_arr[i][1]
        val = temp_arr[i][0]
        ans_arr[idx] = check
        if val and check % val == check :
            check += 1 
            check = check%(max_arr)
        
    print(convert(ans_arr))
        
        
    