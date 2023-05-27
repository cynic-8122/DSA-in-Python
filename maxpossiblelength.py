N = int(input())
k = int(input())
arr = []
sum_arr = 0
for i in range(N) :
	a = float(input())
	sum_arr += a
	arr.append(a)

left = 0
right = min((sum_arr/k),min(arr))
mid = 0.0
check = True

for i in range(30) :
	sum2 = 0
	mid = (left + right) / 2
	for j in range(len(arr)) :
		sum2 += (arr[j]) // mid
	if sum2 >= k :
		left = mid

	else :
		right = mid

if check :
	print(mid)






