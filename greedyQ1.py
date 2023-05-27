N = int(input("Number of meetings"))
meet_arr = []

current_meet = [int(x) for x in input().split()]
meet_arr.append(current_meet)
number_of_rooms = 1
min_so_far = current_meet[1]
for i in range(1, N) :
	current_meet = [int(x) for x in input().split()]
	meet_arr.append(current_meet)
	if meet_arr[i][1] < meet_arr[i - 1][1] :
		min_so_far = meet_arr[i][1]
	if meet_arr[i][0] < meet_arr[i - 1][1] :
		number_of_rooms += 1 


