'''
Given an array of size n with all elements b/w 1 to n and one element which occurs twice and one which is missing. 
Find the missing and duplicate element without using any extra memory.
'''
N = int(input())

arr = [int(x) for x in input().split()]

xor = 0
arr_xor = 0
for i in range(N) :
	xor ^= (i + 1)
	arr_xor ^= arr[i]

val_xor = arr_xor^xor 
rsb = val_xor & (-val_xor)
a = val_xor
for i in range(N):
	if rsb&arr[i] :
		a ^= arr[i]

	if rsb&(i + 1):
		a ^= (i + 1)

b = a^val_xor

for i in range(N):
	if a == arr[i] :
		print("Duplicate value ", a)
		print("Missing value ", b)
		break

	if b == arr[i]:
		print("Duplicate value ", b)
		print("Missing value ", a)
		break


