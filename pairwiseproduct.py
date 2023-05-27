n = int(input())
arr = []

for i in range(n):
	a = int(input())
	arr.append(a)

pairprod = 0

for i in range(1, n) :
	x = sum(arr[:i])
	product = (arr[i])*x
	pairprod += product 

print(2)
print(pairprod)





