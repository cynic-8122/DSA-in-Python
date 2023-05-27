#User function Template for python3

class Solution:
	def ShortestDistance(self, matrix):
		count = 0
		steps = 0
		ansmatrix = [[0 for i in range(len(matrix[0]))] for i in range(len(matrix))]
		ds = []
		ans, count = self.Helper(matrix, count, ansmatrix, float('inf'), ds)
		
		print(ds)
		if len(ds) == 0:
			return [[-1]]

		return ds
		
		
	def Helper(self, matrix, count, ansmatrix, tempcount, ds, i = 0, j = 0):
		print(f"i = {i}, j = {j}")
		if i == len(matrix) - 1 and j == len(matrix[0]) - 1:
			ansmatrix[i][j] = 1
			tempans = list(ansmatrix)
			return tempans, count 
		    
		if matrix[i][j] == 0:
			tempans = list(ansmatrix)
			return tempans, float('inf')
		
		steps = matrix[i][j]
		t = steps
		for x in range(steps):

			if (j+x+1) < len(matrix[0]) and i < len(matrix):
				ansmatrix[i][j] = 1
				count += 1
				tans, c = self.Helper(matrix, count, ansmatrix, tempcount, ds, i, j+x+1)
				print(f"countsofar, {c}")
				print(f"tempcount, {tempcount}")
				if c < tempcount:
					tempcount = c
					ds = list(tans)
					print(f"ds = {ds}")
				    
				ansmatrix[i][j] = 0
				count -= 1

				
        
		for x in range(steps):

			if (i+x+1) < len(matrix) and j < len(matrix[0]):
				ansmatrix[i][j] = 1
				count += 1
				tans2, c2 = self.Helper(matrix, count, ansmatrix, tempcount, ds, i+x+1, j)
				print(f"countsofar2, {c2}")
				print(f"tempcount, {tempcount}")
				if c2 < tempcount:
					tempcount = c2
					ds = list(tans2)
					print(f"ds = {ds}")
				    
				ansmatrix[i][j] = 0
				count -= 1
				
                
                   

	    
	    
	    
	        
	        
	    

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		matrix= []
		for i in range(n):
			a = list(map(int, input().split()))
			matrix.append(a)
		ob = Solution()
		ans = ob.ShortestDistance(matrix)
		for i in ans:
			for j in i:
				print(j, end = " ")
			print()

# } Driver Code Ends