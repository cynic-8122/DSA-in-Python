T = int(input())
 
for i in range(T) :
    n = int(input())
    count = 0
    for j in range(1, n + 1) :
        a = str(j)
        if len(a) == 1 :
            count += 1
        else :
            comp = a[0]
            check = True
            for k in range(1, len(a)):
                if a[k] != comp :
                    
                    check = False
                    break
            if check :
                count += 1 
    print(count)