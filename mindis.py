arr = list(map(int, input().split()))

x = ""

b = 0

m = min(arr)
for i in range(0, len(arr)):
	a = arr[i] 
	a -= m
	a = str(a)
	x += arr[i]


darr = list(map(str, x.split("0")))
arr = darr

temp = arr[b]

temp_lnth = len(temp)





