def no_of_paratas(t, R) :
	count = 0
	while t - R >= 0 :
		count += 1
		R += (count + 1)*R

	return count

T = int(input())

for i in range(T) :
	P = int(input())
	arr = list(map(int, input().split()))
	left = 0
	ranks = arr[1:]
	max_rank = max(ranks)
	right = (max_rank*(P*(P + 1)))//2
	while left < right :
		mid = (left + right) // 2
		
		final_count = 0
		for i in range(len(ranks)) :
			final_count += no_of_paratas(mid, ranks[i])
			
		if final_count >= P :
			right = mid - 1
		else :
			left = mid + 1
	print(mid)

print(no_of_paratas(6, 1))
print(no_of_paratas(6, 2))
print(no_of_paratas(6, 3))
print(no_of_paratas(6, 4))
