
def checkAB(string, startwitha = False):
	if len(string) == 0 :
		return True

	if string[0] == 'a':
		return checkAB(string[1:], True)

	if string[0] == 'b' and string[1] == 'b' and startwitha :
		return checkAB(string[2:], False) 

	else :
		return False


string = str(input())
print(checkAB(string))

