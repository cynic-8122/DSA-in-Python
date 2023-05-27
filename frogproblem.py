N = int(input())
arr = [int(x) for x in input().split()]

cost = 0
for i in range(N - 2) :
	a = abs(arr[i] - arr[i + 1])
	b = abs(arr[i] - arr[i + 2])
	if b <= a :
		i += 2
		cost += b
	else :
		i += 1
		cost += a

print(cost)