T = int(input())

for i  in range(T) :
	arr = [int(x) for x in input().split()]
	drr = sorted(arr)
	y = len(arr)
	a = drr[(y//2)]
	print(a)

