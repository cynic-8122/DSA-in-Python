N = int(input())
arr = []

for i in range(n) :
	a = int(input())
	arr.append(a)

Q = int(input())
for i in range(Q) :
	x, y  = input().split()
	x = int(x)
	y = int(y)
	ans = sum(arr[x : (y + 1)])
	print(ans)



