'''

Chandanpreet Singh
SID : 20104060
VALID PARENTHESES

'''
class Stack():
	def __init__ (self):
		self.arr = []

	def top(self, S):
		if len(self.arr) == 0 :
			return None

		else:
			return self.arr[-1]

	def pop(self, S):
		N = len(self.arr)
		temp = self.arr[-1]
		self.arr = self.arr[:(N - 1)]
		return temp

	def push(self, S, val):
		return self.arr.append(val)

	def isEmpty(self, S):
		return len(self.arr) == 0


A = Stack()
p = str(input("Enter the string "))
count = 0 # Using count we will check if no. of opening parenthesis are equal to no. of closing parenthesis

'''
Algorithm : 
As we get an opening parenthesis we add it into the Stack .
As we get a closing parenthesis we pop the top element from the Stack while checking if is it the correct one.
At the last if the Stack is empty we know the parenthesis is valid.
'''
for i in range(len(p)):
	if p[i] == "[" or p[i] == "{" or p[i] == "(" :
		count += 1
		A.push(A, p[i])

	elif p[i] == "]" or p[i] == "}" or p[i] == ")" :
		count -= 1
		if p[i] == "]" and A.top(A) == "[" :
			A.pop(A)

		elif p[i] == "}" and A.top(A) == "{" :
			A.pop(A)

		elif p[i] == ")" and A.top(A) == "(" :
			A.pop(A)

print(A.isEmpty(A) and not count)


