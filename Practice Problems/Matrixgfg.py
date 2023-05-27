#User function Template for python3

class Solution:
    def searchWord(self, grid, word):
        ansarr = []
        idx = 0
        self.Helper(grid, word, 0, 0, ansarr)
        return ansarr
	    	    
    def Helper(self, grid, word, i, j, ansarr):
        if i >= len(grid) or j >= len(grid[0]):
            return
        
        if self.check(grid, i, j, word) and [i, j] not in ansarr:
            ansarr.append([i, j])
            
        self.Helper(grid, word, i, j+1, ansarr)
        self.Helper(grid, word, i+1, j, ansarr)
        
    def check(self, grid, i, j, word):
        #down
        idx = 0
        i1 = i
        j1 = j
        while i1 < len(grid) and j1 < len(grid[0]) and idx < len(word):
            if grid[i1][j1] == word[idx]:
                i1 += 1
                idx += 1
                
            else:
                break
            
        if idx >= len(word):
            return True
        #right    
        idx = 0
        i1 = i
        j1 = j
        while i1 < len(grid) and j1 < len(grid[0]) and idx < len(word):
            if grid[i1][j1] == word[idx]:
                j1 += 1
                idx += 1
                
            else:
                break
        
        if idx >= len(word):
            return True
            
        #up
        idx = 0
        i1 = i
        j1 = j
        while i1 >= 0 and j1 < len(grid[0]) and idx < len(word):
            if grid[i1][j1] == word[idx]:
                i1 -= 1
                idx += 1
                
            else:
                break
                
        if idx >= len(word):
            return True
            
        #left
        idx = 0
        i1 = i
        j1 = j
        while i1 < len(grid) and j1 >= 0 and idx < len(word):
            if grid[i1][j1] == word[idx]:
                j1 -= 1
                idx += 1
                
            else:
                break
        
        if idx >= len(word):
            return True
            
        #diagonal right down
        idx = 0
        i1 = i
        j1 = j
        while i1 < len(grid) and j1 < len(grid[0]) and idx < len(word):
            if grid[i1][j1] == word[idx]:
                i1 += 1
                j1 += 1
                idx += 1
                
            else:
                break
            
        if idx >= len(word):
            return True
            
        #diagonal left down
        idx = 0
        i1 = i
        j1 = j
        while i1 < len(grid) and j1 >= 0 and idx < len(word):
            if grid[i1][j1] == word[idx]:
                i1 += 1
                j1 -= 1
                idx += 1
                
            else:
                break
                
        if idx >= len(word):
            return True
            
        #diagonal left up
        idx = 0
        i1 = i
        j1 = j
        while i1 >= 0 and j1 >= 0 :
            if grid[i1][j1] == word[idx] and idx < len(word):
                i1 -= 1
                j1 -= 1
                idx += 1
            else:
                break
            
        if idx >= len(word):
            return True
            
        #diagonal right up
        idx = 0
        i1 = i
        j1 = j
        while i1 >= 0 and j1 < len(grid[0]) and idx < len(word):
            if grid[i1][j1] == word[idx]:
                i1 -= 1
                j1 += 1
                idx += 1
                
            else:
                break
                
        if idx >= len(word):
            return True
            
        return False
                
#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n, m = input().split()
		n = int(n); m = int(m);
		grid = []
		for _ in range(n):
			cur  = input()
			temp = []
			for __ in cur:
				temp.append(__)
			grid.append(temp)
		word = input()
		obj = Solution()
		ans = obj.searchWord(grid, word)
		for _ in ans:
			for __ in _:
				print(__, end = " ")
			print()
		if len(ans)==0:
		    print(-1)

# } Driver Code Ends