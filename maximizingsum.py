N = int(input())

K = int(input())

arr = list(map(int,input().split()))

i = 0
SUM = 0
b = len(arr)

while i < b :
	if arr[i] > 0 :
		SUM += arr[i]

	i += 1

i = 0

while (i < len(arr)) and (K > 0) :
	a = min(arr)
	if a < 0 :
		SUM += (-a)
		arr.remove(a)
		K -= 1

	i += 1

print(SUM)









