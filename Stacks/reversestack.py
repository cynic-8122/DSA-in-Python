class Stack :
	def __init__(self):
		self.__arr = []
		self.__count = 0

	def size(self):
		return self.__count

	def push(self, val):
		self.__count += 1
		self.__arr.append(val)

	def pop(self):
		if self.isEmpty() :
			print("Invalid command")
			return
		self.__count -= 1
		return self.__arr.pop()

	def isEmpty(self):
		return self.__count == 0

	def top(self):
		if self.isEmpty :
			print("Stack is Empty")
			return

		return self.__arr[-1]

N = int(input())
arr = [int(x) for x in input().split()]
S1 = Stack()
S2 = Stack()
for i in range(N):
	t = arr[i]
	S1.push(t)

def reverseStack(S1, S2):
	#print("Size", S1.size())
	if S1.isEmpty() :
		return
	if S1.size() == 1 :
		return S1

	if S1.size() == 2 :
		S2.push(S1.pop())
		t = S1.pop()
		S1.push(S2.pop())
		S1.push(t)

		return S1
	S2.push(S1.pop())
	S1 = reverseStack(S1 , S2)
	p = S2.pop()
	count = 0
	while not S1.isEmpty() :
		count += 1
		S2.push(S1.pop())

	S1.push(p)

	while count and not S2.isEmpty():
		S1.push(S2.pop())
		count -= 1

	return S1 

S1 = reverseStack(S1, S2)

while not S1.isEmpty() :
	print(S1.pop())










