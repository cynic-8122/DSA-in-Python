T = int(input())

for i in range(T) :
    L = int(input())
    s = str(input())
    zero_count = 0
    one_count = 0
    check = True
    if s[0] == '1' :
        print("YES")
    else :
        zero_count += 1 
        for j in range(1, L) :
            if s[j] == '0':
                zero_count += 1 
            if s[j] == '1' :
                one_count += 1 
            
            if (one_count/(one_count+zero_count))*100 >= 50 :
                print("YES")
                check = False
                break
        if ((one_count/(L)*100 >= 50)) and (check == True):
            print("YES")
        elif check:
            print("NO")