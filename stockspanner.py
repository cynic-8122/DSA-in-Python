n = int(input())
arr = list(map(int, input().split()))

darr = []
for j in range((len(arr) - 1), -1, -1) :
	i = j - 1
	count = 1
	while i >= 0:
		a = arr[j]
		b = arr[i]
		if a >= b :
			count += 1

		else :
			break

		i -= 1

	darr.append(count)

def reverse(arr) :
	arr2 = []
	for i in range(-1, (-len(arr) - 1), -1) :
		x = arr[i]
		arr2.append(x)

	return arr2

darr = reverse(darr)
print(darr)






