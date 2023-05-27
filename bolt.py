T = int(input())
for i in range(T) :
    k1, k2, k3, v = input().split()
    k1 = float(k1)
    k2 = float(k2) 
    k3 = float(k3)
    v = float(v)
    v_final = k1*k2*k3*v 
    t = 100/v_final
    t = rount(t, 2)
    if t < 9.58 :
        print("yes")
    else :
        print("no")