def isSymmetrical(matrix):
    n = len(matrix)
    for i in range(n):
        for j in range(n):
            if not matrix[i][j] == matrix[j][i]:
                return 0
    return 1


t = int(input())

for t in range(t):
    n = int(input())
    matrix = []
    for i in range(n):
        matrix.append(list(map(int, input().split())))
    diagonal = []
    zeroInDiagonal = False
    upperHalf = []
    upperTriangle = True
    lowerTriangle = True
    lowerHalf = []
    for i in range(n):
        upLine = matrix[i][i+1:]
        lowLine = matrix[n-i-1][:n-i-1]
        upperHalf.append(upLine)
        lowerHalf.append(lowLine)
        if not (upLine.count(0) == len(upLine)):
            upperTriangle = False
        if not (lowLine.count(0) == len(lowLine)):
            lowerTriangle = False
        diagonal.append(matrix[i][i])
        if matrix[i][i] == 0:
            zeroInDiagonal = True
   
    if upperTriangle or lowerTriangle:
        if lowerTriangle and upperTriangle:
            if not zeroInDiagonal:
                isDiagonal = 1
            else:
                isDiagonal = 0
        else:
            isDiagonal = 0
        isTriangular = 1
    else:
        isDiagonal = 0
        isTriangular = 0

    print(isSymmetrical(matrix) + 2*isTriangular + 4*isDiagonal)
