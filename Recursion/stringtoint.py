def str_to_int(S) :
	l = len(S)
	if l == 0 or l == 1 :
		return S 

	if S[0] == "0" :
		smallerstr = S[1:]
		return str_to_int(smallerstr)

	else :
		return S

S = str(input())
print(str_to_int(S))