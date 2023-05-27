class Queue :
	def __init__(self):
		self.__arr = []
		self.__count = 0
		self.__front = None

	def enqueue(self, val):
		'''
		if self.__count >= maxsize :
			print("Queue is Full ")
			return
		'''

		self.__arr.append(val)
		if self.__count == 0 :
			self.__front = 0

		self.__count += 1

	def dequeue(self):
		if self.__count <= 0 :
			print("INVALID COMMAND ")
			return

		self.__count -= 1
		self.__front += 1
		return self.__arr[self.__front - 1]

	def size(self):
		return self.__count

	def isEmpty(self):
		return self.size() == 0

	def front(self):
		if self.__count == 0 :
			print("QUEUE IS EMPTY ")
			return
		return self.__arr[self.__front]

	def rear(self):
		if self.__count == 0 :
			print("QUEUE IS EMPTY ")
			return
		return self.__arr[-1]

	def reverse(self):
		if self.isEmpty() :
			return

		t = self.dequeue()
		#print(t)
		self.reverse()
		print(t)
		self.enqueue(t)
		print(self.__arr)

N = int(input())
arr = [int(x) for x in input().split()]
Q = Queue()
for x in arr :
	Q.enqueue(x)

Q.reverse()
for i in range(len(arr)) :
	print(Q.dequeue())





