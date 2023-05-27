n = int(input())

arr = list(map(int, input().split()))

while len(arr) >= 1 :
	i = 0
	x = arr[i]
	if len(arr) == 1:
		special_element = x

	arr.remove(x)
	if x in arr :
		arr.remove(x)

	else:
		special_element = x
		break

print(special_element)






