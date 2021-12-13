"""Question:  find the distance between two nodes
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

# intution : use the concept of lca.

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def LCA(root, n1, n2):
    if not root or root.data == n1 or root.data == n2:
        return root

    leftLCA = LCA(root.left, n1, n2)
    rightLCA = LCA(root.right, n1, n2)

    if not leftLCA:
        return rightLCA

    elif not rightLCA:
        return leftLCA

    else:
        return root

def findLevel(root, n, dis, level):
    if not root:
        return 

    if root.data == n:
        dis.append(level)

    findLevel(root.left, n, dis, level + 1)
    findLevel(root.right, n, dis, level + 1)


def findDistance(root, n1, n2):
    lca = LCA(root, n1, n2)

    d1 = []
    d2 = []

    if lca:
        findLevel(lca, n1, d1, 0)
        findLevel(lca, n2, d2, 0)
        return d1[0] + d2[0]

    else:
        return -1


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.right.left = Node(5)
root.right.right = Node(6)
root.right.left.left = Node(7)
root.right.left.right = Node(8)

print(findDistance(root, 8, 6))
