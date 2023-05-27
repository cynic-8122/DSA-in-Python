

print('''Incase you wish to use the default value for 'City' or 'Postal Code' :
Just press enter when you're asked for their respective inputs
 ''')
a = input("Enter your Street Number \n")
b = input("Enter the name of your Street \n")
c = input("Enter your City \n")
d = input("Enter you Postal Code \n")

def addressformatter(a, b, c = "Wolfville", d = "B4P 2R6") :

	x = a + " " + b + "\n" + c + " " + d
	 
	return x 

if c != "" and d != "" :

	print(addressformatter(a = a, b = b, c = c , d = d ))

else :
	print(addressformatter(a = a, b = b))




