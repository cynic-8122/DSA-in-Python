arr = []
app = 1
for i in range(1, 9) :
    app += 10**(i)
    arr.append(app)
print(arr)
    
T = int(input())

for i in range(T) :
    x = int(input())
    left = 0
    right = len(arr)
    while x >= 11 :
        while left <= right :
            mid = (left + right)//2
            if arr[mid] == x :
                ans = arr[mid]
                break
        
            if arr[mid] > x :
                right = mid - 1
            
            if arr[mid] < x :
                ans = arr[mid]
                middle = mid
                left = mid + 1
        x -= ans
        left = 0
        right = middle
        
    if x == 0 :
        print("YES")
        
    else :
        print("NO")
        
    