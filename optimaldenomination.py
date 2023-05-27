def gcd(a, b) :
	if a == 0 :
		return b
	if b == 0 :
		return a
	if a > b :
		a = a%b	
	else :
		b = b%a 
	gcd(a, b)

T = int(input())

for i in range(T):
	N = int(input())
	arr = [int(x) for x in input().split()]
	add = arr[0] + arr[1]
	HCF = gcd(arr[0], arr[1])
	for i in range(2, N) :
		add += arr[i]
		HCF = gcd(HCF, arr[i])

	print(add//HCF)

