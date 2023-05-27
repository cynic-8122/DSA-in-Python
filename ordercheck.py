n = int(input())

arr = list(map(int, input().split()))

def ordercheck(n, arr):
	a = 1
	if n == 0 :
		 
		return arr[n]

	x = ordercheck(n - 1, arr)
	y = arr[n]
	if y > x :
		return y
	
	
	
	

