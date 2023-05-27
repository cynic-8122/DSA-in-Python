print("2")
n = int(input())
arr = []
ans = 1
sample = int(input())
arr.append(sample)
for i in range(1, n):
    x = int(input())
    arr.append(x)
    if arr[i]>=sample:
        ans +=1
        sample = arr[i]
print(ans)