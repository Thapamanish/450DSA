"""Question:  print left view
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

# intution : basically question means to print the first node at every level from the left 
             # side of the tree


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def leftViewUtil(root, level, levelDict):
    if root is None:
        return 

    if level not in levelDict:
        levelDict[level] = root.data

    leftViewUtil(root.left, level + 1, levelDict)
    leftViewUtil(root.right, level + 1, levelDict)


def leftView(root):  
    levelDict = {}
    leftViewUtil(root, 1, levelDict)
    levelDict = list(levelDict.values())
    return levelDict



root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.right.left = Node(5)
root.right.right = Node(6)
root.right.left.left = Node(7)
root.right.left.right = Node(8)


print(*leftView(root))