n = int(input("Number of inputs you need to record "))

i = 1
arr = list(map(int, input().split(" ")))

j = 1
while j <= len(arr) :
	print (arr[-j] , end = " ")
	j += 1



