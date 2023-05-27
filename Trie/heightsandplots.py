N, Q = [int(x) for x in input().split()]

arr = [int(x) for x in input().split()]

ansarr = [0 for i in range(N)]
for x in arr:
	ansarr[x-1] += 1


for i in range(Q):
	query = int(input())
	leftans = 0 if query-2 < 0 else ansarr[query-2]
	rightans = 0 if query >= N else ansarr[query]

	if ansarr[query-1]:
		print(ansarr[query-1])

	else:
		print(max(leftans, rightans))


	


	

