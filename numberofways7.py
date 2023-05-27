
def ways(X, K, i, count_arr) :
	if i > X :
		return
	if i == X :
		count_arr[0] += 1
		return 
	n = 1
	while n <= K :
		ways(X, K, i + n, count_arr) 
		n += 1
	return count_arr 
	

T = int(input())
for i in range(T) :
	count_arr = [0]
	X, K = input().split()
	X = int(X)
	K = int(K)
	ways(X, K, 0, count_arr)
	print(count_arr[0])