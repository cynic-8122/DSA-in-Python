def getallsubsequences(string):
	if len(string) == 0 :
		arr = ['']
		return arr

	temparr = getallsubsequences(string[1:])
	arr = []
	for x in temparr :
		arr.append(x)
		arr.append(string[0] + x)

	return arr

string = str(input())
print(getallsubsequences(string))