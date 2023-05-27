print("2")
n = int(input())
arr = []
square =0
for i in range(0, n):
    x = int(input())
    arr.append(x)
    square += x**2
s = sum(arr)
print((s**2-square)//2)