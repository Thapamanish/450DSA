"""Question:  convert string with brackets to a tree
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


# Time complexity: O(n ^ 2) 
                  
# Auxiliary Space: O(n) i.e. height of the tree

# intution : use the concept of finding valid parenthesis.


class Node: 
  def __init__(self, data):
    self.data = data
    self.left = None
    self.right = None


def inorderTraversal(root):
  if not root:
    return

  inorderTraversal(root.left)
  print(root.data, end = ' ')
  inorderTraversal(root.right)

def findIndex(inpStr, si, ei):

  if si > ei:
    return -1


  brackets = []

  while si <= ei:

    if inpStr[si] == '(':
      brackets.append('(')

    elif inpStr[si] == ')':
      if brackets[-1] == '(':
        brackets.pop()

        if len(brackets) == 0:
          return si

    si += 1

  return -1


def stringToTree(inpStr, si, ei):
  if si > ei:
    return

  root = Node(int(inpStr[si]))
  index = -1

  if si + 1 <= ei and inpStr[si + 1] == '(':
    index = findIndex(inpStr, si, ei)


  if index != -1:
    root.left = stringToTree(inpStr, si + 2, index - 1)

    root.right = stringToTree(inpStr, index + 2, ei - 1)


  return root





inpStr = "1(2(4))(3(5(7)(8))(6))"
root = stringToTree(inpStr, 0, len(inpStr) - 1)
inorderTraversal(root)
