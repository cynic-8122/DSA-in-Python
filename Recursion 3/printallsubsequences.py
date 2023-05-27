
def printallsubsequences(string, ans = ""):
	if len(string) == 0 :
		print(ans)
		return

	printallsubsequences(string[1:], ans)
	printallsubsequences(string[1:], ans + string[0])

string = str(input())
printallsubsequences(string)