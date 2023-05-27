# cook your dish here
N = int(input())

for i in range(N) :
    I, J = [int(x) for x in input().split()]
    count = 0 
    a = max(I, J)
    b = (I + J) - a
    if a == b :
        print(count)
        continue

    while a > b  :
        check = False
        if a & 1 == 1 :
            check = True
            
        a = a>>1 
        count += 1
    print(f"a after first while loop is : {a}")
    if a == b :
        print(count)
    else :
        a = a << 1 
        if check :
            a += 1
        print(f"a restored : {a}")
        count -= 1
        print(f"count corrected : {count}") 
        
        while a != b :
            check2 = False
            a = a>>1 
            b = b>>1
            count += 2
            if a == 1 or b == 1 :
                check2 = True
                break
        if check2:
            while a != 1 :
                if a & 1 == 1 :
                    a -= 1 
                a = a>>1 
                count += 1 
            
        print(count)
            
        
        
        