import queue

S = queue.LifoQueue()

string = str(input())


def checkredundant(string):
	opcount = 0
	for i in range(len(string)) :
		t = string[i]
		if t == ")":
			p = S.get()
			while p != "(" :
				if p == "+" or p == "-" or p == "/" or p == "*" :
					opcount += 1

				p = S.get()

			if opcount == 0 :
				return False
			opcount = 0


		else :
			S.put(t)

	return True


print(checkredundant(string))
