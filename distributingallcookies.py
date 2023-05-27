arr = list(map(int, input().split()))
index_arr = []

t = tuple(arr)
m = min(arr)

print(f"( 1, {len(arr)} ) \n {m}")

for i in range(0, len(arr)):
	arr[i] -= m


for i in range(0, len(arr)):
	if arr[i] == 0 :
		index_arr.append(i)

a = 0
j = 0
b = len(index_arr)
darr = []
while a < b :
	x = arr[j:index_arr[a]]
	

	darr.append(x)
	j = index_arr[a] + 1
	a += 1

x = arr[j : len(arr)]
darr.append(x)

print(arr, darr)


