n, m = [int(x) for x in input().split()]

count= [0]
def number_of_ways(n, m) :
	if n == 0 and m == 0 :
		count[0] += 1
		return
	if n < 0 or m < 0 :
		return
	number_of_ways(n - 1, m)
	number_of_ways(n, m - 1)

number_of_ways(n - 1, m - 1)
print(count[0])