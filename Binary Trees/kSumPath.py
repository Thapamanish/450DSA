"""Question:  find the path whose sum is equal to K
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


# Time complexity: O(n * h) 
                  
# Auxiliary Space: O(n) i.e. height of the tree

# intution : use the concept of preorder traversal


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def kPathUtil(root, path, k):
    global ans

    if not root:
        return

    path.append(root.data)

    kPathUtil(root.left, path, k)
    kPathUtil(root.right, path, k)



    temp = 0

    for j in range(len(path) - 1, -1, -1):
        temp += path[j]

        if temp == k:
            ans.append(list(path[j:]))


    path.pop(-1)



def kPath(root, k):
    path = []
    kPathUtil(root, path, k)

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.right.left = Node(5)
root.right.right = Node(6)
root.right.left.left = Node(7)
root.right.left.right = Node(8)

ans = []
k = 9
kPath(root, k)
print(ans)






