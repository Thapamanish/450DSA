# https://www.geeksforgeeks.org/lowest-common-ancestor-binary-tree-set-1/

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def LCA(root, n1, n2):
    if root is None:
        return None

    if root.data == n1 or root.data == n2:
        return root

    leftLCA = LCA(root.left, n1, n2)
    rightLCA = LCA(root.right, n1, n2)


    if leftLCA and rightLCA:
        return root

    return leftLCA if leftLCA is not None else rightLCA





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

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.right.left = Node(5)
root.right.right = Node(6)
root.right.left.left = Node(7)
root.right.left.right = Node(8)


print(LCA(root,7,8).data)
print(LCA(root,7,6).data)
print(LCA(root,4,6).data)
print(LCA(root,7,1).data)
print(LCA(root,4,0).data)

