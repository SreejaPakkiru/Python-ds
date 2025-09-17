#Python implementation of Graph represented using Adjacency Matrix:

def add_edge(mat, i, j):
    mat[i][j] = 1
    mat[j][i] = 1

def  display(mat):
    for i in mat:
        print(" ".join(map(str, i)))

V = 4
mat = [[0] * V for i in range(V)]
add_edge(mat, 0, 1)
add_edge(mat, 0, 2)
add_edge(mat, 1, 2)
add_edge(mat, 2, 3)
print("Adjacency Matrix:")
display(mat)

#using Adjacency List
def addEdge(adj, i, j):
    adj[i].append(j)
    adj[j].append(i)

def display_adjlist(adj):
    for i in range(len(adj)):
        print(f"{i}: ", end=" ")
        for j in adj[i]:
            print(j, end=" ")
        print()
Vl= 4
adjl = [[] for i in range(V)]

# Now add edges one by one
addEdge(adjl, 0, 1)
addEdge(adjl, 0, 2)
addEdge(adjl, 1, 2)
addEdge(adjl, 2, 3)


print("Adjacency List Representation:")
display_adjlist(adjl)


#Just for ref for  using []
# def add_edge(adj, i, j):
#     adj[i].append(j)
#     adj[j].append(i)

# def display_adj_list(adj):
#     for i in range(len(adj)):
#         print(f"{i}: ", end="")
#         for j in adj[i]:
#             print(j, end=" ")
#         print()

# V = 4
# adj = [[] for _ in range(V)]  # create 4 empty lists

# add_edge(adj, 0, 1)
# add_edge(adj, 0, 2)
# add_edge(adj, 1, 2)
# add_edge(adj, 2, 3)

# print("Adjacency List Representation:")
# display_adj_list(adj)
