import random
def createSet(set_size, max_num) :
	set1 = {}
	for i in range(set_size) :
		x = random.randrange(0, (max_num + 1))
		set1.add(x)

	return set1


set_size = int(input("set_size = "))
max_num = int(input("max_num = "))
target_size = int(input("target_size = "))
print(createSet(set_size, max_num))

intersection_set = []
def intersectionSize(target_size, set_size, max_num) :
	a = createSet(set_size, max_num)
	b = createSet(set_size, max_num)
	a = list(a)
	for i in range(len(a)) :
		if (a[i] in b) :
			intersection_set.append(a[i])
	if len(intersection_set) >= target_size :
		print(set(intersection_set))

	return

intersectionSize(target_size, set_size, max_num)