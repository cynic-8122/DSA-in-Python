def check(string, pointer):
	i = pointer - 1
	j = pointer + 1

	while i >= 0 and j < len(string):
		if string[i] == string[j]:
			i -= 1
			j += 1

		else :
			break

	tempans = j - i 

	k = pointer - 1
	l = pointer

	while k >= 0 and l < len(string):
		if string[k] == string[l]:
			l += 1
			k -= 1

		else:
			break

	tempans2 = l - k 

	if tempans > tempans2 :
		return [i+1, j-1], tempans 

	else :
		return [k+1, l-1], tempans2 

def longestPalindromicSubstring(s):
	ans = -float('inf')
	idx = []
	for i in range(len(s)):
		tempidx, tempans = check(s, i)
		if tempans > ans :
			ans = tempans
			idx = tempidx 

	return s[(idx[0]):(idx[1] + 1)]

string = str(input())
print(longestPalindromicSubstring(string))


