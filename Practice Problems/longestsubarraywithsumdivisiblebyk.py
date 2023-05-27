'''
Given an array containing N integers and a positive integer K, 
find the length of the longest sub array with sum of the elements divisible by the given value K.

Example 1:

Input:
A[] = {2, 7, 6, 1, 4, 5}
K = 3
Output: 4
Explanation:The subarray is {7, 6, 1, 4}
with sum 18, which is divisible by 3.
'''
def longSubarrWthSumDivByK (self,arr,  n, K) : 
        prefix_arr = []
        sum_so_far = 0
        for i in range(n):
            sum_so_far += arr[i]
	        prefix_arr.append(sum_so_far)
	    
	    max_len = 0
	    Hashmap = {}
        for i in range(n) :
            x = prefix_arr[i]%K
            if x in Hashmap.keys() :
                L = Hashmap[x]
                length = i - L
                max_len = max(max_len, length)
            
            if x == 0:
                max_len = max(max_len, i + 1)
            if x not in Hashmap.keys() :
                Hashmap[x] = i 
            
        return max_len