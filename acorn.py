n = input("ENTER YOUR NAME \n")

a = input("DO you have fever? \n")

b = input("DO you have a cough (new or worsening)? \n")

if a == "y" or b == "y" :
	print(n, end = "")
	print(", you should stay at home and call 811 to schedule a test.")
	exit()

number_of_y = 0
if a == "n" and b == "n" :
	c = input("Do you have a headache? \n")
	if c == "y" :
		number_of_y += 1

	d = input("Do you have a sore throat? \n")
	if d == "y" :
		number_of_y += 1

	e = input("Do you have a runny nose / nasal congestion? \n")
	if e == "y" :
		number_of_y += 1

	f = input("Do you have shortness of breath? \n")
	if f == "y" :
		number_of_y += 1

	if number_of_y == 0 :
		print(n, end = "")
		print(", you should come to class.")
		

	elif number_of_y == 1 :
		print(n, end = "")
		print(", you should stay home.")

	else :
		print(n, end = "")
		print(", you should stay at home and call 811 to schedule a test.")

else :
	print("INVALID INPUT \n USE ONLY (y/n) TO RESPOND ")

