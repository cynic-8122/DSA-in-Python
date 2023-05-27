def remove_x(S, i = 0) :
	l = len(S)
	if i == len(S) :
		return ""

	x = remove_x(S, i + 1)

	if S[i] == "x" :
		return x 

	else :
		return S[i] + x 

S = str(input())
print(remove_x(S))