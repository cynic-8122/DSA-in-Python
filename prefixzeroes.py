def func(S, K):
    if len(S) == 0 :
        return 0

    tempdiff = (10 - int(S[0])) if int(S[0]) else 0

    if len(S) == 1 and K >= tempdiff :
        return 1


    mindiff = float('inf')
    idx = -1
    for i in range(len(S)):
        t = S[i]
        if t == '0':
            mindiff = 0
            idx = i 
            break

        diff = 10 - int(S[i])

        if diff < mindiff :
            idx = i 
            mindiff = diff 

    newleftsubstring = ''
    for i in range(idx):
        t1 = (int(S[i]) + mindiff)%10
        newleftsubstring += str(t1)

    rightsubstring = S[(idx+1):]
    ans1 = 0 
    if K >= mindiff :
        ans1 = func(newleftsubstring, K - mindiff)

    ans2 = 0
    if K >= 0 and ans1:
        ans1 += 1 
        ans2 = func(rightsubstring, K)

    return ans1 + ans2

T = int(input())

for i in range(T):
    N, K = [int(x) for x in input().split()]
    S = str(input())
    print(func(S, K))
    