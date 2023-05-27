import random

def mysteryPrinter(list1, list2) :
	x = random.randrange(1, 6)

	if len(list1) == len(list2) :
		print("Two lists are of same size ")

	elif len(list1) > 20 or len(list2) > 20 :
		print("One of the lists is too long ")
		return

	elif x == 1 :
		output = list1[0] + list2[-1]
		print("Mystery sum 1", output)
		
	elif x == 2 :
		output = list1[-1] + list2[0]
		print("Mystery sum 2", output)

	elif x == 3 :
		output = sum(list1) - sum(list2)
		print("Mystery sum 3", output)

	elif x == 4 :
		output = min(list1) + min(list2)
		print("Mystery sum 4", output)

	else :
		output = (sum(list1)/len(list1)) - (sum(list2)/len(list2))
		print("Mystery sum 5", output)

	return

list1 = [int(x) for x in input().split()]
list2 = [int(x) for x in input().split()]

mysteryPrinter(list1, list2)


		


