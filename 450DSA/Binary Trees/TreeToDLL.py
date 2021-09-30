"""Question:  convert the tree below to doubly linkedlist
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


# Time complexity: O(n) 
                  
# Auxiliary Space: O(n) i.e. height of the tree

# intution : use reverse inorder traversal

class Node:
  def __init__(self, data):
    self.data = data
    self.left = None
    self.right = None


def preOrderTraversal(root):
  if not root:
    return 

  print(root.data, end = ' ')
  preOrderTraversal(root.left)
  preOrderTraversal(root.right)

def sumTree(root):
  if not root:
    return 0

  left = sumTree(root.left)
  right = sumTree(root.right)

  old = root.data

  root.data = left + right

  return root.data + old

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.right.left = Node(5)
root.right.right = Node(6)
root.right.left.left = Node(7)
root.right.left.right = Node(8)

sumTree(root)
preOrderTraversal(root)