"""Question:  whether the tree is balanced or not ?
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

# intution : use the concept of finding the height of the tree.


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def dfsHeight(root):
    if not root:
        return 0

    lDepth = dfsHeight(root.left)
    if lDepth == -1:
        return -1

    rDepth = dfsHeight(root.right)
    if rDepth == -1:
        return -1

    if abs(lDepth - rDepth) > 1: 
        return -1

    return 1 + max(lDepth, rDepth)





def isBalanced(root):
    if not root:
        return
    return dfsHeight(root) != -1


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.right.left = Node(5)
root.right.right = Node(6)
root.right.left.left = Node(7)
root.right.left.right = Node(8)

print(isBalanced(root))
