N, K = [int(x) for x in input().split()]

arr = [int(x) for x in input().split()]

prefix_arr = []
sum_so_far = 0
for i in range(N):
	sum_so_far += arr[i]
	prefix_arr.append(sum_so_far)

temp_arr = []
Hashmap = {}
for i in range(N):
	x = prefix_arr[i]%K
	if x in Hashmap.keys() :
		L = Hashmap[x]
		print(L, i)
		break
		
	if x == 0:
		print(0, i)
		break
	temp_arr.append(x)


