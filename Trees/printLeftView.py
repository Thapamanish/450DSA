# https://www.techiedelight.com/print-left-view-of-binary-tree/


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def leftTree(root, level, levelDict):
    if root is None:
        return 

    if level not in levelDict:
        levelDict[level] = root.data

    leftTree(root.left, level + 1, levelDict)
    leftTree(root.right, level + 1, levelDict)


def printLeftView(root):  
    levelDict = {}
    leftTree(root, 1, levelDict)
    levelDict = list(levelDict.values())
    return levelDict





""" Construct the following tree
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

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.right.left = Node(5)
root.right.right = Node(6)
root.right.left.left = Node(7)
root.right.left.right = Node(8)


print(*printLeftView(root))