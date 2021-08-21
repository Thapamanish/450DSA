class Node:
    def __init__(self):
        self.children = [None] * 26
        self.isEndWord = None


class Trie:
    def __init__(self):
        self.root = self.getNode()


    def getNode(self):
        return Node()

    def charToIndex(self, char):
        return ord(char) - ord('a')


    def insert(self, data):
        current = self.root
        length = len(data)
        for level in range(length):
            index = self.charToIndex(data[level])


            if current.children[index] is None:
                current.children[index] = self.getNode()

            current = current.children[index]


        current.isEndWord = True



    def search(self, key):
        current = self.root
        length = len(key)
        for level in range(length):
            index = self.charToIndex(key[level])

            if current.children[index] is None:
                return False

            current = current.children[index]

        return current.isEndWord



keys = ["the","a","there","anaswe","any",
        "by","their"]
output = ["Not present in trie",
          "Present in trie"]

t = Trie()

for x in keys:
    t.insert(x)


print('the :', output[t.search('the')])
print('these :', output[t.search('these')])
print('their :', output[t.search('their')])
print('thaw :', output[t.search('thaw')])
print('aa :', output[t.search('aa')])
