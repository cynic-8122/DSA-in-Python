def getOneBits(n):
	t = bin(n)
	t = str(t)
	t = t[2:]
	count = 0
	for i in range(len(t)):
		if t[i] == "1":
			count += 1

	ansarr = [count]

	for j in range(len(t)):
		if t[j] == '1':
			ansarr.append(j+1)

	return ansarr

n = int(input())
print(*getOneBits(n))