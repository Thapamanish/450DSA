"""Question:  Sum of the Longest Bloodline of a Tree (Sum of nodes on the 
                longest path from root to leaf node)
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

# intution : use the concept of maxlevel and keep the track of max path.

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def sumOfNodesUtil(root, level, nodeSum, ans):
    global maxlevel
    if not root:
        return 0

    nodeSum += root.data

    if level > maxlevel:
        maxlevel = level
        ans[0] = nodeSum

    elif level == maxlevel:
        ans[0] = max(ans[0], nodeSum)

    sumOfNodesUtil(root.left, level + 1, nodeSum, ans)
    sumOfNodesUtil(root.right, level + 1, nodeSum, ans)

def sumOfNodes(root):
    level = 0
    ans = [float('-INF')]
    nodeSum = 0
    sumOfNodesUtil(root, level, nodeSum, ans)
    return ans[0]


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.right.left = Node(5)
root.right.right = Node(6)
root.right.left.left = Node(7)
root.right.left.right = Node(8)
maxlevel = 0

print(sumOfNodes(root))

