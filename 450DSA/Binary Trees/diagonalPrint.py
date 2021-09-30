"""Question:  Print the tree in the diagonal fashion
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

# intution : use the concept of diagonal hashmaps same as level and hd


class Node:
  def __init__(self, data):
    self.data = data
    self.right = None
    self.left = None

def diagonalTraversalUtil(root, d, diagonalMap):
  if not root:
    return 

  if d in diagonalMap:
    diagonalMap[d].append(root.data)
  else:
    diagonalMap[d] = [root.data]

  diagonalTraversalUtil(root.left, d + 1, diagonalMap)
  diagonalTraversalUtil(root.right, d, diagonalMap)



def diagonalTraversal(root):
  diagonalMap = {}
  diagonalTraversalUtil(root, 0, diagonalMap)
  ans = []
  for d in diagonalMap:
    ans += diagonalMap[d]

  return ans

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.right.left = Node(5)
root.right.right = Node(6)
root.right.left.left = Node(7)
root.right.left.right = Node(8)

print(diagonalTraversal(root))


