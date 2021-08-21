class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None



def insertion(root, data):
    if root is None:
        return Node(data)
    else:
        if data == root.data:
            return root
        elif data < root.data:
            root.left = insertion(root.left, data)
        else:
            root.right = insertion(root.right, data)

    return root


def printInorder(root):
    if root:
        printInorder(root.left)
        print(root.data, end = ' ')
        printInorder(root.right)



def search(root, key):
    if root is None or root.data == key:
        return root
    elif key < root.data:
        return search(root.left, key)
    else:
        return search(root.right, key)


r = Node(50)
r = insertion(r, 50)
r = insertion(r, 30)
r = insertion(r, 20)
r = insertion(r, 40)
r = insertion(r, 70)
r = insertion(r, 60)
r = insertion(r, 80)

printInorder(r)
print()
if(search(r, 70)):
    print('Element found')
else:
    print("Element not found")



