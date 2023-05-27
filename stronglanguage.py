T = int(input())
for i in range(T) :
    N, K = input().split()
    N = int(N)
    K = int(K)
    S = input()
    
    count = 0
    j = 0
    while j < (len(S) - 1) :
        if S[j] == "*" :
            count = 1 
            i = j + 1
            while i < len(S) and count <= K :

                if S[i] == "*" :
                    count += 1 
                    i += 1

                else :
                    break
            if count >= K :
                break
            else :
                j = i + 1
                
        else :
            j += 1       

    if count >= K :
        print("yes")
    else :
        print("no")