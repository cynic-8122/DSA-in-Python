#User function Template for python3

class Solution:
    def isPossible(self, S, N, X, A):
        ansarr = []
        ansarr.append(S)
        sumsofar = S
        
        for i in range(N):
            x = A[i]
            t = sumsofar + x
            ansarr.append(t)
            sumsofar += t
            
        
        dp = [[-1 for i in range(X+1)] for i in range(N+1)]
        return self.ispossible(ansarr, X, N, dp)
        
    def ispossible(self, arr, target, n, dp):
        if n < 0:
            return 0
            
        if n == 0:
            if target == 0:
                return 1
                
            else:
                return 0
        
        if dp[n][target] != -1:
            return dp[n][target]
            
        take = self.ispossible(arr, target-arr[n], n-1, dp)
        nottake = self.ispossible(arr, target, n-1, dp)
        
        dp[n][target] = (take or nottake)
        return dp[n][target]
        # code here

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        S, N, X = [int(y) for y in input().split()]
        A = input().split()
        for i in range(N):
            A[i] = int(A[i])
        
        ob = Solution()
        if ob.isPossible(S, N, X, A) == 1:
            print("yes")
        else:
            print("no")
# } Driver Code Ends