# cook your dish here
T = int(input())

for i in range(T) :
    N, K = [int(x) for x in input().split()]
    S = str(input())
    arr = [int(x) for x in input().split()]
    ans = 0
    ans_arr = []
    for i in range(0, N - 1):
        if S[i] == S[i + 1] :
            ans += 2
        else :
            ans += 1
        x = int(S[i])
        ans_arr.append(x)
    ans_arr.append(int(S[-1]))
    for i in range(K) :
        idx = arr[i] - 1 
        if idx == 0 :
            if ans_arr[idx] == ans_arr[idx + 1]:
                ans -= 1
            else :
                ans += 1
            print(ans)
            ans_arr[idx] = ans_arr[idx]^1
        elif idx == (N - 1) :
            if ans_arr[idx] == ans_arr[idx - 1] :
                ans -= 1 
            else :
                ans += 1
            ans_arr[idx] = ans_arr[idx]^1
            print(ans)
        else :
            #print("idx", idx)
            if ans_arr[idx] == ans_arr[idx - 1] :
                if ans_arr[idx] == ans_arr[idx + 1] :
                    ans -= 2
            else :
                if ans_arr[idx] != ans_arr[idx + 1] :
                    ans += 2
            print(ans)
            ans_arr[idx] = ans_arr[idx]^1
                    
                    
                
            
            
    
    
                
            
                
            