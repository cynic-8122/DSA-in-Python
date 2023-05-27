def pair_star(S):
	l = len(S)
	if len(S) == 0 or len(S) == 1 :
		return S 

	smallerstr = S[1:]

	if S[0] == S[1] :
		return S[0] + "*" + pair_star(smallerstr)

	else :
		return S[0] + pair_star(smallerstr)

S = str(input())
print(pair_star(S))