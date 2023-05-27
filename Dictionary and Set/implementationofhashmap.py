class Node :
	def __init__(self, key = None, next = None, value = None):
		self.key = key
		self.next = next
		self.value = value

class LinkedList :
	def __init__(self):
		self.head = None
		self.tail = None

class Hashmap :
	def __init__(self, bucketsize):
		self.bucketsize = bucketsize
		self.bucket = [None]*bucketsize
		self.__count = 0

	def insert(self, key, value):
		Hashcode = hash(key)
		idx = Hashcode%(self.bucketsize)
		if self.bucket[idx] :
			self.bucket[idx].tail.next  = Node(key, None, value)
			self.bucket[idx].tail = self.bucket[idx].tail.next

		else :
			t = LinkedList()
			t.head = Node(key, None, value)
			t.tail = t.head
			self.bucket[idx] = t

		self.__count += 1

	def search(self, key):
		Hashcode = hash(key)
		idx = Hashcode%(self.bucketsize)
		itr = self.bucket[idx].head
		while itr :
			if itr.key == key :
				return itr.value

			itr = itr.next

		return None

	def remove(self, key):
		if not self.__count :
			return
		self.__count -= 1
		Hashcode = hash(key)
		idx = Hashcode%(self.bucketsize)
		itr = self.bucket[idx].head
		if itr.key == key :
			self.bucket[idx].head = itr.next
		while itr.next :
			if itr.next.key == key :
				itr.next = itr.next.next
			itr = itr.next

	def print(self):
		for i in range(len(self.bucket)) :
			if self.bucket[i] :
				itr = self.bucket[i].head
				while itr :
					print(itr.key, ":", itr.value)
					itr = itr.next


Map = Hashmap(10)
Map.insert("fuck you ", 3000)
Map.insert("lonley", float('inf'))
Map.print()
Map.insert("This is hella wierd", "I don't fuckin' know why")
Map.insert("You seem to be a perfect.... asshole ", "Agreed??")
Map.insert("How the f**k do you wake up knowing you're still going to be miserable by the end of your day", 3000)
Map.insert("Is the shit ever going to be right??", 0)
Map.insert("What the fuck do you even know ... This ain't what you think it is....", 101)
Map.print()



