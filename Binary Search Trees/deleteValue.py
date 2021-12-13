class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None



def insert(root, data):
    if root is None:
        return Node(data)

    if data == root.data:
        return root
    elif data < root.data:
        root.left = insert(root.left, data)
    elif data > root.data:
        root.right = insert(root.right, data)

    return root


def printGraph(root):
    if root:
        printGraph(root.left)
        print(root.data, end = ' ')
        printGraph(root.right)


def minNode(root):
    current = root
    while current.left:
        current = current.left

    return current


def deleteNode(root, key):
    if root is None:
        return root

    if key < root.data:
        root.left = deleteNode(root.left, key)

    elif key > root.data:
        root.right = deleteNode(root.right, key)

    else:

        if root.left is None:
            temp = root.right
            root = None
            return temp

        if root.right is None:
            temp = root.left
            root = None
            return temp


        temp = minNode(root.right)

        root.data = temp.data

        root.right = deleteNode(root.right, temp.data)

    return root




root = None
root = insert(root, 50)
root = insert(root, 30)
root = insert(root, 20)
root = insert(root, 40)
root = insert(root, 70)
root = insert(root, 60)
root = insert(root, 80)
printGraph(root)

print("\nDelete 20")
root = deleteNode(root, 20)
print("Inorder traversal of the modified tree")
printGraph(root)
 
print("\nDelete 30")
root = deleteNode(root, 30)
print("Inorder traversal of the modified tree")
printGraph(root)

print("\nDelete 50")
root = deleteNode(root, 50)
print("Inorder traversal of the modified tree")
printGraph(root)