
class Trie:
	def __init__(self):
		self.arr = [None for i in range(26)]
		self.bool = False

	def insert(self, string):
		root = self
		for i in range(len(string)):
			char = string[i]
			idx = ord(char) - ord('a')
			if root.arr[idx]:
				root = root.arr[idx]

			else:
				root.arr[idx] = Trie()
				root = root.arr[idx]
			

		root.bool = True

	def checkpresence(self, string):
		root = self
		for i in range(len(string)):
			char = string[i]
			idx = ord(char) - ord('a')
			if root.arr[idx]:
				root = root.arr[idx]

			else:
				return False

		if root.bool:
			return True

		return False


T = Trie()
T.insert("apple")
T.insert('apxl')
T.insert('bac')
print(T.checkpresence('apple'))
print(T.checkpresence('app'))
print(T.checkpresence('apxl'))
print(T.checkpresence('ba'))


