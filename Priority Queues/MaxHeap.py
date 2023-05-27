class MaxHeap :
	def __init__(self):
		self.__arr = []

	def insert(self, val):
		self.__arr.append(val)
		i = len(self.__arr) - 1
		while i :
			parentidx = (i - 1)>>1
			parent = self.__arr[parentidx]

			if self.__arr[i] > parent :
				self.__arr[parentidx], self.__arr[i] = self.__arr[i], self.__arr[parentidx]
				i = parentidx

			else :
				break

	def getsize(self):
		return len(self.__arr)

	def isEmpty(self):
		return len(self.__arr) == 0

	def getmax(self):
		return self.__arr[0]

	def removemax(self):
		if self.isEmpty() :
			return

		self.__arr[0], self.__arr[-1] = self.__arr[-1], self.__arr[0]
		ans = self.__arr.pop()
		i = 0
		while i < len(self.__arr):
			