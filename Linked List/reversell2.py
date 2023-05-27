class Node :
	def __init__(self, data = None, next = None):
		self.data = data
		self.next = next

arr = [int(x) for x in input().split()]
def takeinput(arr):
	i = 0
	while  i < len(arr) :
		#print(i)
		if arr[i] == -1 :
			break
		newnode = Node(arr[i])
		if i == 0 :
			head = newnode
			tail = head
			i += 1
			continue

		tail.next = newnode
		tail = newnode
		i += 1

	return head

def printll(head):
	if head == None :
		return

	itr = head
	ans = ""
	while itr.next :
		ans += str(itr.data) + " -> "
		itr = itr.next

	ans += str(itr.data)
	print(ans)


def reverse(head):
	if head == None or head.next == None :
		return head

	newhead = reverse(head.next)
	tail = head.next
	head.next = None 
	tail.next = head 

	return newhead

def reverseitr(head):
	if head == None or head.next == None :
		return head 

	itr = head 
	temp = None 
	prev = None 
	while itr.next :
		prev = temp
		temp = itr 
		itr = itr.next
		temp.next = prev

	itr.next = temp 
	return itr

head = takeinput(arr)
printll(head)
head = reverseitr(head)
printll(head)


