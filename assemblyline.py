def bisect(arr, val) :
	left = 0
	right = len(arr)
	while left <= right :
		mid = (left + right)//2
		if arr[mid] >= val :
			right =  mid - 1
		if arr[mid] < val :
			ans = arr[mid]
			idx = mid
			left = mid + 1
	return idx

N = int(input()) 

H = [int(x) for x in input().split()]

barr = []
count = 0
idx = 0
i = 0
max_so_far = 0
while i < (N) :
	carr = [H[i]]
	
	if (i + 1) < N :
		if H[i] < H[i + 1] :
			carr.append(H[i + 1])
			j = i + 1
			while (j + 1) < N:
				if H[j] < H[j + 1] :
					carr.append(H[j + 1])
					j += 1
				else :
					break
			i = j

	count += 1
	i += 1
	
	barr.append(carr)
	if len(carr) > max_so_far :
		max_so_far = len(carr)
		idx = count - 1

print(barr)
print(idx)






