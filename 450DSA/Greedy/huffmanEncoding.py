class Node:
    def __init__(self, freq, symbol, left = None, right = None):
        self.freq = freq
        self.symbol = symbol
        self.left = left
        self.right = right
        self.huff = ''


def printHuffman(node, val = ''):
    newVal = val + str(node.huff)

    if node.left:
        printHuffman(node.left, newVal)
    if node.right:
        printHuffman(node.right, newVal)


    if not node.left and not node.right:
        print(f'{node.symbol} : {newVal}')



def huffmanTree(char, freq, nodes):
    for x in range(len(char)):
        nodes.append(Node(freq[x], char[x]))



    while len(nodes) > 1:
        nodes.sort(key = lambda x : x.freq)

        left = nodes[0]
        right = nodes[1]

        left.huff = 0
        right.huff = 1

        newNode = Node(left.freq + right.freq, left.symbol + right.symbol, left, right)
        nodes.remove(left)
        nodes.remove(right)
        nodes.append(newNode)





chars = ['a', 'b', 'c', 'd', 'e', 'f']
 
freq = [ 5, 9, 12, 13, 16, 45]

nodes = []

huffmanTree(chars, freq, nodes)

printHuffman(nodes[0])
