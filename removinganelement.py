arr = list(map(int,input().split()))

i = 0 
b = len(arr)


while i < len(arr) :
	a = min(arr)
	arr.remove(a)
	print(arr)
	i += 1

