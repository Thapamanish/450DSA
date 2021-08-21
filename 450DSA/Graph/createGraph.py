from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def printGraph(self):
        for vertex in list(self.graph):
            print(f'{vertex} : ', end = ' ')
            for neighbor in self.graph[vertex]:
                print(neighbor, end = ' ')

            print()





g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 4)
g.addEdge(1, 2)
g.addEdge(2, 3)
g.addEdge(4, 5)

g.printGraph()