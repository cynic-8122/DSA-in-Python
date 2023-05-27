def remove_duplicates(S, i = 0):
	l = len(S)
	if i == len(S) :
		return ""

	x = remove_duplicates(S, i + 1)
	if i >= 1 and S[i] == S[i - 1] :
		return x 

	else :
		return S[i] + x 

S = str(input())
print(remove_duplicates(S)) 

	
