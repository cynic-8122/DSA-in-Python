
string = str(input())
target = str(input())

def pitable(target):
	n = len(target)
	pi = [-1]*n 

	j = 0
	i = 1
	while i < n:
		if target[i] == target[j]:
			pi[i] = j
			i += 1
			j += 1
		
		else:
			if j == 0:
				i += 1

			else:
				j = pi[j-1] + 1
				continue

	return pi 

pi = pitable(target)
i = 0
j = 0


while i < len(string) and j < len(target):
	if string[i] == target[j]:
		i += 1
		j += 1

	else:
		if j == 0:
			i += 1

		else:
			j = pi[j-1]+1
			continue


if j >= len(target):
	print(True)

else:
	print(Falset)



