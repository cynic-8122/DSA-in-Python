from queue import PriorityQueue as pq

class Solution:
    
    #Function to return the minimum cost to react at bottom
	#right cell from top left cell.
    def minimumCostPath(self, grid):
        n = len(grid)
        adjlist = [[] for i in range(n*n)]
        
        for i in range(n):
            for j in range(n):
                node1 = i*n+j
                rightnode = node1+1
                downnode = node1+n
                if j+1 < n:
                    adjlist[node1].append([rightnode, grid[i][j+1]])
                    adjlist[rightnode].append([node1, grid[i][j+1]])
                    
                if i+1 < n:
                    adjlist[node1].append([downnode, grid[i+1][j]])
                    adjlist[downnode].append([node1, grid[i+1][j]])
                
        
        distarr = [float('inf') for i in range(n*n)]
        visitedarr = [False for i in range(n*n)]
        print(adjlist)
        distarr[0] = 0
        Q = pq()
        Q.put([0, 0])
        while not Q.empty():
            currentnode, dist = Q.get()
            visitedarr[currentnode] = True
            for x in adjlist[currentnode]:
                node, weight = x
                if distarr[node] > distarr[currentnode] + weight and visitedarr[node] == False:
                    distarr[node] = distarr[currentnode] + weight
                    Q.put([node, distarr[currentnode] + weight])
                    
        
        print(distarr)
        return distarr[-1] + grid[0][0]
                
                
	                
	   
	                


#{ 
 # Driver Code Starts
if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		grid = []
		for _ in range(n):
			a = list(map(int, input().split()))
			grid.append(a)
		obj = Solution()
		ans = obj.minimumCostPath(grid)
		print(ans)

# } Driver Code Ends