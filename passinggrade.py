T = int(input())

for i in range(T) :
    A_min, B_min, C_min, T_min, A, B, C = input().split()
    A_min = int(A_min)
    B_min = int(B_min)
    C_min = int(C_min)
    T_min = int(T_min)
    A = int(A)
    B = int(B)
    C = int(C)
    if A >= A_min and B >= B_min and C >= C_min :
        if (A + B + C) >= T_min :
            print("YES")
        else :
            print("NO")
    else :
        print("NO")