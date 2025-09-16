from collections import deque

class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data
    
def in_order(node):
    if node is None:
        return
    in_order(node.left)
    print(node.data)
    in_order(node.right)

def pre_order(node):
    if node is None:
        return
    print(node.data)
    pre_order(node.left)
    pre_order(node.right)

def post_order(node):
    if node is None:
        return
    post_order(node.left)
    post_order(node.right)
    print(node.data)

def insert(root, key):
    if root is None:
        return Node(key)
    queue = deque([root])
    while queue:
        temp = queue.popleft()
        if temp.left is None:
            temp.left = Node(key)
            break
        else:
            queue.append(temp.left)
        
        if temp.right is None:
            temp.right = Node(key)
            break
        else:
            queue.append(temp.right)

    return root

#creating BT with nodes 2,3,4,5
# firstNode = Node(2)
# secondNode = Node(3)
# thirdNode = Node(4)
# fourthNode = Node(5)

# firstNode.left = secondNode
# firstNode.right = thirdNode
# secondNode.left = fourthNode
        
class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data
    
def in_order(node):
    if node is None:
        return
    in_order(node.left)
    print(node.data)
    in_order(node.right)

def pre_order(node):
    if node is None:
        return
    print(node.data)
    pre_order(node.left)
    pre_order(node.right)

def post_order(node):
    if node is None:
        return
    post_order(node.left)
    post_order(node.right)
    print(node.data)

#creating BT with nodes 2,3,4,5
# firstNode = Node(2)
# secondNode = Node(3)
# thirdNode = Node(4)
# fourthNode = Node(5)

# firstNode.left = secondNode
# firstNode.right = thirdNode
# secondNode.left = fourthNode
class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data
    
def in_order(node):
    if node is None:
        return
    in_order(node.left)
    print(node.data, end=" ")
    in_order(node.right)

def pre_order(node):
    if node is None:
        return
    print(node.data, end=" ")
    pre_order(node.left)
    pre_order(node.right)

def post_order(node):
    if node is None:
        return
    post_order(node.left)
    post_order(node.right)
    print(node.data, end=" ")

def bfs(root):
    if root is None:
        return
    queue = [root]
    while queue:
        node = queue.pop(0)
        print(node.data, end=" ")
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

#creating BT with nodes 2,3,4,5
# firstNode = Node(2)
# secondNode = Node(3)
# thirdNode = Node(4)
# fourthNode = Node(5)

# firstNode.left = secondNode
# firstNode.right = thirdNode
# secondNode.left = fourthNode
        
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(5)

print("In-order DFS: ", end='')
in_order(root)
print("\nPre-order DFS: ", end='')
pre_order(root)
print("\nPost-order DFS: ", end='')
post_order(root)
print("\nLevel order: ", end='')
bfs(root) #1
          #2 3
          #5
key = 6
root = insert(root, key)

print("Inorder traversal after insertion: ", end="")
in_order(root)