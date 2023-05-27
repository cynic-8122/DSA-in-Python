"""
Chef is multi-talented. He has developed a cure for coronavirus called COVAC-19. Now that everyone in the world is infected, it is time to distribute it throughout the world efficiently to wipe out coronavirus from the Earth. Chef just cooks the cure, you are his distribution manager.

In the world, there are N countries (numbered 1 through N) with populations a1,a2,…,aN. Each cure can be used to cure one infected person once. Due to lockdown rules, you may only deliver cures to one country per day, but you may choose that country arbitrarily and independently on each day. Days are numbered by positive integers. On day 1, Chef has x cures ready. On each subsequent day, Chef can supply twice the number of cures that were delivered (i.e. people that were cured) on the previous day. Chef cannot supply leftovers from the previous or any earlier day, as the cures expire in a day. The number of cures delivered to some country on some day cannot exceed the number of infected people it currently has, either.

However, coronavirus is not giving up so easily. It can infect a cured person that comes in contact with an infected person again ― formally, it means that the number of infected people in a country doubles at the end of each day, i.e. after the cures for this day are used (obviously up to the population of that country).

Find the minimum number of days needed to make the world corona-free.
"""
# cook your dish here
T = int(input())

for i in range(T) :
    N, x = [int(y) for y in input().split()]
    arr = [int(y) for y in input().split()]
    arr.sort()
    days = 0
    i = 0
    check = True
    while i < (N):
    	print(f"loop is being executed i = {i}")
		if check:
			arr[i] = arr[i]<<(days)
		else :
			arr[i] = arr[i]<<1 
		arr[i] = max(0, (arr[i] - x))
		print(f"arr[{i}] = {arr[i]}")
		if x > arr[i] :
			x = arr[i]
		x = x<<1 
		days += 1
		if arr[i] == 0 :
			i += 1
			check = True
		else:
			check = False 
    
	print(days)