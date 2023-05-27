class Solution:
    def DFS(self, itr, dest, path):
        path.append(itr)
        if itr > dest:
            return False
        
        if itr == dest:
            return True
        
        #print(f"destination = {dest}, path = {path}")
        left = self.DFS(2*itr, dest, path)
        if not left:
            path.pop()

        else:
            return True
        right = self.DFS((2*itr)+1, dest, path)
        if not right:
            path.pop()

        else:
            return True
            
        
        
    def LCA(self, x, y):
        root = 1
        path1 = []
        path2 = []
        itr1 = root
        itr2 = root
        self.DFS(itr1, x, path1)
        self.DFS(itr2, y, path2)
        n = min(len(path1), len(path2))
        
        LCA = path1[0]
        check = False
        for i in range(n):
            if path1[i] == path2[i]:
                LCA = path1[i]
                
            else:
                check = True
                break
            
        
        return LCA
            
                    
            
    def shortestPath(self, x, y):
        start = self.LCA(x, y)
        print('start', start)
        path1 = []
        path2 = []
        self.DFS(start, x, path1)
        self.DFS(start, y, path2)
        print(path1)
        print(path2)
        return len(path1) + len(path2) - 1

A = Solution()
x = int(input())
y = int(input())
print(A.shortestPath(x, y))