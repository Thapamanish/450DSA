"""Question:  level order Traversal
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
                  
# Auxiliary Space: O(1)

# intution : use queue method i.e. BFS concept


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def levelOrder(root):
    if root is None:
        return

    queue = []
    queue.append(root)

    while queue:
        node = queue.pop(0)
        print(node.data, end = ' ')

        if node.left: 
            queue.append(node.left)

        if node.right: 
            queue.append(node.right)



root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.right.left = Node(5)
root.right.right = Node(6)
root.right.left.left = Node(7)
root.right.left.right = Node(8)

levelOrder(root)
print()
