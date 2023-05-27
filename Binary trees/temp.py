from sys import stdin, stdout, setrecursionlimit
from queue import Queue

setrecursionlimit(10 ** 7)


# Following is Binary tree node class for reference:
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

path_arr = []
def pathfromroottotarget(root, target):
    if root == None :
        return
    
    if root.data == target :
        path_arr.append(root)
        return root
    l = pathfromroottotarget(root.left, target)
    r = pathfromroottotarget(root.right, target)
    
    if l :
        t = [root, "L"]
        path_arr.append(t)
        return root 
    if r :
        t = [root, "R"]
        path_arr.append(t)
        return root

ans_arr = []
def printnodesatdepthk(root, k):
    if k < 0 :
        return
    
    if root == None :
        return
    
    #if k < 0 :
		#return 
    
    if k == 0 :
        ans_arr.append(root.data)
        return
    
    printnodesatdepthk(root.left, k - 1)
    printnodesatdepthk(root.right, k - 1)
    
def printNodesAtDistanceK(root, target, K):
    initial_distance = len(path_arr) - 1
    for i in reversed(range(1, len(path_arr))) :
        if initial_distance > K :
            initial_distance -= 1
            continue
            
        if initial_distance == K :
            ans_arr.append(path_arr[i][0].data)
            initial_distance -= 1
            continue
            
        if path_arr[i][1] == "L":
            printnodesatdepthk(path_arr[i][0].right, K - initial_distance - 1)
            
        elif path_arr[i][1] == "R" :
            printnodesatdepthk(path_arr[i][0].left, K - initial_distance - 1)
            
        initial_distance -= 1
    
    if len(path_arr):
    	printnodesatdepthk(path_arr[0], K)
    
        
    # Write your code here.
    return ans_arr


def findTarget(root, target):
    if root.data == target:
        return root

    if root.left is not None:
        leftSol = findTarget(root.left, target)
        if leftSol is not None:
            return leftSol

    if root.right is not None:
        rightSol = findTarget(root.right, target)
        if rightSol is not None:
            return rightSol

    return None


# Taking input.
def takeInput():
    arr = list(map(int, stdin.readline().strip().split(" ")))
    rootData = arr[0]

    n = len(arr)

    if rootData == -1:
        return None

    root = BinaryTreeNode(rootData)
    q = Queue()
    q.put(root)
    index = 1
    while q.qsize() > 0:
        currentNode = q.get()

        leftChild = arr[index]

        if (leftChild != -1):
            leftNode = BinaryTreeNode(leftChild)
            currentNode.left = leftNode
            q.put(leftNode)

        index += 1

        rightChild = arr[index]

        if rightChild != -1:
            rightNode = BinaryTreeNode(rightChild)
            currentNode.right = rightNode
            q.put(rightNode)

        index += 1

    return root


# Main.
T = int(input().strip())
while T > 0:
    T -= 1
    root = takeInput()
    target = int(stdin.readline())
    targetNode = findTarget(root, target)
    if targetNode is None:
        targetNode = root
    K = int(stdin.readline())
    nodesVector = printNodesAtDistanceK(root, targetNode, K)
    print(ans_arr)
    if len(nodesVector) == 0:
        stdout.write("-1\n")
    else:
        nodesVector.sort(key=lambda x:x.data)
        for i in nodesVector:
            stdout.write(str(i.data) + " ")
        stdout.write("\n")