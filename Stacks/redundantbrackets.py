class Stack :
	def __init__(self):
		self.__arr = []
		self.__count = 0

	def push(self, val):
		self.__count += 1
		self.__arr.append(val)

	def isEmpty(self):
		return self.__count == 0

	def size(self):
		return self.__count

	def pop(self):
		if self.isEmpty() :
			return

		self.__count -= 1

		return self.__arr.pop()

	def top(self):
		if self.isEmpty() :
			return

		return self.__arr[-1]


a = str(input())
S = Stack()
count = 0
check = False
for i in range(len(a)) :
	t = a[i]
	if t == "+" or t == "*" or t == "-" or t == "/":
		check = True

	if t == "(" or t == "[" or t == "{" :
		S.push(t)

	elif t == ")" and S.top() == "(" and check :
		check = False
		S.pop()
		count = 0

	elif t == "}" and S.top() == "{" and check :
		check = False
		S.pop()
		count = 0

	elif  t == "]" and S.top() == "[" and check :
		check = False
		S.pop()
		count = 0


if S.isEmpty() :
	print(False)

else :
	print(True)
