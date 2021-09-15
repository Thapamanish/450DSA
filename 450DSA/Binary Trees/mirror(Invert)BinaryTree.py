"""Question:  mirror (Invert) the tree below
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
                  
# Auxiliary Space: O(n) i.e call stack(height of tree)

# intution : use postorder traversal and swap the two left
            # and right nodes



class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def inorderTraversal(root):
    if root:
        inorderTraversal(root.left)
        print(root.data, end = ' ')
        inorderTraversal(root.right)


def mirror(root):
    if not root:
        return

    mirror(root.left)
    mirror(root.right)
    root.left, root.right = root.right, root.left




root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.right.left = Node(5)
root.right.right = Node(6)
root.right.left.left = Node(7)
root.right.left.right = Node(8)

inorderTraversal(root)
mirror(root)
print()
inorderTraversal(root)
