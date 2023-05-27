'''
Suppose you have a string, S, made up of only 'a's and 'b's. 
Write a recursive function that checks if the string was generated using the following rules:
a. The string begins with an 'a'
b. Each 'a' is followed by nothing or an 'a' or "bb"
c. Each "bb" is followed by nothing or an 'a'
If all the rules are followed by the given string, return true otherwise return false.
Input format :
String S
Output format :
'true' or 'false'
'''
def check_AB(S):
	print(S)
	l = len(S)
	if len(S) == 0 :
		return True

	if S[0] != 'a':
		return False

	if len(S) >= 3 and S[0] == 'a' and S[1] == 'b' and S[2] == 'b' :
		smallerstr = S[3:]
		return check_AB(smallerstr)

	elif S[0] == 'a':
		smallerstr = S[1:]
		return check_AB(smallerstr)

S = str(input())
print(check_AB(S))



