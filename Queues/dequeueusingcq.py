class circularqueue :
	def __init__(self, maxsize):
		self.maxsize = maxsize
		self.count = 0
		self.arr = [None]*(self.maxsize)
		self.front = -1
		self.rear = -1

	def enqueue(self, val):
		if self.count >= self.maxsize :
			print("QUEUE IS FULL ALREADY ")
			return

		self.count += 1
		if self.front == -1 :
			self.arr[0] = val
			self.front = 0
			self.rear = 0
			return

		self.rear =  (self.rear + 1)%self.maxsize
		self.arr[self.rear] = val


	def dequeue(self):
		if self.count == 0 :
			print("INVALID COMMAND \nQUEUE IS EMPTY ")
			self.front = self.rear = -1
			return

		self.count -= 1
		temp = self.arr[self.front]
		self.arr[self.front] = None
		self.front += 1

		return temp

	def isEmpty(self):
		return self.count == 0

	def isFull(self):
		return self.count == self.maxsize

	def size(self) :
		return self.count

	def getfront(self):
		if self.isEmpty() :
			print("QUEUE IS EMPTY ")
			return

		print(self.arr[self.front])

	def getrear(self):
		if self.isEmpty() :
			print("QUEUE IS EMPTY ")
			return

		#print("rear at", self.rear)
		print(self.arr[self.rear])

class Dequeue(circularqueue) :
	def __init__(self, maxsize):
		super().__init__(maxsize)

	def enqueueleft(self, val):
		if self.count >= self.maxsize :
			print("QUEUE IS FULL ALREADY ")
			return

		self.count += 1

		if self.count == 0 :
				super().enqueue(val)

		
		self.front = (self.front - 1)%self.maxsize
		self.arr[self.front] = val

	def dequeueright(self):
		if self.count == 0 :
			print("QUEUE IS EMPTY")
			self.front = self.rear = -1
			return

		self.count -= 1
		temp = self.arr[self.rear]
		#print("rear at", self.rear)
		self.rear = (self.rear - 1)%self.maxsize
		return temp
		

D = Dequeue(7)
D.enqueue(3)
D.enqueue(4)
D.enqueueleft(2)
print("SIZE", D.size())
print("IS THE QUEUE EMPTY ?", D.isEmpty())
print("FRONT ELEMENT OF THE QUEUE IS :", end = ' ')
D.getfront()
D.enqueueleft(1)
D.enqueue(5)
print("REAR EMENENT OF THE QUEUE IS :" , end = ' ')
D.getrear()
D.enqueue(6)
D.enqueue(7)
print("IS THE QUEUE FULL ?", D.isFull())
print(D.dequeue())
print("FRONT ELEMENT OF THE QUEUE IS :", end = ' ')
D.getfront()
print(D.dequeueright())
print("REAR EMENENT OF THE QUEUE IS :" , end = ' ')
D.getrear()











