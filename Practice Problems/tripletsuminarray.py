'''
Given an array arr of size n and an integer X. 
Find if there's a triplet in the array which sums up to the given integer X.


Example 1:

Input:
n = 6, X = 13
arr[] = [1 4 45 6 10 8]
Output:
1
Explanation:
The triplet {1, 4, 8} in 
the array sums up to 13.
'''
def find3Numbers(self,A, n, X):
    A.sort()
    for i in range(n - 2):
        looking_for = X - A[i]
        left = i + 1
        right = n - 1
        while left < right :
            current_sum = A[left] + A[right]
            if current_sum == looking_for :
                return True
            if current_sum > looking_for :
                right -= 1
            else :
                left += 1
    return False