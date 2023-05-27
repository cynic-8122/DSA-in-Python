
def Pivot(arr):
    indices = {}

    for i in range(len(arr)):
        if arr[i][0] in indices:
            continue
        indices[arr[i][0]] = i

    index = list(indices.values())
    index = sorted(index)
    return(index)

n = int(input())
darr = list(map(int, input().split()))
arr = []
for i in range(0, 2*n, 2):
    arr.append((darr[i], darr[i+1]))

candidates = Pivot(arr)

print(len(candidates))
print(*candidates)
