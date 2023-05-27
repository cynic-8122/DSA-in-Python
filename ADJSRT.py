n = int(input())

arr = list(map(int, input().split()))

def adjsrt(arr) :
	no_of_swaps = 0
	swap = []
	l = len(arr)
	for i in range(0, l) :
		S = False
		for j in range(0, l-i-1) :
			if arr[j] > arr[j + 1] :
				no_of_swaps += 1
				swap.append(j)
				arr[j], arr[j + 1] = arr[j + 1], arr[j]
				S = True

		if not S :
			print(no_of_swaps)

			for s in swap :
				print(s, end = " ")

			return

adjsrt(arr)


