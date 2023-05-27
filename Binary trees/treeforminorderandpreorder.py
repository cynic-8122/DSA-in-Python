#User function Template for python3

'''
# Node class

class Node:
    def __init__(self,val):
        self.data = val
        self.right = None
        self.left = None

'''

class Solution:
    def buildtree(self, inorder, preorder, n):
        i = 0
        l = 0
        r = n-1
        return self.Helper(inorder, preorder, i, l, r, n)
    
    def Helper(self, inorder, preorder, i, l, r, n):
        if l < 0 or r >= n or i >= n:
            return
        
        if l > r:
            return
        
        if l == r:
            return Node(inorder[l])
            
        currentnode = Node(preorder[i])
        for x in range(l, r+1):
            if inorder[x] == preorder[i]:
                mid = x
                currentnode.left = self.Helper(inorder, preorder, i+1, l, mid-1, n)
                currentnode.right = self.Helper(inorder, preorder, i+1, mid+1, r, n)
            
        
        
        return currentnode


class Node:
    def __init__(self,val):
        self.data = val
        self.right = None
        self.left = None

def printPostorder(n):
    if n is None:
        return
    printPostorder(n.left)
    printPostorder(n.right)
    print(n.data, end=' ')

if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        inorder = [ int(x) for x in input().split() ]
        preorder = [ int(x) for x in input().split() ]
        
        root = Solution().buildtree(inorder, preorder, n)
        printPostorder(root)
        print()

