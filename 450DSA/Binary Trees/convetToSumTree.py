# """Question:  convert it to a sum tree
#                            1
#                          /   \
#                         /     \
#                        2       3
#                       /      /   \
#                      /      /     \
#                     4      5       6
#                           / \
#                          /   \
#                         7     8
# """


# # Time complexity: O(n) 
                  
# # Auxiliary Space: O(n) i.e. height of the tree

# # intution : postorder traversal

class Node:
  def __init__(self, data):
    self.data = data
    self.left = None
    self.right = None

def inorderTraversal(root):
  if not root:
    return

  print(root.data, end = ' ')
  inorderTraversal(root.left)
  inorderTraversal(root.right)


def toSumTree(root):
  if not root:
    return 0

  left = toSumTree(root.left)
  right = toSumTree(root.right)

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

toSumTree(root)
inorderTraversal(root)