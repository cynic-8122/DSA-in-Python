
def Subsequences(string, arr = []):
	if len(string) == 0 :
		arr.append("")
		return arr

	arr = Subsequences(string[1:], arr)
	for x in arr :
		temp = string[0] + x
		arr.append(temp)

	return arr

string = str(input())
print(Subsequences(string))