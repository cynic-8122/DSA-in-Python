
def replacepi(string):
	if len(string) == 0:
		return ""

	if string[0] == "p" and string[1] == 'i' :
		return "3.14" + replacepi(string[2:])

	else :
		return string[0] + replacepi(string[1:])


string = str(input())

print(replacepi(string))