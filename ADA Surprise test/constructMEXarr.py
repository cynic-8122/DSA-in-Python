
arr = [int(x) for x in input().split()]

val = 0
for i in range(len(arr)):
	t = arr[i]
	temp = 1<<(t-1)
	val = val|temp

print(val)

barr = [0 for i in range(len(arr))]

for i in range(len(arr)):
	q = val
	count = 1
	while q and count < arr[i] :
		digit = q&1

		if not digit:
			break

		q = q>>1
		count += 1

	barr[i] = count

print(barr)

