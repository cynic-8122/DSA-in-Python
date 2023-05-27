'''
Staircase

A child is running up a staircase with N steps, and can hop either 1 step, 2 steps or 3 steps at a time. 
Implement a method to count how many possible ways the child can run up to the stairs. 
You need to return number of possible ways W.
Input format :
Integer N
Output Format :
Integer W
Constraints :
1 <= N <= 30
Sample Input 1 :
4
Sample Output 1 :
7
Sample Input 2 :
5
Sample Output 2 :
13
'''
def no_of_ways(N) :
	if N < 0 :
		return
	if N == 0 :
		return 1

	if N == 1 :
		return 1

	if N == 2 :
		return 2

	return no_of_ways(N - 1) + no_of_ways(N - 2) + no_of_ways(N - 3)

N = int(input())
print(no_of_ways(N))



