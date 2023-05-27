T = int(input())

for i in range(T) :
	N, K = [int(x) for x in input().split()]
	arr = [int(x) for x in input().split()]
	ans = 0
	while True :
		count = 0
		add = 0
		for i in range(N) :
			x = arr[i]
			add += x
			if x&1:
				count += 1
			arr[i] = arr[i]>>1

		if count%K :
			ans += (count//K) + 1
		else :
			ans += (count//K)
		if not add :
			break
	print(ans)


	