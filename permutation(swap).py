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
		a = tuple(temp[i])
		b = list(a)
		b.append(li[right])
		per_arr.append(b)
		b = tuple(b)
		c = list(b)
		print(f"per_arr outside the swap loop {per_arr}")
		for j in reversed(range(1, right + 1)) :
			
			
			print(f"c before any swaps = {c}")
			c[j], c[j - 1] = c[j - 1], c[j]
			print(f"c after swapping {j} and {j-1}th index = {c}")
			per_arr.append(c)
			print(f"per_arr after append operation {per_arr}")
			

	
	return per_arr


for i in range(T) :
	n = int(input())
	li = input("Input your string ")
	print(li)
	print(permutation(li, 0, len(li) - 1))
	