#User function Template for python3

class Solution:
    def findPath(self, m, n):
        print(m)
        ansarr = []
        visitedarr = [[False for i in range(n)] for i in range(n)]
        self.Helper(m, n, 0, 0, ansarr, '', visitedarr)
        
        return ansarr
        
    def Helper(self, m, n, i, j, ansarr, tempans, visitedarr):
        print(f"i = {i}, j = {j}")
        print(m[i][j])
        if i == n-1 and j == n-1:
            ansarr.append(tempans)
            return
        
        visitedarr[i][j] = True
        
        if i+1 < n and not visitedarr[i+1][j] and m[i+1][j] != 0:
            self.Helper(m, n, i+1, j, ansarr, tempans+'D', visitedarr)
            
            
        if j+1 < n and not visitedarr[i][j+1] and m[i][j+1] != 0:
  
            self.Helper(m, n, i, j+1, ansarr, tempans+'R', visitedarr)
            
            
        if i-1 >= 0 and not visitedarr[i-1][j] and m[i-1][j] != 0:
            
            self.Helper(m, n, i-1, j, ansarr, tempans+'U', visitedarr)
                        
        if j-1 >= 0 and not visitedarr[i][j-1] and m[i][j-1] != 0:
            self.Helper(n, n, i, j-1, ansarr, tempans+'U', visitedarr)
                    

        visitedarr[i][j] = False
        
        
        

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))
        
        matrix = [[0 for i in range(n[0])]for j in range(n[0])]
        k=0
        for i in range(n[0]):
            for j in range(n[0]):
                matrix[i][j] = arr[k]
                k+=1
        ob = Solution()
        result = ob.findPath(matrix, n[0])
        result.sort()
        if len(result) == 0 :
            print(-1)
        else:
            for x in result:
                print(x,end = " ")
            print()
# } Driver Code Ends