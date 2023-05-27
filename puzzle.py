arr = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]

initial_pos = arr[3][0]


def traversal(arr, curr_y, curr_x, ans_str):
	if curr_x > 3:
		print(ans_str)
		return
	if curr_y < 0:
		print(ans_str)
		return
	if curr_y > 3 :
		return
	if curr_x < 0 :
		return

	traversal(arr, curr_y - 1, curr_x, ans_str + str(arr[curr_y][curr_x]) + ",")
	traversal(arr, curr_y, curr_x + 1, ans_str + str(arr[curr_y][curr_x]) + ",")
	


	print(ans_str)
	count = 0
	check = ","
	for check in ans_str :
		count += 1 
	if count == 14 :
		print("Yes")
	return ans_str

traversal(arr, 3, 0, "")