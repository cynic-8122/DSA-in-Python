
def staircase(n):
	prev = 1
	prev2 = 1

	i = 2
	while i <= n:
		t = prev + prev2
		prev2 = prev 
		prev = t 
		i += 1

	return prev 

n = int(input())

print(staircase(n))