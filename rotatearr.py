arr = [int(x) for x in input().split()]

d = int(input())

def rotLeft(a, d):
    
	pointer_at = 0
	for i in range(len(a)):		
		swap_val = (pointer_at - d)%(len(a))
		a[swap_val], a[0] = a[0], a[swap_val]
		print(a)
		pointer_at = swap_val       
    
	return a

print(rotLeft(arr, d))
