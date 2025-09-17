def addEdge(mat, i, j, directed = False):
    mat[i][j] = 1
    if not directed:
        #For undirected 
        mat[j][i] = 1

def removeEdge(mat, i, j, directed = False):
    mat[i][j] = 0
    if not directed:
        mat[j][i] = 0

def hasEdge(mat, i, j):
    return mat[i][j] == 1

def display(mat):
    for i in mat:
        print(" ".join(map(str, i)))

V = int(input("Enter no of vertices: "))
mat = [[0] * V for i in range(V)]
addEdge(mat, 0, 1)
addEdge(mat, 0,2)
addEdge(mat, 1, 2)
addEdge(mat, 3, 2)

print("adj matrix: ")
display(mat)