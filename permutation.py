T = int(input())
per_arr = []
def permutation(li, left, right) :
	if left == right :
		return [[li[left]]]
	x = permutation(li, left, right - 1)
	temp = x
	#print(f"temp = {temp}")
	per_arr = []


	for i in range(len(temp)) :
		for j in range(right + 1) :
			a = tuple(temp[i])
			b = list(a)
			#print(f"a = {a}")
			b.insert(j, li[right])
			#print(f"inserting {li[right]} at index j = {j}")
			per_arr.append(b)
			#print(f"after appending the per_arr looks {per_arr}")

	
	return per_arr


for i in range(T) :
	n = int(input())
	li = input("Input your string ")

	#for j in range(1, n+1) :
		#li.append(j)
	print(li)
	#print("______________________________________________________________")
	print(permutation(li, 0, len(li) - 1))
	#print("______________________________________________________________")
	
	
		

#print(f"x = {x}")
#print(f"inserting {li[right]} at j = {j}")
#y = list(x)
#x.insert(j, li[right])
#per_arr.append(x)
#if len(y) == len(li) :
		#return
	#y.append(li[right])