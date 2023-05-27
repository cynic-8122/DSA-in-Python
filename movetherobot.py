T = int(input())

for i in range(T) :
	x1, y1, x2, y2 = input().split()
	x1 = int(x1)
	y1 = int(y1)
	x2 = int(x2)
	y2 = int(y2)
	no_of_moves = abs(x2 - x1) + abs(y2 - y1)
	output = ""
	while x1 != x2 :
		if x2 > x1 :
			x1 += 1
			output += "E"

		else :
			x1 -= 1
			output += "W"

	while y1 != y2 :
		if y2 > y1 :
			y1 += 1
			output += "N"

		else :
			y1 -= 1
			output += "S"

	print(no_of_moves)
	print(output)
