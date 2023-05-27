T = int(input())

for i in range(T) :
	N = int(input())
	arr = [int(x) for x in input().split()]
	q = int(input())
	for j in range(q) :
		ans = 0
		L, R = [int(x) for x in input().split()]
		arr_start = L % N 
		com_cycles = (R - L + 1)//N 
		arr_end = R % N 
		ans = com_cycles*(sum(arr))
		arr_start += com_cycles - 1 
		arr_start = arr_start % N
		count = (R - L + 1) % N
		print("ans", ans)
		while (count) :
			arr_start = arr_start % N
			print("arr_start", arr_start)
			print("arr_end", arr_end)
			ans += arr[arr_start]
			print("pointer at", arr[arr_start])
			arr_start += 1
			count -= 1 

		
		print(ans)


