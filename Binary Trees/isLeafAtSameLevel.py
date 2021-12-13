# """Question:  is leaf at same level ??
#                            1
#                          /   \
#                         /     \
#                        2       3
#                       /      /   \
#                      /      /     \
#                     4      5       6
#                           / \
#                          /   \
#                         7     8
# """


# # Time complexity: O(n) 
                  
# # Auxiliary Space: O(n) i.e. height of the tree

# # intution : store the leftmost leaf node level and compare it with other leaf 
                # nodes


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None



def isSameLevel(root, level):
    global leafLevel
    if not root:
        return True

    if not root.left and not root.right:
        print(leafLevel, level)
        if leafLevel == 0:
            leafLevel = level

        print(leafLevel)
        return leafLevel == level


    return isSameLevel(root.left, level + 1) and isSameLevel(root.right, level + 1)


def check(root):
    level = 0
    return isSameLevel(root, level)    



root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.right.left = Node(5)
root.right.right = Node(6)
root.right.left.left = Node(7)
root.right.left.right = Node(8)


leafLevel = 0
print(check(root))
