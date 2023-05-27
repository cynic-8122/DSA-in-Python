T = int(input())

for i in range(T) :
    N = int(input())
    arr = [int(x) for x in input().split()]
    count = 0
    x = min(arr)
    for i in range(N) :
        check = True 
        val = arr[i]
        if val == x :
            continue
        while check :
            
            count += 1 
            if x <= val//2 :
                if isinstance(val/2, int) and x == val/2:
                    val = val>>1
                    continue 
                else :
                    check = False
                    break
            val = val>>1
    print(min(N, count))