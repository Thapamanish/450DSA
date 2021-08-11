from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)


    def addEdge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)


    def dfsUtil(self, v, visited):
        visited.add(v)
        print(v)

        for neighbor in self.graph[v]:
            if neighbor not in visited:
                self.dfsUtil(neighbor, visited)


    def dfs(self):
        visited = set()

        for vertex in list(self.graph):
            if vertex not in visited:
                self.dfsUtil(vertex, visited)



g = Graph()
g.addEdge(1,2)
g.addEdge(2,4)
g.addEdge(2,7)
g.addEdge(4,1)
g.addEdge(6,7)
g.dfs()