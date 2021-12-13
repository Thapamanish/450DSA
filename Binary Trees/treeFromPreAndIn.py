# """Question:  construct a Tree from inorder and preorder
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


# Time complexity: O(n) 
                  
# Auxiliary Space: O(n) i.e. height of the tree

# intution : find the element of preorder in inorder and divide into left subtree and 
            # right subTree


class Node:
  def __init__(self, data):
    self.data = data
    self.right = None
    self.left = None

def postOrderTraversal(root):
  if not root:
    return

  postOrderTraversal(root.left)
  postOrderTraversal(root.right)
  print(root.data, end = ' ')


def contructTreeUtil(start, end, preorder, preIndex, mp):
  if start > end:
    return None, preIndex

  root = Node(preorder[preIndex])

  preIndex += 1
  index = mp[root.data]

  root.left, preIndex = contructTreeUtil(start, index - 1, preorder, preIndex, mp)
  root.right, preIndex = contructTreeUtil(index + 1, end, preorder, preIndex, mp)

  return root, preIndex  

def contructTree(inorder, preorder):
  mp = {}

  for ind, num in enumerate(inorder):
    mp[num] = ind

  preIndex = 0
  root = contructTreeUtil(0, len(inorder) - 1, preorder, preIndex, mp)[0]
  return root

inorder = [4,2,1,7,5,8,3,6]
preorder = [1,2,4,3,5,7,8,6]
root = contructTree(inorder, preorder)

postOrderTraversal(root)
