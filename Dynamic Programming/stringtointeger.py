def stringtointeger(string, check = False):
	if len(string) == 0 :
		return 0

	if string[0] == "0" :
		return stringtointeger(string[1:], check)

	elif string[0] != '0' :
		check = True
		return int(string[0])*(10**(len(string) - 1)) + stringtointeger(string[1:], check)

string = str(input())
print(stringtointeger(string))

