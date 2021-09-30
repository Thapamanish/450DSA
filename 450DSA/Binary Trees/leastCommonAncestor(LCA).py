"""Question:  find the least common ancestor of two nodes 
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

# intution : use the concept of dfs.


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def lca(root, n1, n2):
    if not root or root.data == n1 or root.data == n2:
        return root

    leftLCA = lca(root.left, n1, n2)
    rightLCA = lca(root.right, n1, n2)

    if not leftLCA:
        return rightLCA

    elif not rightLCA:
        return leftLCA

    else:
        return root


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.right.left = Node(5)
root.right.right = Node(6)
root.right.left.left = Node(7)
root.right.left.right = Node(8)

print(lca(root, 8, 6).data)



