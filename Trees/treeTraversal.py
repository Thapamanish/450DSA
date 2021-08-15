
""" Construct the following tree
           1
         /   \
        /     \
       2       3
      /      /   \
     /      /     \
    4      5       6
          / \
         /   \
        7     8
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def inorderTraversal(root):
    if root == None:
        return 

    inorderTraversal(root.left)
    print(root.data, end = ' ')
    inorderTraversal(root.right)

def preorderTraversal(root):
    if root == None:
        return 

    print(root.data, end = ' ')
    preorderTraversal(root.left)
    preorderTraversal(root.right)

def postorderTraversal(root):
    if root == None:
        return 

    postorderTraversal(root.left)
    postorderTraversal(root.right)
    print(root.data, end = ' ')



root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.right.left = Node(5)
root.right.right = Node(6)
root.right.left.left = Node(7)
root.right.left.right = Node(8)

print("Inorder Traversal of the tree")
inorderTraversal(root)
print()

print("Preorder Traversal of the tree")
preorderTraversal(root)
print()

print("Postorder Traversal of the tree")
postorderTraversal(root)
print()