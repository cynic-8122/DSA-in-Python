S = input("Enter any word ")
def wordPrinter(S, start, end = (len(S) - 1)) :
	j = 0
	for i in range(start, (end + 1)) :
		x = S[(end - j):(end + 1)]
		print(x)
		j += 1

	return

start = int(input("Start "))
end = input("End ")

if end == "" :
	wordPrinter(S, start)
	
else :
	end = int(end)

	if (start < 0) or (end >= len(S)) or (start > end) :
		print("____________________________________________Be careful bitch____________________________________________")

	else :
			wordPrinter(S, start, end)






