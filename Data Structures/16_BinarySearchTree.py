class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.value = key

def insert(root, key): #O(n) TC O(1) SC
    if root is None:
        return Node(key)
    if root.value == key:
        return root
    if root.value < key:
        root.right = insert(root.right, key)
    else:
        root.left = insert(root.left, key)
    return root

def search(root, key):
    if root is None or root.key==key:
        return root
    if root.key < key:
        return search(root.left, key)
    return search(root.right, key)


def in_order(root):
    if root:
        in_order(root.left)
        print(root.value, end=" ")
        in_order(root.right)

r = Node(15)
r = insert(r, 10)
r = insert(r, 18)
r = insert(r, 4)
r = insert(r, 11)
r = insert(r, 16)
r = insert(r, 20)
r = insert(r, 13)

# Print inorder traversal of the BST
in_order(r)