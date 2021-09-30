"""Question:  Maximum sum of nodes in Binary tree such that no two are adjacent
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

# intution : use the concept of dynamic programming as in max sum of adjacent
            #element in an array




class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def maxSumUtil(root):
    if not root:
        dpSum = [0 , 0]
        return dpSum

    sum1 = maxSumUtil(root.left)
    sum2 = maxSumUtil(root.right)
    dpSum = [0, 0]

    dpSum[0] = sum1[1] + sum2[1] + root.data

    dpSum[1] = max(sum1[0], sum1[1]) + max(sum2[0], sum2[1])

    return dpSum

def maxSum(root):
    res = maxSumUtil(root)
    return max(res[0], res[1])


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.right.left = Node(5)
root.right.right = Node(6)
root.right.left.left = Node(7)
root.right.left.right = Node(8)


print(maxSum(root))


