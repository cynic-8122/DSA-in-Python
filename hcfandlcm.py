a, b = input().split(" ")

print("good so far")

a = int(a)
b = int(b)

print("good so far")

if a > b :
	c = b
	print("good so far")
	while c >= 1 :

		print("good so far")
	
		if a%c == 0 :
			m = c # m is the HCF of the two 
			print("good so far")

		else :
			c -= 1
			print("good so far")



	n = (a*b)/m # n is the LCM of two numbers
	print (m , end = " " )
	print (n)

else :
	c = a

	while c >= 1 :
		if b%c == 0:
			m = c # m is the HCF of the two numbers

		else :
			c -= 1


	n = (a*b)/m # n is the LCM of two numbers
	print (m , end = " " )
	print (n)