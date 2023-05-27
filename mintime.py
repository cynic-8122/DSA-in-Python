N = int(input())
x_arr = []
v_arr = []
for i in range(N) :
	
	x, v = input().split()
	x = float(x)
	v = float(v) 
	x_arr.append(x)
	v_arr.append(v)
print(f"x_arr = {x_arr}")
print(f"v_arr = {v_arr}")
x = min(v_arr)
y = min(x_arr)
z = max(x_arr)
def good(mid, x_arr, v_arr) :
	
		a = x_arr[0]
		b = x_arr[1]
		c = v_arr[0]
		d = v_arr[1]

		if (a + c*(mid)) == (b + d*(mid)) :
			temp_ans = (a + c*(mid))
		elif (a - c*(mid)) == (b + d*(mid)) :
			temp_ans =  (a - c*(mid)) 
		elif (a + c*(mid)) == (b - d*(mid)) :
			temp_ans = (a + c*(mid))
		elif (a - c*(mid)) == (b - d*(mid)) :
			temp_ans = (b - d*(mid))
		else :
			return False

		check = True
		for i in range(2, len(v_arr)) :
			if abs(temp_ans - x_arr[i]) != mid*(v_arr[i]) :
				check = False
				break

		return check


left = 0
right = (abs(z - y))/ x
for j in range(100) :
	mid = left + (right - left)/2
	if good(mid, x_arr, v_arr) :
		right = mid
	else :
		left = mid

print(mid) 

