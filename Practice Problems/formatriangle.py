from sys import stdin

def possibleToMakeTriangle(arr):
    arr.sort()
    for i in range(len(arr) - 2):
        a = arr[i]
        for j in range(i + 1, len(arr) - 1):
            b = arr[j]
            left = j + 1
            right = len(arr) - 1
            while left <= right :
                mid = (left + right)//2
                c = arr[mid]
                if b > c - a :
                    print(a, b, c)
                    return True
                else:
                    right = mid - 1
    return False
            
        

    # Write your function here.

# Main code.
t = int(input().strip())

for i in range(t):
    n = list(map(int, stdin.readline().strip().split(" ")))

    if len(n) > 1:
        arr = n
    else:
        arr = list(map(int, stdin.readline().strip().split(" ")))

    if (possibleToMakeTriangle(arr)):
        print("YES")
    else:
        print("NO")
