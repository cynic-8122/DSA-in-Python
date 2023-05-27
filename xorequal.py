T = int(input())

for i in range(T):
	N, X = [int(x) for x in input().split()]
	arr = [int(x) for x in input().split()]
	Hashmap = {}
	for i in range(N):
		if arr[i] in Hashmap.keys() :
			Hashmap[arr[i]] += 1

		else :
			Hashmap[arr[i]] = 1

	max_count = -float('inf')
	min_change = float('inf')

	for x in Hashmap.keys() :
		#print("CHECKING FOR...", x)
		check = False
		count = Hashmap[x]
		change = 0
		if x^X in Hashmap.keys() and X != 0:
			count += Hashmap[(x^X)]
			#print("count in this case...", count)
			change += Hashmap[x]
			#print("REQ CHANGE", change)
			
		#print(max_count, count)
		if count > max_count :
			#print("min_change", min_change)
			max_count = count
			min_change = change 

		if count == max_count:
			min_change = min(min_change, change)

				

	print(max_count, min_change)