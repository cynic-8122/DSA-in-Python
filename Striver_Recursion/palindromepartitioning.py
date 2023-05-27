
def palindromepartitioning(string, ansarr, temparr):
	if len(string) == 0:
		t = list(temparr)
		ansarr.append(t)
		return

	
	for i in range(1, len(string) + 1):
		temp = string[:i]
		if check(temp):
			temparr.append(temp)
			palindromepartitioning(string[i:], ansarr, temparr)
			temparr.pop()

		

def check(string):
	i = 0
	j = len(string) - 1
	while i <= j:
		if string[i] != string[j]:
			return False

		i += 1
		j -= 1 

	return True

ansarr = []
temparr = []
string = str(input())
palindromepartitioning(string, ansarr, temparr)
print(ansarr)


