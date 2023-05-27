
def allpartitions(string, ansarr):
	if len(string) == 0:
		return

	if len(string) == 1:
		t = [string]
		ansarr.append(t)
		return ansarr

	temparr = allpartitions(string[1:], ansarr)

	ele = string[0]
	ansarr = []
	for x in temparr:
		t1 = list(x) 
		t1[0] = str(ele)+str(t1[0])

		x.insert(0, ele)
		ansarr.append(x)
		ansarr.append(t1)

	return ansarr

string = str(input())

print(allpartitions(string, []))