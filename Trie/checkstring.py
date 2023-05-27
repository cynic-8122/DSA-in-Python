import sys
sys.setrecursionlimit(10**5)

def stringchecker(string):
	if len(string) == 0:
		return True

	if len(string) == 1:
		if string[0] == '1' or string[0] == '2':
			return True

		else:
			return False


	if string[0] == '1':
		return stringchecker(string[1:])


	if string[0] == '2':
		if len(string) > 2 and string[1] == '2' and string[2] == '1':
			return stringchecker(string[3:])

		else:
			return False


	#return False

T = int(input())
for i in range(T):
	N = int(input())
	S = input()

	if len(S) == 0:
		print('NO')
		continue


	ans = stringchecker(S)

	if ans:
		print('YES')

	else:
		print('NO')




