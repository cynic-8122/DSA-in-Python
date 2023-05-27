def printname(name, count = 5):
	if count == 0:
		return

	print(name)
	printname(name, count-1)

name = str(input('Enter the name\n'))

printname(name)