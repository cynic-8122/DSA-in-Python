def spiralPathMatrix(matrix, n, m):
    count = n*m
    l = 0
    r = m
    t = 1
    b = n
    i = 0
    j = 0
    ansarr = []
    while True:
        while j < r:
            ansarr.append(matrix[i][j])
            print(f"at i = {i}, j = {j}")
            j += 1
            count -= 1
        
        if count <= 0:
            break 

        r -= 1
        j -= 1
        i += 1
        while i < b:
            ansarr.append(matrix[i][j])
            print(f"at i = {i}, j = {j}")
            i += 1
            
            count -= 1
        
        if count <= 0:
            break 
                   
        i -= 1
        b -= 1
        j -= 1
        while j >= l:
            ansarr.append(matrix[i][j])
            print(f"at i = {i}, j = {j}")
            j -= 1
            count -= 1
        
        if count <= 0:
            break 
                   
        l += 1
        i -= 1
        j += 1
        while i >= t:
            ansarr.append(matrix[i][j])
            print(f"at i = {i}, j = {j}")
            i -= 1
            count -= 1
        
        if count <= 0:
            break 
                   
        t += 1
        j += 1
        i += 1
        
    return ansarr

n = int(input())
matrix = []
for i in range(n):
    row = [int(x) for x in input().split()]
    matrix.append(row)

print(spiralPathMatrix(matrix, n, len(matrix[0])))