print("1")
n = int(input())
arr = []
for i in range(0, n):
    x = int(input())
    arr.append(x)
q = int(input())
for i in range(0, q):
    x = int(input())
    if x in arr:
        print('yes')
    else:
        print('no')