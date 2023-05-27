
def power(a, b):
	if b == 0:
		return 1

	if b == 1:
		return a 

	if b&1:
		t = power(a, b//2)
		return (t*t*a)

	else:
		t = power(a, b//2)
		return (t*t) 

a = int(input())
b = int(input())

print(power(a, b))