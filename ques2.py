arr = [int(x) for x in input().split()]
n = len(arr)
for i in range(1, len(arr) - 1) :
	if arr[i - 1] < arr[i] and arr[i] > arr[i + 1] :
		print(i)
		break

print("No possible case")



