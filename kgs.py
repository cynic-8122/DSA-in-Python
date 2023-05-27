T = int(input())
for i in range(T) :
    N, K = [int(x) for x in input().split()]
    S = input()
    check = 0
    count = 0
    condition = False
    for j in range(len(S)//2+1):
        if check == K :
            condition = True
            break
        if S[j] != S[-(j + 1)] :
            check+= 1
    if condition :
        print(count)
        
    else :   
        for j in range(len(S)//2) :
            if (check + count) == K :
                print(count)
                
                break
            if S[j] != S[-(j + 1)] :
                count += 1
           