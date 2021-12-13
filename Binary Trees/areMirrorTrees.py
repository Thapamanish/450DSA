"""Question:  whether the trees are mirror or not
                          1                     1
                         / \                   / \
                        /   \                 /   \
                       2       3             3     2
                      / \                         / \
                     /   \                       /   \
                    4      5                    5     4

"""


# Time complexity: O(n) 
                  
# Auxiliary Space: O(n) i.e. height of the tree

# intution : use the concept of checking the tree is identical or not.


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None




    
def areMirrorUtil(root1, root2):
    if not root1 and not root2:
        return True
        
    return root1 and root2 and root1.data == root2.data and areMirrorUtil(root1.left, root2.right) and areMirrorUtil(root1.right, root2.left) 
    
def areMirror(root1,root2):
    
    return areMirrorUtil(root1, root2)



root1 = Node(1)
root2 = Node(1)
 
root1.left = Node(2)
root1.right = Node(3)
root1.left.left = Node(4)
root1.left.right = Node(5)
 
root2.left = Node(3)
root2.right = Node(2)
root2.right.left = Node(5)
root2.right.right = Node(4)


print(areMirror(root1, root2))


    
