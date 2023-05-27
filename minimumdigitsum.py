import math
Q = int(input())

for i in range(Q):
	n, l, r = [int(x) for x in input().split()]
	ans = 0
	while l <= r :
		mid = (l + r)//2
		pwr1 = (math.log(n))//(math.log(mid))
		temp1 = n - (mid)**(pwr1)
		p = mid + 1 
		pwr2 = (math.log(n))//(math.log((mid + 1)))
		temp2 = n - (mid+1)**(pwr2)
		q = mid - 1
		pwr0 = (math.log(n))//(math.log((mid - 1)))
		temp0 = n - (mid - 1)**(pwr0) 

		#print("mid", mid)
		#print("temp1", temp1)
		#print("temp2", temp2)
		if temp0 > temp1 and temp2 > temp1 :
			#found the precise number
			ans = mid
			break
		if temp1 > temp2 :
			#ideal val is somewhere in the right
			l = mid + 1
			ans = mid

		else :
			#ideal val is somewhere in the left
			r = mid - 1
			ans = mid

	print(ans)






