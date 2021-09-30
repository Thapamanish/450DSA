"""Question:  whether the trees are isomorphic or not

                                    1                     1
                                   /  \                 /  \
                                  /    \               /    \
                                 2      3             3      2
                                / \    /               \    / \
                               /   \  /                 \  /   \ 
                              4    5  6                 6  4    5
                                  / \                          / \
                                 /   \                        /   \
                                7     8                      8     7
"""


# Time complexity: O(min(m, n) ^ 2) 
                  
# Auxiliary Space: O(n) i.e. height of the tree

# intution : use the concept of dfs.



class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def isIsomorphic(root1, root2):
    if not root1 and not root2:
        return True

    if not root1 or not root2:
        return False

    if root1.data != root2.data:
        return False

    return isIsomorphic(root1.left, root2.left) and isIsomorphic(root1.right, root2.right) or \
            isIsomorphic(root1.left, root2.right) and isIsomorphic(root1.right, root2.left)

n1 = Node(1)
n1.left = Node(2)
n1.right = Node(3)
n1.left.left = Node(4)
n1.left.right = Node(5)
n1.right.left = Node(6)
n1.left.right.left = Node(7)
n1.left.right.right = Node(8)
 
n2 = Node(1)
n2.left = Node(3)
n2.right = Node(2)
n2.right.left = Node(4)
n2.right.right = Node(5)
n2.left.right = Node(6)
n2.right.right.left = Node(8)
n2.right.right.right  = Node(7)


print(isIsomorphic(n1, n2))
