def replace_pi(S, i = 0):
	l = len(S)
	if i >= len(S) :
		return ""

	x = replace_pi(S, i + 1)
	if i >= 1 and S[i] == "i" and S[i - 1] == "p" :
		return "3.14" + x 

	elif i < len(S) - 1 and S[i] == "p" and S[i + 1] == "i" :
		return x
	else :
		return S[i] + x

S = str(input())
print(replace_pi(S))



