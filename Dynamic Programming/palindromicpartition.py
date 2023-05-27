#User function Template for python3

class Solution:
    def check(self, prev, curr, string):
        i = prev+1
        j = curr
        while i <= j:
            if string[i] != string[j]:
                return False
                
            i += 1
            j -= 1
            
        return False
        
    def palindromicPartition(self, string):
        prev = -1
        curr = 0
        n = len(string)
        return self.Helper(string, prev, curr, n)
        
    def Helper(self, string, prev, curr, n):
        if curr >= n :
            if self.check(prev, curr, string):
                return 0
                
            else:
                return float('inf')
        
        ans1 = float('inf')    
        if self.check(prev, curr, string):
            ans1 = 1 + self.Helper(string, curr, curr+1, n)
            
        ans2 = self.Helper(string, prev, curr+1, n)
        return min(ans1, ans2)
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range (t):
        string = input()
        
        ob = Solution()
        print(ob.palindromicPartition(string))
# } Driver Code Ends