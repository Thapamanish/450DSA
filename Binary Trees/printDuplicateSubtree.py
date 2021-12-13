"""Question:  find the dubplicate subtreea in  a tree
    
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

# intution : use the concept of preorder traversal.




class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def findDuplicateUtil(root, mp, ans):
    if not root:
        return ''


    nodeStr = str(root.data) + ' '
    nodeStr += findDuplicateUtil(root.left, mp, ans) + ' '  
    nodeStr += findDuplicateUtil(root.right, mp, ans) + ' '


    if nodeStr in mp:
        if mp[nodeStr] == 1:
            ans.append(list(map(int, nodeStr.split())))
        mp[nodeStr] += 1

    else:
        mp[nodeStr] = 1

    return nodeStr
        

def findDuplicate(root):
    mp = {}
    ans = []
    findDuplicateUtil(root, mp, ans)

    return ans


root = Node(1)
root.left = Node(20)
root.right = Node(3)
root.left.left = Node(4)
root.right.left = Node(20)
root.right.left.left = Node(4)
root.right.right = Node(4)
print(findDuplicate(root))

