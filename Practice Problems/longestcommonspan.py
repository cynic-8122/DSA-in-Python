'''
Given two binary arrays arr1[] and arr2[] of same size N.
Find length of the longest common span [i, j] where j>=i such that arr1[i] + arr1[i+1] + …. + arr1[j] = arr2[i] + arr2[i+1] + …. + arr2[j]. 

 

Example 1:

Input:
N = 6
Arr1[] = {0, 1, 0, 0, 0, 0}
Arr2[] = {1, 0, 1, 0, 0, 1}
Output: 4
Explanation: The longest span with same
sum is from index 1 to 4 following zero 
based indexing.
'''
def longestCommonSum(self, arr1, arr2, n):
	Hashmap = {}
	diff = 0
	sum_so_far1 = 0
	sum_so_far2 = 0
	max_len = 0
	for i in range(n):
	    sum_so_far1 += arr1[i]
	    sum_so_far2 += arr2[i]
	    diff = sum_so_far1 - sum_so_far2
	    if diff == 0 :
	        max_len = max(max_len, i+1)
	    elif diff in Hashmap.keys():
	        x = Hashmap[diff]
	        max_len = max(max_len, i - x)
	    else :
	        Hashmap[diff] = i
	        
	return max_len