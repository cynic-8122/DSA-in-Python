'''
Given an array arr of size N with all initial values as 0, 
the task is to perform the following M range increment operations as shown below:
Increment(ai, bi, ki) : Increment values from index 'ai' to 'bi' by 'ki'.
After M operations, calculate the maximum value in the array arr[].

Example 1:

Input: N = 5, M = 3, a[] = {0, 1, 2}
b[] = {1, 4, 3}, k[] = {100, 100, 100}
Output: 200
Explanation: Initially array = {0, 0, 0, 
                                   0, 0}
After first operation : {100, 100, 0, 0, 0}
After second operation: {100, 200, 100, 100, 100}
After third operation: {100, 200, 200, 200, 100}
Maximum element after m operations is 200.
'''

def findMax(self,n, m,a, b, c):
        prefix_arr = [0]*n
        for i in range(m):
            L = a[i]
            R = b[i]
            if R != n-1 :
                R += 1
                prefix_arr[R] += -c[i]
            prefix_arr[L] += c[i]
            #print(prefix_arr)
            
        sum_so_far = 0
        max_val = -float('inf')
        for i in range(n):
            sum_so_far += prefix_arr[i]
            prefix_arr[i] = sum_so_far
            max_val = max(max_val, sum_so_far)
        
        #print(prefix_arr)    
        return max_val