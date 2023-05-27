
def permutation(string):
	if len(string) == 0:
		return []

	if len(string) == 1:
		return [string[0]]

	temparr = permutation(string[1:])
	currentchar = string[0]
	newarr = []
	for x in temparr:
		spaces = len(x) + 1
		i = 0
		while i < spaces:
			p = x[:i] + currentchar + x[(i):]
			newarr.append(p)
			i += 1

	return newarr

string = str(input())
print(permutation(string))