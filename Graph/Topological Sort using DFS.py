from collections import defaultdict 

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)


    def addEdge(self, u, v):
        self.graph[u].append(v)


    def topologicalSortUtil(self, v, visited, stack):
        visited.add(v)

        for neighbor in self.graph[v]:
            if neighbor not in visited:
                self.topologicalSortUtil(neighbor, visited, stack)

        stack.append(v)

    def topologicalSort(self):
        visited = set()
        stack = []
        for vertex in list(self.graph):
            if vertex not in visited:
                self.topologicalSortUtil(vertex, visited, stack)

        print(*stack[::-1])

g = Graph()
g.addEdge(5, 2)
g.addEdge(5, 0)
g.addEdge(4, 0)
g.addEdge(4, 1)
g.addEdge(2, 3)
g.addEdge(3, 1)
g.topologicalSort()