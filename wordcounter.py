words = {}
letters = {}

string = input() #Input laina ja kive krna tu dekli
string.lower() # Lowercase vich convert ni ho rhe check krli

for i in range(len(string)) :
	if string[i] in letters :
		letters[string[i]] += 1
	else :
		letters[string[i]] = 1

arr = list(map(str, string.split()))
for i in range(len(arr)) :
	if arr[i] in words :
		words[arr[i]] += 1
	else :
		words[arr[i]] = 1


for x in letters.keys() :
	print(f"letters ({x}, {letters[x]}) ")

for y in words.keys() :
	print(f"words ({y}, {words[y]})")