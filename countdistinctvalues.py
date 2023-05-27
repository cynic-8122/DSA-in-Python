n = int(input())

dinstinct_values = 0
arr = []
for i in range(n) :
	a = int(input())
	
	if not(a in arr) :
		dinstinct_values += 1

	arr.append(a)

print(2)
print(dinstinct_values)



