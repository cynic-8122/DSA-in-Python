n = int(input())
arr = []
darr = []


for i in range(n) :
    a = int(input())
    arr.append(a)

i = 0
while i < len(arr) :
    j = i
    m = 0
    dist = 1
    while j < len(arr) :
        if dist < 0 :
            break
        k = j + 1
        X1 = arr[j]
        X2 = arr[k]
        if X1 == X2:
            m += 1
        elif abs(X1 - X2) <= 1 :
            m += 1
            dist -= 1
            
        else :
            break
        darr.append(m)
        j += 1
    i += 1
    
print(max(darr))