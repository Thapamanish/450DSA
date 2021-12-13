"""Question:  zigzag traversal of the tree
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
                  
# Auxiliary Space: O(n) + O(n) 

# intution : use a flag variable to toggle between traversal from left to right and 
            # right to left.


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def zigZagTraversal(root):
    if not root:
        return

    currentLevel = []
    currentLevel.append(root)
    nextLevel = []
    ans = []

    flag = True

    while currentLevel:
        node = currentLevel.pop()
        ans.append(node.data)
        
        if flag:
            if node.left:
                nextLevel.append(node.left)

            if node.right:
                nextLevel.append(node.right)

        else:
            if node.right:
                nextLevel.append(node.right)

            if node.left:
                nextLevel.append(node.left)


        if not currentLevel:
            flag = not flag

            currentLevel, nextLevel = nextLevel, currentLevel

    return ans


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.right.left = Node(5)
root.right.right = Node(6)
root.right.left.left = Node(7)
root.right.left.right = Node(8)

print(*zigZagTraversal(root))
