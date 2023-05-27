def getallsubsequences(string):
	if len(string) == 0 :
		return [""]

	arr = getallsubsequences(string[1:])
	currentelement = string[0]
	for i in range(len(arr)):
		temp = arr[i]
		arr.append(currentelement + temp)

	return arr 

string = str(input())
print(getallsubsequences(string))
