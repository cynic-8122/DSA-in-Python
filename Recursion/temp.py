import random
arr = [int(x) for x in input().split()]
l = 0
r = len(arr) - 1

x =  random.choice(arr[l:(r + 1)])
print(f"x = {x}")
idx = arr.index(x)
count = 0
for i in range(l, r + 1) :
	if arr[i] <= x :
		count += 1

	#idx = arr.index(x)
count -= 1
print(count)
arr[count], arr[idx] = arr[idx], arr[count]
print(arr)
i = l 
j = r 
while i < count and j > count :
	check1 = False
	check2 = False
	if arr[i] > x :
		check1 = True
	if arr[j] <= x :
		check2 = True 

	if check1 and check2 :
		arr[i] , arr[j] = arr[j], arr[i]
		i += 1
		j -= 1
	elif check1 :
		j -= 1

	elif check2 :
		i += 1

	else :
		i += 1
		j -= 1


print(arr)