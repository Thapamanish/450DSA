"""Question:  print bottom view
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

# Time complexity: O(n) + O(nlogn) i.e. nlogn for sorting
                  
# Auxiliary Space: O(n) i.e. height of the tree

# intution : use level order traversal and use the horizontal distance concept from 
            # vertical traversal

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.hd = 0


def bottomView(root):
    if not root:
        return

    queue = []
    queue.append(root)
    mp = {}

    while queue:
        node = queue.pop(0)
        hd = node.hd

        mp[hd] = node.data

        if node.left:
            node.left.hd = hd - 1
            queue.append(node.left)

        if node.right:
            node.right.hd = hd + 1
            queue.append(node.right)


    ans = []
    for i in sorted(mp):
        ans.append(mp[i])
    return ans



root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.right.left = Node(5)
root.right.right = Node(6)
root.right.left.left = Node(7)
root.right.left.right = Node(8)

print(*bottomView(root))