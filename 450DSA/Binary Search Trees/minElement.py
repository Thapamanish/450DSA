class Node:
	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None


def insert(root, data):
	if not root:
		return Node(data)
	else:
		if data == root.data:
			return root
		elif data < root.data:
			root.left = insert(root.left, data)

		else:
			root.right = insert(root.right, data)

	return root


def printBST(root):
	if root:
		printBST(root.left)
		print(root.data, end = ' ')
		printBST(root.right)

def minElement(root):
	if not root.left:
		return root.data
	return minElement(root.left)


r = None
r = insert(r, 14)
r = insert(r, 10)
r = insert(r, 40)
r = insert(r, 60)
r = insert(r, 80)
r = insert(r, 2)
r = insert(r, 11)
r = insert(r, 67)

printBST(r)
print()
print(minElement(r))