# """Question:  whether the tree is a sum tree or not
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

# # intution : use the concept of making a sumTree

class Node:
  def __init__(self, data):
    self.data = data
    self.left = None
    self.right = None

def checkSumTree(root):
  if not root:
    return 0

  if not root.left and not root.right:
    return root.data

  if root.data == checkSumTree(root.left) + checkSumTree(root.right):
    return 2 * root.data

  return float('-INF')

def isSumTree(root):
  return checkSumTree(root) != float('-INF')

# root = Node(1)
# root.left = Node(2)
# root.right = Node(3)
# root.left.left = Node(4)
# root.right.left = Node(5)
# root.right.right = Node(6)
# root.right.left.left = Node(7)
# root.right.left.right = Node(8)

root = Node(26)
root.left= Node(10)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(6)
root.right.right = Node(3)

print(isSumTree(root))


