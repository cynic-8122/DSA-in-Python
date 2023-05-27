n = int(input("Give a positive integer as an Input "))

if n==1: 
	print ("0")
	exit("")

elif n>=2:

	i = 2
	while i**2 <= n:
		if n%i==0 : 
			print("0")
			exit()

		else:
			i+=1

print("1")