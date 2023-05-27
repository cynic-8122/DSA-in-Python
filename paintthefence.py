N, Q = [int(x) for x in input().split()]

ranges = []

for i in range(Q) :
	arr = [int(x) for x in input().split()]
	ranges.append(arr)

count = 0
ans_arr = []
count_arr = []
for i in range(N) :
	ans_arr.append(i + 1)

for i in range(Q) :
	L, R = ranges[i][0], ranges[i][1]
	None_count = 0
	tiles_count = 0

	for j in range(L, R + 1):
		if arr[j] :
			ans_arr[j] = None
			tiles_count += 1

		else :
			None_count += 1
	count += tiles_count


