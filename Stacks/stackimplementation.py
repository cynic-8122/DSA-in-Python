class Stack():
	def __init__ (self, size):
		self.size = size
		self.arr = [None]*(size)
		self.count = 0

	def top(self, S):
		if len(self.arr) == 0 :
			return None

		else:
			return self.arr[-1]

	def pop(self, S):
		if self.count == 0 :
			print("INVALID COMMAND \nSTACK IS EMPTY ")
			return

		self.count -= 1
		temp = self.arr[self.count]
		self.arr = self.arr[:self.count]
		return temp

	def push(self, S, val):
		if self.count >= self.size :
			print("Stack is Full ")
			return

		self.count += 1
		self.arr[self.count - 1] = val
		

	def isEmpty(self, S):
		return self.count == 0

	def isFull(self, S):
		return self.count == self.size

A = Stack(5)
print('IS THE STACK EMPTY ?',A.isEmpty(A))
A.push(A, 1)
A.push(A, 2)
A.push(A, 3)
A.push(A, 4)
#print(A.arr)
print("ELEMENT POPPED OUT WAS : ", A.pop(A))
print("ELEMENT AT THE TOP IS : ", A.top(A))
print("ELEMENT POPPED OUT WAS : ", A.pop(A))
print("ELEMENT AT THE TOP IS : ", A.top(A))
print("ELEMENT POPPED OUT WAS : ", A.pop(A))
print("ELEMENT AT THE TOP IS : ", A.top(A))
print("IS THE STACK FULL ?", A.isFull(A))
print('IS THE STACK EMPTY ?', A.isEmpty(A))
print("ELEMENT POPPED OUT WAS : ", A.pop(A))
print('IS THE STACK EMPTY ?', A.isEmpty(A))
