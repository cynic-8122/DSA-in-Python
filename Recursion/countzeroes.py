def count_zeroes(N):
	print(N)
	if N//10 == 0 and N%10 != 0:
		return 0
	
	
	ans = count_zeroes(N//10)
	if N%10 == 0 :
		return 1 + ans
	if N%10 != 0 :
		return ans
	

N = int(input())
#print(N)
print(count_zeroes(N))