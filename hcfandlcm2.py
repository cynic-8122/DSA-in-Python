a, b = input().split(" ")

a = int(a)
b = int(b)

if a > b :
	c = b

else :
	c = a


while c >= 1 :
	if a % c == 0 and b % c == 0 :
		hcf = c
		break


	else :
		c -= 1


lcm = (a*b)//hcf
print (hcf , end = " ")
print (lcm)


