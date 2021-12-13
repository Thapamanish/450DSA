# """Question:  convert to the binary search tree in minmam swaps
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


# Time complexity: O(nlogn) 
                  
# Auxiliary Space: O(n) i.e. height of the tree

# intution : use the concept of min swap required to sort an array

class Node:
  def __init__(self, data):
    self.data = data
    self.left = None
    self.right = None


def extractKeys(root, inorder):
  if not root:
    return

  extractKeys(root.left, inorder)
  inorder.append(root.data)
  extractKeys(root.right, inorder)



def convertToBST(root):
  inorder = []
  extractKeys(root, inorder)
  inorderBST = sorted(inorder)

  mp = {}
  for ind, num in enumerate(inorder):
    mp[num] = ind

  cnt = 0

  for i in range(len(inorder)):
    if inorder[i] != inorderBST[i]:
      cnt += 1
      init = inorder[i]

      inorder[i], inorder[mp[inorderBST[i]]] = inorder[mp[inorderBST[i]]], inorder[i]

      mp[init] = mp[inorderBST[i]]
      mp[inorderBST[i]] = i

  return cnt




root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.right.left = Node(5)
root.right.right = Node(6)
root.right.left.left = Node(7)
root.right.left.right = Node(8)



print(convertToBST(root))



