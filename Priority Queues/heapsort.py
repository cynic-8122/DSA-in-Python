class MaxHeap :
	def __init__(self):
		self.__count = 0

	def checkmaxheap(self, idx, arr):
		if idx == 0 :
			return

		parent = (idx - 1)>>1
		if arr[parent] < arr[idx]:
			arr[parent], arr[idx] = arr[idx], arr[parent]
			self.checkmaxheap(parent, arr)

	def heapify(self, arr):
		for i in range(len(arr)) :
			self.checkmaxheap(i, arr)
			self.__count += 1

	def getmax(self, arr):
		if self.__count == 1 :
			self.__count -= 1
			return 

		#for i in range(self.__count):
			#print("i =", i, "element =", arr[i])

		#print(f"(happening in getmax) element1 = {arr[0]} at index = {0} is being swapped with element2 = {arr[self.__count - 1]} index = {self.__count - 1}")
		arr[0], arr[self.__count - 1] = arr[self.__count - 1], arr[0]
		self.__count -= 1

	def downheapify(self, arr):
		i = 0
		while i < self.__count :
			child1 = 2*i + 1
			child2 = 2*i + 2

			if child1 >= self.__count:
				break

			cval1 = arr[child1]
			cval2 = (-float('inf') if child2 >= self.__count else arr[child2])
			swapidx = child1 if cval1 > cval2 else child2

			if arr[i] < arr[swapidx]:
				#print(f"(happening in down heapify) element1 = {arr[i]} at index = {i} is being swapped with element2 = {arr[swapidx]} index = {swapidx}")
				arr[i], arr[swapidx] = arr[swapidx], arr[i]
				i = swapidx

			else :
				break

	def heapsort(self, arr):
		self.heapify(arr)
		#print(arr)
		while self.__count :
			self.getmax(arr) 
			self.downheapify(arr)

		print(arr)

arr = [int(x) for x in input().split()]
mheap = MaxHeap()
mheap.heapsort(arr)



