"""Question:  find the Kth ancestor of a node.
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


def findKAncestor(root, n, k):
    if not root:
        return

    if root.data == n or findKAncestor(root.left, n, k) or findKAncestor(root.right, n, k):
        if k[0] > 0:
            k[0] -= 1

        else:
            print('kth ancestor is :', root.data)
            return

        return root

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.right.left = Node(5)
root.right.right = Node(6)
root.right.left.left = Node(7)
root.right.left.right = Node(8)
k = [2]
print(findKAncestor(root, 7, k))
