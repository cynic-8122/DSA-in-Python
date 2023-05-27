def print_n_numbers(n):
	if n == 0 :
		return 
	print_n_numbers(n - 1)
	print(n)

def print_n_reversed(n):
	
	if n == 0 :
		return 
	print(n) 
	x = print_n_reversed(n-1)
	

n = int(input())
print_n_numbers(n)
print_n_reversed(n)