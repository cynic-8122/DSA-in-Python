def replace_occurences(S, a, b, i = 0) :
	l = len(S)
	if i == len(S):
		return ""

	x = replace_occurences(S, a, b, i + 1)
	if S[i] == a :
		x = b + x

	else :
		x = S[i] + x

	return x

S = str(input())
a = str(input())
b = str(input())
print(replace_occurences(S, a, b))


