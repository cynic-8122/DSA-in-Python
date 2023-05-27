class Solution:
	def isBipartite(self, V, adj):
		color = [-1 for i in range(V)]
		for i in range(V):
			if color[i] == -1:
				tempans = self.DFS(i, adj, color, 0)
				if tempans == False:
					return False
	                
		return True
    
	def DFS(self, start, adj, color, currentcolor):
		if color[start] != -1 :
			if color[start] != currentcolor:
				return False

			return True
            
		color[start] = currentcolor
		ans = True
		for x in adj[start]:
			nextcolor = currentcolor^1
			tempans = self.DFS(x, adj, color, nextcolor)
			ans = (ans and tempans)
            
		return ans
            
	            

#{ 
#  Driver Code Starts
if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		V, E = map(int, input().strip().split())
		adj = [[] for i in range(V)]
		for i in range(E):
			u, v = map(int, input().strip().split())
			adj[u].append(v)
			adj[v].append(u)
		obj = Solution()
		ans = obj.isBipartite(V, adj)
		if(ans):
			print("1")
		else:
			print("0")

# } Driver Code Ends