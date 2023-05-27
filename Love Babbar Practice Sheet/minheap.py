class minheap:
	def __init__(self):
		self.arr = []

	def size(self):
		return len(self.arr)

	def isEmpty(self):
		return len(self.arr) == 0

	def push(self, ele):
		self.arr.append(ele)

		idx = len(self.arr) - 1
		parent = (i - 1)>>1

		while parent >= 0: 
			if self.arr[idx] < self.arr[parent]:
				self.arr[idx], self.arr[parent] = self.arr[parent], self.arr[idx]
				idx = parent
				parent = (parent - 1)>>1

			else:
				break

	def heapify(self, tarr):
		for i in range(len(tarr)):
			self.push(tarr[i])

	def top(self):
		return self.arr[0]

	def pop(self):
		self.arr[0], self.arr[-1] = self.arr[-1], self.arr[0]
		t = self.arr.pop()

		i = 0
		leftchild = 2*i + 1
		while leftchild < len(self.arr) :
			child1 = self.arr[leftchild]
			child2 = float('inf') if (2*i + 2) >= len(self.arr) else self.arr[(2*i + 2)]

			if child1 <= child2 :
				idx = leftchild

			else :
				idx = (2*i + 2)

			if self.arr[i] > self.arr[idx]:
				self.arr[i], self.arr[idx] = self.arr[idx], self.arr[i]
				i = idx
				leftchild = 2*i + 1

			else :
				break

		return t

arr = [int(x) for x in input().split()]

k = int(input())
H = minheap()
for i in range(k):
	H.push(arr[i])

for j in range(k, len(arr)):
	if arr[j] > H.top():
		H.pop()
		H.push(arr[j])

print(f"{k}th largest element in the array is {H.top()}")



