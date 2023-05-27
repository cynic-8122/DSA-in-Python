def good(no_of_opr, req_jump, li_min, L, R) :
    if req_jump == 0 :
        return True
    if req_jump <= no_of_opr*(R) - li_min[no_of_opr - 1]:
        return True
    else :
        return False
        
T = int(input())

for i in range(T) :
    K, N, L, R = [int(x) for x in input().split()]
    min_sum = R*N
    max_sum = 0
    all_arr = []
    j_pointer = 0
    j = 0
    while j < K :
        arr = [int(x) for x in input().split()]
        all_arr.append(arr)
        s = sum(arr)
        if min_sum > s :
            min_sum = s
            j_pointer = j
        if max_sum < s :
            max_sum = s
        j += 1 
    li_min = sorted(all_arr[j_pointer])
    req_jump = max_sum - min_sum
    for j in range(1, N) :
        li_min[j] = li_min[j - 1] + li_min[j]
    
    left = 0
    right = N 
    while left <= right :
        mid = (left + right) // 2
        if good(mid, req_jump, li_min, L, R) :
            ans = mid
            right = mid - 1 
        else :
            left = mid + 1 
            
    print(ans)
    
    
            
            
    