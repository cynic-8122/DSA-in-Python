n = int(input())
arr = []

for i in range(n) :
	a = int(input())
	arr.append(a)

maximum = 1
for i in range(1, n ):
	x = max(arr[:i])
	if arr[i] > x :
		maximum += 1

print(2)
print(maximum)

