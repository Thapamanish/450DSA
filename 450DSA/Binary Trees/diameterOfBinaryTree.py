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
                  
# Auxiliary Space: O(n)

# intution : find max height of left and right subtree and tree and add them
            # to find the diameter



class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def diameter(root, maxDia):
    if not root:
        return 0

    lDepth = diameter(root.left, maxDia)
    rDepth = diameter(root.right, maxDia)
    maxDia[0] = max(maxDia[0], lDepth + rDepth + 1)

    return 1 + max(lDepth, rDepth)





root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.right.left = Node(5)
root.right.right = Node(6)
root.right.left.left = Node(7)
root.right.left.right = Node(8)
maxDia = [0]
diameter(root, maxDia)
print(maxDia[0])