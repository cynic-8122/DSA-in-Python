#User function Template for python3

class Solution:
    def shortestPath(self, x, y): 
        # code here
        path1 = []
        path2 = []
        itr = x
        while itr > 0:
            path1.append(itr)
            itr = (itr)//2
            
        itr = y
        while itr > 0:
            path2.append(itr)
            itr = (itr)//2
            
        print(path1)
        print(path2)
        
        i = len(path1) - 1
        j = len(path2) - 1
        while i>=0 and j>=0 and path1[i] == path2[j]:
            i -= 1
            j -= 1
            
        i += 1
        j += 1
        return (i+j)

A = Solution()
x = int(input())
y = int(input())

print(A.shortestPath(x, y))