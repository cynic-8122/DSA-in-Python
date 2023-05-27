
n = int(input())

arr = [True for i in range(n+1)]

arr[1] = False

i = 2
while i <= n:
	if arr[i] == True:
		j = i+i 
		while j <= n:
			arr[j] = False
			j += i 

	i += 1

print(arr)

