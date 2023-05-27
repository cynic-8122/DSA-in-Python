N = int(input("NUMBER OF LINES YOU NEED TO INPUT "))


i = 1
larr = []

while i <= N :
	line = input()
	larr.append(line)
	i += 1

a = len(larr)
i = 0
wlarr = []
allwarr = []


while i < a :
	b = larr[i]
	warr = list(map(str, b.split(" ")))
	words_in_line = len(warr)
	j = 0
	while j < words_in_line :
		c = warr[j]
		allwarr.append(c)
		j += 1

	wlarr.append(words_in_line)
	words_in_line = 0
	i += 1

replace = input("WHICH WORD DO YOU WANT TO REPLACE ")
replace_with = input("ENTER THE WORD WITH WHICH YOU WANT TO REPLACE THE SELECTED WORD ")
p = 0
o = len(allwarr)

if replace in allwarr :
	while p < o :
		if allwarr[p] == replace :
			x = allwarr.index(replace)
			allwarr.remove(replace)
			allwarr.insert(x, replace_with)
			
		p += 1

else :
	print("INVALID INPUT")
	exit()



i = 0
j = 0
k = 0
while i < N :
	m = wlarr[i]
	while j < (m + k) :
		print(allwarr[(j)], end = " ")
		j += 1

	print("")
	k = (j)
	i += 1
	


















	





 




