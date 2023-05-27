#User function Template for python3

import collections
from collections import deque
from collections import defaultdict

class Solution:
    def findNumberOfGoodComponent(self, V, adj):
        visitedarr = [False for i in range(V)]
        count = 0
        for i in range(V):
            if visitedarr[i] == False:
                count += 1
                self.Helper(i, adj, visitedarr)
                
        return count
        
    def Helper(self, node, adj, visitedarr):
        visitedarr[node] = True
        for x in adj[node]:
            if visitedarr[x] == False:
                self.Helper(x, adj, visitedarr)

#{ 
#  Driver Code Starts
#Initial Template for Python 3

from sys import stdin, stdout
if __name__ == '__main__':
    test_cases = int(input())
    for _ in range (test_cases):
        E, V = map(int, input().split())
        adj = []
        for _ in range(E):
            a,b = map(int, input().split())
            adj.append([a,b])
        res = Solution().findNumberOfGoodComponent(V, adj)
        print(res)
# } Driver Code Ends