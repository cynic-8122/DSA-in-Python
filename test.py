while True :
	a = int(input())
	b = int(input())
	c = int(input())
	d = int(input())
	if (a|b|c^a|d) == (b|c|d) :
		print("Worked for this case")
		continue

	else :
		print("Didn't work for this case")
		break