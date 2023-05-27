def pairstar(string, prev = None):
	if len(string) == 0 :
		return ""

	temp = pairstar(string[1:], string[0])

	if prev == None :
		return string[0] + temp

	if string[0] == prev :
		return "*" + string[0] + temp

	else:
		return string[0] + temp

string = str(input())

print(pairstar(string))