n = int(input())

arr = []
i = 1
while i <= n :
	a = int(input())
	arr.append(a)
	i += 1

while len(arr) > 1 :
	x = min(arr)
	arr.remove(x)

	y = min(arr)
	arr.remove(y)

	b = (3*x + 2*y)% 100
	arr.append(b)

print(arr[0])

