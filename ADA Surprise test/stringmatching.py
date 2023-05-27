def stringmatching(string1, string2):
	if len(string1) != len(string2):
		return 0

	for i in range(len(string1)):
		if string1[i] != string2[i]:
			return 0

	return 1

string1 = str(input())
string2 = str(input())

ans = stringmatching(string1, string2)

if ans:
	print('Both the strings are same')

else :
	print("Both the stings are different")