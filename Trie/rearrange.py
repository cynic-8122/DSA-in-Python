def Rearrange(n):
	string = str(n)
	ans = 0
	for i in range(0, len(string), 2):
		val = int(string[i])
		ans = 10*ans + val

	return ans

