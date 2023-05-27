
def lcsubstr(str1, str2, check = False):
	if len(str1) == 0 or len(str2) == 0:
		return 0

	if check:
		if str1[0] == str2[0]:
			ans1 = 1 + lcsubstr(str1[1:], str2[1:], True)
			if len(str1) > 1 and len(str2) > 1:
				check = False

			else:
				return ans1

		else:
			return 0


	if check == False:
		ans2 = ans3 = ans4 = 0
		if str1[0] == str2[0] :
			ans2 = 1 + lcsubstr(str1[1:], str2[1:], True)
			if len(str1) > 1 and len(str2) > 1:
				str1 = str1[1:]
				str2 = str2[1:]

		if str1[0] != str2[0]:
			ans3 = lcsubstr(str1[1:], str2, False)
			ans4 = lcsubstr(str1, str2[1:], False)

		return max(ans2, ans3, ans4)

str1 = str(input('Enter first string '))
str2 = str(input('Enter second string '))

print(lcsubstr(str1, str2))
