def maximumPower(S, N):
	prefixarr = []
	suffixarr = [[0, 0] for i in range(N)]
	onesofar = 0 
	zerosofar = 0
	for i in range(N):
		if S[i] == '0':
			zerosofar += 1

		else:
			onesofar += 1

		prefixarr.append([zerosofar, onesofar])


	zerosofar = 0
	onesofar = 0
	for i in range(N-1, -1, -1):
		if S[i] == '0':
			zerosofar += 1

		else:
			onesofar += 1

		suffixarr[i][0] = zerosofar if S[i] == '1' else zerosofar - 1
		suffixarr[i][1] = onesofar if S[i] == '0' else onesofar-1


	ans = -float('inf')

	for i in range(N):
		tempans1 = prefixarr[i][0] + suffixarr[i][1]
		tempans2 = prefixarr[i][1] + suffixarr[i][0]
		ans = max(ans, tempans1, tempans2)

	return ans


