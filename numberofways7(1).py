T = int(input())

def working_out_DP(X, K, count_arr_initial, idx) :
	for i in range(1, K + 1) :
		for j in range(1, i):
			count_arr_initial[i] += count_arr_initial[j] + 1




for i in range(T) :
	X, K = [int(x) for x in input().split()]
	count_arr = [0]*(X + 1)
	count_arr_initial = [0]