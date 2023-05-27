
class Entry:
	def __init__(self, value, idx):
		self.value = value
		self.idx = idx

def countminimumswaps(arr):
	darr = []
	for i in range(len(arr)):
		temp = Entry(arr[i], i)
		darr.append(temp)

	darr = sorted(darr, key = lambda Entry:Entry.value)

	count = 0
	i = 0

	while i < len(arr):
		index = darr[i].idx

		if i == index :
			i += 1
			continue

		darr[i], darr[index] = darr[index], darr[i]
		count += 1

	return count 

arr = [int(x) for x in input().split()]
print(countminimumswaps(arr))






