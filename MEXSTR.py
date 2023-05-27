def is_subsequence(a, b) :
	i = 0
	j = 0
	while i < len(a) and j < len(b) :
		if a[i] == b[j] :
			i += 1
			j += 1
		else :
			i += 1

	if j == len(b) and i <= len(a) :
		return True
	else :
		return False

T = int(input())
for i in range(T) :
	S = input()
	left = 0
	right = 1000000
	while left <= right:
		mid = left + (right - left)//2
		a = bin(mid) 
		a = str(a[2:])

		if not is_subsequence(S, a) :
			ans = a
			right = mid - 1

		else :
			left = mid + 1

	print(ans)
			
		

