N = int(input())
arr1 = [int(x) for x in input().split()]

M = int(input())
arr2 = [int(x) for x in input().split()]

finalarr = set()
for x in arr2:
	check = True
	for y in arr1:
		if (x-y) > 0 and (x - y) in finalarr:
			check = False
			break

	if check :
		finalarr.add(x-y)


tempset = set()
for x in arr2:
	tempset.add(x)

ansarr = []
for x in finalarr:
	check2 = True
	for y in arr1:
		if (x+y) in tempset:
			continue

		else:
			check2 = False
			break

	if check2:
		ansarr.append(x)

ansarr.sort()
print(*ansarr)
