from collections import deque

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None #Optional  (to support deletion)
    
    def add_child(self, child):
        child.parent = self #upward link
        self.children.append(child) #add to children 

    def remove_child(self, child):
        if child in self.children:
            self.children.remove(child)
            child.parent = None

#A Tree that keeps a reference to the root
class Tree:
    def __init__(self, root_data):
        if root_data is not None:
            self.root = TreeNode(root_data)
        else:
            self.root = None
    
    #Recursive DFS: search tree by value
    #Find a node (DFS, returns first match)
    def recursive_dfs(self, node, value):
        if node is None:
            return None
        if node.data == value:
            return node
        for c in node.children:
            res = self.recursive_dfs(c, value)
            if res:
                return res
        return None
    def find(self, value):
        return self.recursive_dfs(self.root, value)
        
    #Insert (add child by parent value) Find the parent, create new node, attach it
    def  add(self, parent_data, child_data):
        if self.root is None:
            raise ValueError("Tree has no root")
        parent = self.find(parent_data)
        if parent is None:
            raise ValueError("Parent isn't found")
        child = TreeNode(child_data)
        parent.add_child(child)
        return child
