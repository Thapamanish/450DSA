"""Question:  reverse level order
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
                  
# Auxiliary Space: O(n)

# intution : same as level order traversal but append right child first
            # and store the poped element in stack which is reversed to
            # obtain the ansi.e. BFS concept



class Node:
  def __init__(self, data):
    self.data = data
    self.left = None
    self.right = None



def reverseLevelO(root):
  if not root:
    return

  queue = []
  queue.append(root)
  ans = []

  while queue:
    node = queue.pop(0)
    ans.append(node.data)

    if node.right:
      queue.append(node.right)

    if node.left:
      queue.append(node.left)

  while ans:
    print(ans.pop(), end = ' ')




root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.right.left = Node(5)
root.right.right = Node(6)
root.right.left.left = Node(7)
root.right.left.right = Node(8)

reverseLevelO(root)       
