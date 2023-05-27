'''
Given two strings (of same length), you have to check if you can convert str1 to str2 using one or more conversions.
In a conversion you can convert all the occurances of a character in str1 to any other character.
'''
N = int(input("Length of the string "))

str1 = input()
str2 = input()

Hashmap = {}
for i in range(N):
	if str1[i] in Hashmap.keys() :
		Hashmap[str1[i]].append(i)

	else:
		Hashmap[str1[i]] = [i]

flag = False
for x in Hashmap.keys() :
	diff = ord(x) - ord(str2[Hashmap[x][0]])
	for i in range(1, len(Hashmap[x])):
		temp = ord(x) - ord(str2[Hashmap[x][i]])
		if temp != diff :
			flag = True
			break

if flag :
	print("NO")

else:
	print("YES")

