
def permutation(string):
	if len(string) == 0:
		return ['']

	if len(string) == 1:
		return [string[0]]


	newarr = []
	for i in range(len(string)):
		currentchar = string[i]
		remainingstr = string[:i] + string[(i+1):]
		temparr = permutation(remainingstr)
		for x in temparr :
			p = currentchar + x
			newarr.append(p)

	return newarr


string = str(input())

print(permutation(string))