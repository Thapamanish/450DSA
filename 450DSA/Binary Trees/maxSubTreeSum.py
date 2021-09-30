"""Question:  find the subtree with max sum
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

# intution : use the concept of dfs




class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
def maxSumSubTreeUtil(root, ans):
    if not root:
        return 0

    subTreeSum = root.data + maxSumSubTreeUtil(root.left, ans) \
                    + maxSumSubTreeUtil(root.right, ans)

    ans[0] = max(ans[0], subTreeSum)

    return subTreeSum


def maxSumSubTree(root):
    ans = [float('-INF')]

    maxSumSubTreeUtil(root, ans)

    return ans[0]





root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.right.left = Node(5)
root.right.right = Node(6)
root.right.left.left = Node(7)
root.right.left.right = Node(8)

print(maxSumSubTree(root))


