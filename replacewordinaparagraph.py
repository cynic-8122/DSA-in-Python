N = int(input("NUMBER OF LINES YOU NEED TO INPUT "))


i = 1
larr = []# This list will have (i + 1)th line at its ith index

while i <= N :# Using this loop we take all the inputs
	line = input()
	larr.append(line)
	i += 1

a = len(larr)
i = 0
wlarr = [] # This list will contain the number of words in each line
allwarr = []# This list will contain all the words


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
while i < N :# Using this nested loop we print the updated paragraph
	m = wlarr[i]
	while j < (m + k) :
		print(allwarr[(j)], end = " ")
		j += 1

	print("")
	k = (j)
	i += 1
	
H = input("KINDLY ENTER THE WORD YOU NEED TO INSERT ")
I = input("CHOOSE THE WORD AFTER WHICH YOU WISH TO INSERT ")
print(wlarr)

if I in allwarr :
	i = 0
	ins = []
	while i < o :
		if allwarr[i] == I :
			ins.append(i)
			a = i + 1
			allwarr.insert(a, H)

		
		i += 1
	
	i = 0
	j = 0
	k = 0
	
	while (i < len(ins)) and (k < len(wlarr)) :
		a = wlarr[k]
		m = ins[i]
		print(f"ins = {ins}")


		if m < (a + j) :
			wlarr[k] += 1
			y = wlarr[k] 
			print(f"upadated value at i = {i} is {y}")
			

		else :
			j += a 
			k += 1
			
		i += 1
		print(f"k = {k}")
		print(f"m =  {m}")
		print(f"m = {m} and (a + j) = {a + j}")

	print(wlarr)
	print(allwarr)

	i = 0
	j = 0
	k = 0
	while i < N : # Using this nested loop we print the updated paragraph
		m = wlarr[i]
		while j < (m + k) :
			print(allwarr[(j)], end = " ")
			j += 1


		print("")
		k = (j)
		i += 1


			

		



















	





 




