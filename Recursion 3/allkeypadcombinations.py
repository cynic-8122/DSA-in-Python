Hashmap = {}
Hashmap['2'] = ['a', 'b', 'c']
Hashmap['3'] = ['d', 'e', 'f']
Hashmap['4'] = ['g', 'h', 'i']
Hashmap['5'] = ['j', 'k', 'l']
Hashmap['6'] = ['m', 'n', 'o']
Hashmap['7'] = ['p', 'q', 'r', 's']
Hashmap['8'] = ['t', 'u', 'v']
Hashmap['9'] = ['w', 'x', 'y', 'z']

num = str(input())

def allcombinations(num):
	if len(num) == 0:
		return [""]

	arr = allcombinations(num[1:])
	newarr = []
	for x in arr :
		for y in Hashmap[num[0]]:
			newarr.append(y+x)

	return newarr

print(allcombinations(num))