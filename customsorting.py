class linkedlist():
	def __init__(self) :
		self.head = None

	def insert_link(self, list1) :
		for i in range(len(list1)) :
			temp = Node(list1[i][0])
			self.head = temp
			link = Node(list1[i])
			temp.next = link
			list1[i] = temp
	
	def merge(self, list1, list2) :
		arr = []
		i = 0
		j = 0
		while i < len(list1) and j < len(list2):
			a = list1[i].head.data
			b = list2[j].head.data
			if a <= b :
				arr.append(list1[i])
				i += 1

			else :
				arr.append(list2[j])
				j += 1
		if j >= len(arr2) :
			while i < len(arr1) :
				arr.append(list1[i])
				i += 1

		else :
			while j < len(arr2) :
				arr.append(list2[j])
				j += 1

		return arr 



	def sort_function(self, list1, left = 0, right = len(list1)) :
		
		if left == right :
			return [list1[left]]

		mid = (left + right)//2
		x = sort_function(list1, left, mid)
		y = sort_function(list1, mid+1, right)
		output = merge(x, y)
		return output

class Node():
	def __init__ (self, data = None, next = None) :
		self.data = data
		self.next = next






