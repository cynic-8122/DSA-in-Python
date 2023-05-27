'''
Given a number N, the task is to ;
find the number of ways to represent this number as a sum of 2 or more consecutive natural numbers.

 

Example 1:

Input:
N = 10
Output:
1
Explanation:
10 can be reprsented as sum of two or
more consecutive numbers in only one
way. 10 = 1+2+3+4.
'''

def check_count(n):
	count = 0
	l = 2
	sum_of_len = 3
	while sum_of_len <= n :
		#print("GOOD")
		l += 1
		sum_of_len = (l*(l+1))//2

	l -= 1
	#print(l)
	
	check = 2
	while check <= l:
		#print("LOOP 2")
		if (n - ((check - 1)*(check)//2))%(check) == 0 :
			#print("worked for", (check))
			count += 1

		check += 1
		

	return count 

n = int(input())
print(check_count(n))



