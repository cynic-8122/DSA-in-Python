arr = [int(x) for x in input().split()]

X = int(input())

Hashmap = {}

for x in arr :
	Hashmap[x] = Hashmap.get(x, 0)+1

Check = False
for x in Hashmap.keys() :
	if X - x in Hashmap.keys() :
		ansarr = [x, X-x]
		Check = True
		break

if Check:
	print("YES")
	print(*ansarr)

else :
	print('NO')