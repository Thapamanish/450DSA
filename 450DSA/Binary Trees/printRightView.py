"""Question:  print right view
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

# intution : basically question means to print the first node at every level from the right 
             # side of the tree


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def rightViewUtil(root, level, ans):
    if not root:
        return

    if len(ans) == level:
        ans.append(root.data)

    rightViewUtil(root.right, level + 1, ans)
    rightViewUtil(root.left, level + 1, ans)


def rightView(root):
    if not root:
        return

    ans = []
    rightViewUtil(root, 0, ans)
    return ans




root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.right.left = Node(5)
root.right.right = Node(6)
root.right.left.left = Node(7)
root.right.left.right = Node(8)

print(*rightView(root))
