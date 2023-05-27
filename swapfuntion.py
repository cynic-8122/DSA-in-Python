x = int(input())
y = int(input())

print(x, y)

def swap(x, y) :
	
	x = x + y
	y = x - y
	x = x - y
	return x, y

print(swap(x, y))
