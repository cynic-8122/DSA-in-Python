def sum_of_digits(N):
	if N//10 == 0 :
		return N 

	return (N%10) + sum_of_digits(N//10)

N  = int(input())
print(sum_of_digits(N))