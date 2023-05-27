class Node :
	def __init__(self, data = None, next = None):
		self.data = data
		self.next = next

#arr1 = [int(x) for x in input().split()]
#arr2 = [int(x) for x in input().split()]
arr3 = [int(x) for x in input().split()]
#arr1.sort()
#arr2.sort()
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

def midofll(head):
	if head == None or head.next == None :
		return head 

	itr1 = itr2 = head 
	while itr2.next and itr2.next.next :
		itr1 = itr1.next
		itr2 = itr2.next.next

	return itr1.data

def mergetwoll(head1, head2):
	if head1 == None :
		return head2

	elif head2 == None :
		return head1


	itr1 = head1
	itr2 = head2

	temp = Node(min(head1.data, head2.data))
	if temp.data == itr1.data:
		itr1 = itr1.next

	else:
		itr2 = itr2.next
	start = temp
	while itr1 and itr2 :
		if itr1.data <= itr2.data:
			temp.next = Node(itr1.data)
			temp = temp.next
			itr1 = itr1.next

		else :
			temp.next = Node(itr2.data)
			temp = temp.next
			itr2 = itr2.next

	while itr2 :
		temp.next = Node(itr2.data)
		temp = temp.next
		itr2 = itr2.next

	while itr1 :
		temp.next = Node(itr1.data)
		temp = temp.next
		itr1 = itr1.next

	return start

def givell(head, l, r):
	if l > r :
		return 

	if l == r :
		count = 0
		itr = head 
		while itr :
			count += 1
			if count == l + 1 :
				return Node(itr.data) 

			itr = itr.next

	itr = head
	while l :
		itr = itr.next
		l -= l 

	start = Node(itr.data)
	temp = start
	t = r - l 
	while t and itr.next :
		#print(itr.data)
		itr = itr.next 
		temp.next = Node(itr.data)
		temp = temp.next
		t -= 1 

	return start


def mergesort(head, l, r):
	if l > r :
		return 

	if l == r:
		return givell(head, l, r)

	mid = (l + r)//2

	head1 = mergesort(head, l, mid)
	head2 = mergesort(head, mid + 1, r)
	#printll(head1)
	#printll(head2)
	#print("First LL")
	#printll(head1)
	#print("Second LL")
	#printll(head2)
	return mergetwoll(head1, head2)

def lengthofll(head):
	if head == None :
		return 0

	count = 0
	itr = head 
	while itr :
		count += 1
		itr = itr.next

	return count
	
#head1 = takeinput(arr1)
#head2 = takeinput(arr2)
head3 = takeinput(arr3)
#printll(head1)
#printll(head2)
#print(midofll(head1))
#print(midofll(head2))
#merge = mergetwoll(head1, head2)
#printll(merge)
length = lengthofll(head3)
sortedll = mergesort(head3, 0, length - 1)
printll(sortedll)





