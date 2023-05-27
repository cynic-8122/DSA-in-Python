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

def firstoccurenceofx(head, val):
	idx = 0
	if head == None :
		return -1

	itr = head
	while itr :
		if itr.data == val :
			return idx 

		idx += 1
		itr = itr.next

	return -1 

def swap(head, node1, node2):
	node1.data , node2.data = node2.data, node1.data
	return head

def swap2(head, idx1, idx2) :

	itr = head
	prev1 = None 
	prev2 = None 
	count = 0
	while itr.next :
		if count == idx1 - 1:
			prev1 = itr

		if count == idx2 - 1:
			prev2 = itr
		itr = itr.next
		count += 1

	if not (prev1 and prev2):
		print("Invalid input")

	next1 = prev1.next.next
	next2 = prev2.next.next

	if abs(idx1 - idx2) == 1 :
			prev1.next = prev2.next
			prev1.next.next = prev2
			prev2.next = next2

	else :
		prev1.next, prev2.next = prev2.next, prev1.next 
		print(prev1.next.data, prev2.next.data)
		prev2.next.next = next2
		prev1.next.next = next1
				

	return head



def evenafterodd(head):
	if head == None or head.next == None :
		return head

	itr = head
	while itr.next :
		if not itr.data&1 and itr.next.data&1 :

			swap(head, itr, itr.next)
			itr = head
			continue

		itr = itr.next

	return head

def deleteNNodes(head, M, N):
	#delete N nodes after every M nodes
	itr = head
	check = True
	while itr :
		if check :
			itr = None 
		temp1 = M 
		while temp1:
			#print("Will remain ", itr.data)
			if check :
				itr = head
			itr = itr.next
			temp1 -= 1
			if not itr :
				break
		#print("itr at", itr.data)
		temp2 = N + 1 
		tail = itr
		while tail and temp2 :
			#print("Will be deleted ", tail.data)
			tail = tail.next
			temp2 -= 1

		if itr :
			itr.next = tail
			

	return head
M, N = [int(x) for x in input().split()]
head = takeinput(arr)
#delnodes = deleteNNodes(head, M, N)
#printll(delnodes)
printll(head)
sw = swap2(head, M, N)
printll(sw)