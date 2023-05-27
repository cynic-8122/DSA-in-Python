arr = list(map(str, input().split()))
k = int(input())
Hashmap = {}

for x in arr :
	if x in Hashmap.keys() :
		Hashmap[x] += 1
	else :
		Hashmap[x] = 1

def wordswithfrequencyk(k):
	ansarr = []
	for x in Hashmap.keys() :
		if Hashmap[x] == k :
			ansarr.append(x)

	return ansarr

print(*wordswithfrequencyk(k))

for x in Hashmap.keys():
	if x == "the" :
		Hashmap["The"] = Hashmap[x]
		Hashmap.pop(x)

print(Hashmap)
