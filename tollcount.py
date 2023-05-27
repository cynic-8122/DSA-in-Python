n = int(input())
plate_arr = []
t_arr = []
total_fair = 0
 

for i in range(n) :
	a = input()
	
	plate = input()
	t = int(input())
	if plate in plate_arr :
		x = plate_arr.index(plate)
		t1 = t_arr[x]
		T = abs(t1 - t)
		if (T % 60) >= 30 :
			T = (T // 60) + 1
		else :
			T = (T // 60)
		

		fair = (T + 1)*(30)
		total_fair += fair
		print(f"Time spent by {plate} is {T} hours ")

	plate_arr.append(plate)
	t_arr.append(t)

print(total_fair)












