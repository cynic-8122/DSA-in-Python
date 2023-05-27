'''
def checkelement(arr, element, i = 0):
	if i >= len(arr):
		return -1

	if arr[i] == element :
		return i 

	return checkelement(arr, element, i + 1)


arr = [int(x) for x in input().split()]
element = int(input())

print(checkelement(arr, element))

def LastIndex(arr, element, i = 0):
	if i >= len(arr):
		return -1

	ans = LastIndex(arr, element, i + 1)

	if ans == -1 and arr[i] == element :
		ans = i 

	return ans


print(LastIndex(arr, element))
'''
def power(a, b):
	if b == 0 :
		return 1

	if b&1 :
		return power(a, b//2)*power(a, b//2)*a 

	else :
		return power(a, b//2)*power(a, b//2)

a, b = [int(x) for x in input().split()]

print(power(a, b))