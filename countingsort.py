x = int(input())
for i in range(0, x):
    y = int(input())
    arr = list(map(int, input().split()))
    if(len(arr) == y):
        arr.sort()
        for i in range(0, y):
            print(arr[i], end = " ")
        print("")