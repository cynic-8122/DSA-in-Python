arr_1 = [int(x) for x in input().split()]
arr_2 = [int(x) for x in input().split()]
arr_1.sort()
arr_2.sort()

n = len(arr_1)
m = len(arr_2)
left_1, left_2 = 0, 0
right_1, right_2 = n, m 

while left_1 <= right_1 and left_2 <= right_2 :
	mid_1 = (left_1 + right_1)//2
	mid_2 = (left_2 + right_2)//2
	if arr_1[mid_1] >= arr_2[mid_2] and arr_1[mid_1] <= arr_2[mid_2 + 1] :
		ans = arr_1[mid_1]
		break
	if arr_1[mid_1] < arr_2[mid_2] :
		left_1 = mid_1 + 1
		right_2 = mid_2 - 1
	else :
		left_2 = mid_2 + 1
		right_1 = mid_1 - 1

if (m + n)&1 == 1 :
	print(ans)

else :
	print((ans + min(arr_1[mid_1 + 1], arr_2[mid_2 + 1]))/2)
