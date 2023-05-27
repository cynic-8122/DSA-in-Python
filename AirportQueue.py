N = int(input("Enter the value of N "))
airport_queue = []

while True :
	for i in range(N):
		#________________________________ENQUEUE_____________________________________
		a = input("Enter the type of passenger ")
		b = input("Name of the passenger")
		if a == "VIP" :
			airport_queue.insert(0, b)
		else :
			airport_queue.append(b)
	
		print(airport_queue)

		ans = input("Are there anymore passengers? (y/n)")

		if ans == "n" :
			break

	#________________________________DEQUEUE_____________________________________
	while len(airport_queue) >= (0.8)*N :
		airport_queue.pop(0)
		airport_queue.pop()
		print(airport_queue)

	while len(airport_queue) != 0 :
		airport_queue.pop(0)
		print(airport_queue)
	
	ans = input("Are there anymore passengers? (y/n)")
	if ans == "n" :
		break
