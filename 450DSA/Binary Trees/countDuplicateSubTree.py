"""Question:  whether the tree is balanced or not
                                       1
                                      / \
                                    20   3
                                    /   / \
                                   4  20   4
                                      /
                                     4
"""


# Time complexity: O(n) 
                  
# Auxiliary Space: O(n) i.e. height of the tree

# intution : use the concept of finding the height of the tree.



class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def countDupSubtreeUtil(root, mp, ans):
    if not root:
        return ''

    nodeStr = str(root.data) + ' '
    nodeStr += countDupSubtreeUtil(root.left, mp, ans) + ' '
    nodeStr += countDupSubtreeUtil(root.right, mp, ans) + ' '

    if nodeStr in mp:
        if mp[nodeStr] == 1:
            subTree = list(map(int, nodeStr.split()))
            if len(subTree) > 1:
                ans.append(subTree)

        mp[nodeStr] += 1

    else:

        mp[nodeStr] = 1

    return nodeStr


def countDupSubtree(root):
    mp = {}
    ans = []
    countDupSubtreeUtil(root, mp, ans)

    return len(ans)

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.right.left = Node(2)
root.right.left.left = Node(4)
root.right.right = Node(4)
print(countDupSubtree(root))