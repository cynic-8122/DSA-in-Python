#User function Template for python3

class Solution:
    def canRepresentBST(self, arr, N):
        llimit = -1
        rlimit = float('inf')
        if self.Helper(arr, 0, N - 1, llimit, rlimit):
            return 1
            
        return 0
        
    def Helper(self, arr, start, end, llimit, rlimit):
        if start > end:
            return True
            
        if start == end:
            return (arr[start]>llimit) and (arr[start] < rlimit)
        
        mid = start    
        for j in range(start+1, end+1):
            if arr[j] > rlimit or arr[j] < llimit:
                return False
                
            if arr[j] < arr[start]:
                mid = j
                
            else:
                break
            
        ans1 = self.Helper(arr, start+1, mid, llimit, arr[start])
        ans2 = self.Helper(arr, mid+1, end, arr[start], rlimit)
        
        return ans1 and ans2
            
        

#{ 
#  Driver Code Starts
#Initial Template for Python 3

import sys
sys.setrecursionlimit(10**6)

if __name__ == '__main__':
    t = int(input())
    for _ in range (t):
        N = int(input())
        arr = input().split()
        for itr in range(N):
            arr[itr] = int(arr[itr])
        
        ob = Solution()
        print(ob.canRepresentBST(arr, N))
# } Driver Code Ends