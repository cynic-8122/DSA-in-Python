class Node:
 
    __slots__ = "row", "col", "data", "next"
 
    def __init__(self, row=0, col=0, data=0, next=None):
 
        self.row = row
        self.col = col
        self.data = data
        self.next = next
 
 
class Sparse:
 
    def __init__(self):
        self.head = None
        self.temp = None
        self.size = 0
 
    def __len__(self):
        return self.size
 
    def isempty(self):
        return self.size == 0
 
    def create_new_node(self, row, col, data):
 
        newNode = Node(row, col, data, None)
 
        if self.isempty():
            self.head = newNode

        else:
            self.temp.next = newNode

        self.temp = newNode
 
        self.size += 1
 
    def PrintList(self):
        temp = r = s = self.head
        print("row_position:", end=" ")
        while temp != None:
            print(temp.row, end=" ")
            temp = temp.next

        print()
        print("column_postion:", end=" ")

        while r != None:
            print(r.col, end=" ")
            r = r.next

        print()
        print("Value:", end=" ")

        while s != None:
            print(s.data, end=" ")
            s = s.next

        print()
 
 
s = Sparse()
 
sparseMatric = [[0, 0, 3, 0, 4],
                [0, 0, 5, 7, 0],
                [0, 0, 0, 0, 0],
                [0, 2, 6, 0, 0]]
                
for i in range(4):
    for j in range(5):
 
        if sparseMatric[i][j] != 0:
            s.create_new_node(i, j, sparseMatric[i][j])
 
s.PrintList()
 
    
