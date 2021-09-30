"""Question:  Construct the following tree
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
                  
# Auxiliary Space: O(n) i.e. call stack

# intution : use recurrsion i.e. DFS concept

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def maxDepth(root):
    if root is None:
        return 0

    lDepth = maxDepth(root.left)
    rDepth = maxDepth(root.right)

    return 1 + max(lDepth, rDepth)




root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.right.left = Node(5)
root.right.right = Node(6)
root.right.left.left = Node(7)
root.right.left.right = Node(8)

print("The height of the tree is", maxDepth(root))
