n=int(input())
for i in range(1,n): 
	n-=i
	if n<=0:
		print("Patlu") 
		break
	n-=i*2 
	if n<=0:
		print("Motu") 
		break
