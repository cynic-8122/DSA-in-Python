Hashmap = {}
Hashmap['2'] = ['a', 'b', 'c']
Hashmap['3'] = ['d', 'e', 'f']
Hashmap['4'] = ['g', 'h', 'i']
Hashmap['5'] = ['j', 'k', 'l']
Hashmap['6'] = ['m', 'n', 'o']
Hashmap['7'] = ['p', 'q', 'r', 's']
Hashmap['8'] = ['t', 'u', 'v']
Hashmap['9'] = ['w', 'x', 'y', 'z']

def printallkeypadcombinations(num, ans = ""):
	if len(num) == 0 :
		print(ans)
		return

	for x in Hashmap[num[0]]:
		printallkeypadcombinations(num[1:], ans+x)


num = str(input())

printallkeypadcombinations(num)
