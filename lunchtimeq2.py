T = int(input())

S = "EQUINOX"
for i in range(T) :
    N, A, B  = [int(x) for x in input().split()]
    sum_a = 0
    sum_b = 0
    for j in range(N) :
        s = input()
        if s[0] in S :
            sum_a += A 
        else :
            sum_b += B 
    if sum_a > sum_b :
        print("SARTHAK")
    elif sum_a < sum_b :
        print("ANURADHA")
    else :
        print("DRAW")