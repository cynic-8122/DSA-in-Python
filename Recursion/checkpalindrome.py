def check_palindrome(S):
	l = len(S)
	#print(S)
	if l == 0 or l == 1 :
		return True

	elif S[0] != S[len(S) - 1] :
		return False

	
	smallerstring = S[1:(len(S) - 1)]
	return check_palindrome(smallerstring)

	

S = str(input())
print(check_palindrome(S))