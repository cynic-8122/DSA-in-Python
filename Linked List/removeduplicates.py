'''
Eliminate duplicates from LL
Send Feedback
You have been given a singly linked list of integers where the elements are sorted in ascending order. 
Write a function that removes the consecutive duplicate values such that, 
the given list only contains unique elements and returns the head to the updated list.
 Input format :
The first line contains an Integer 't' which denotes the number of test cases or queries to be run. 
Then the test cases follow.

The first and the only line of each test case or query contains the elements(in ascending order) of the 
singly linked list separated by a single space.
 Remember/Consider :
While specifying the list elements for input, -1 indicates the end of the singly linked list and hence, 
would never be a list element.
 Output format :
For each test case/query, print the resulting singly linked list of integers in a row, 
separated by a single space.

Output for every test case will be printed in a seperate line.
Constraints :
1 <= t <= 10^2
0 <= M <= 10^5
Time Limit: 1sec

Where 'M' is the size of the singly linked list.
Sample Input 1 :
1
1 2 3 3 4 3 4 5 4 5 5 7 -1
Sample Output 1 :
1 2 3 4 3 4 5 4 5 7 
Sample Input 2 :
2
10 20 30 40 50 -1
10 10 10 10 -1
Sample Output 2 :
10 20 30 40 50
10

'''
class Node :
	def __init__(self, data = None, next = None):
		self.data = data
		self.next = next

class LinkedList :
	def __init__(self):
		self.head = None
		self.tail = None

	def addatlast(self, data):
		if self.head == None :
			self.head = Node(data)
			self.tail = self.head
			return

		self.tail.next = Node(data)	
		self.tail = self.tail.next

	def arrtoll(self, arr):
		if len(arr) == 0 :
			return

		for i in range(len(arr)):
			self.addatlast(arr[i])

	def print(self):
		itr = self.head
		ans = ""
		while itr.next :
			ans += str(itr.data) + " -> "
			itr = itr.next

		ans += str(itr.data)
		print(ans)

	def search(self, val):
		if self.head == None :
			print(-1)
			return

		itr = self.head
		while itr :
			if itr.data == val :
				print("Found the match ")
				return

			itr = itr.next

		print(-1)

	def removeduplicates(self):
		itr = self.head
		check = self.head
		while itr.next :
			if itr.next.data == check.data :
				#print("check1")
				itr.next = itr.next.next
				
				
			else :
				#print("check2")
				itr = itr.next
				check = itr
				
			
		
arr = [int(x) for x in input().split()]
arr.sort()
LL = LinkedList()
LL.arrtoll(arr)
LL.print()
LL.removeduplicates()
LL.print()


