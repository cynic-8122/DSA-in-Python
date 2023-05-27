
string1 = str(input())
string2 = str(input())

def LCS(string1, string2):
	if len(string1) == 0 or len(string2) == 0:
		return 0

	ans1 = -float('inf')
	if string1[0] == string2[0]:
		ans1 = 1 + LCS(string1[1:], string2[1:])

	ans2 = max(LCS(string1[1:], string2), LCS(string1, string2[1:]))

	return max(ans1, ans2)

print(LCS(string1, string2))
