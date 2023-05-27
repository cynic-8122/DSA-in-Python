class MinHeap :
	def __init__(self):
		self.__arr = []

	def insert(self, val):
		self.__arr.append(val)
		i = len(self.__arr) - 1
		while i :
			parent = arr[(i - 1)//2]
			print(self.__arr)
			print("childindex", i)
			print("parentindex", (i - 1)//2)
			print(f'parent = {parent}')
			print(f'child = {self.__arr[i]}')
			if self.__arr[i] < parent :
				print('check considered')
				self.__arr[i], self.__arr[(i - 1)//2] = self.__arr[(i - 1)//2], self.__arr[i]
				i = (i - 1)//2

			else :
				break

			

	def removemin(self):
		if not len(self.__arr) :
			return

		self.__arr[-1], self.__arr[0] = self.__arr[0], self.__arr[-1]
		ans = self.__arr.pop()
		i = 0
		while i < len(self.__arr):
			child1 = (i<<1) + 1 
			child2 = (i<<1) + 2
			if child1 >= len(self.__arr):
				break

			cval1 = self.__arr[child1]
			cval2 = (float('inf') if child2 >= len(self.__arr) else self.__arr[child2])

			if cval1 <= cval2 and cval1 < self.__arr[i] :
				self.__arr[child1], self.__arr[i] = self.__arr[i], self.__arr[child1]
				i = child1

			elif cval2 < cval1 and cval2 < self.__arr[i] :
				self.__arr[child2], self.__arr[i] = self.__arr[i], self.__arr[child2]
				i = child2

			else :
				break

		return ans

	def printheap(self):
		print(self.__arr) 

	def getmin(self):
		return self.__arr[0]

	def heapify(self, arr):
		for i in range(len(arr)):
			self.insert(arr[i])

	def isEmpty(self):
		return len(self.__arr) == 0


heap = MinHeap()
arr = [int(x) for x in input().split()]
heap.heapify(arr)

heap.printheap()
while not heap.isEmpty() :
	print(heap.removemin())



