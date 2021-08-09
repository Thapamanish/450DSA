class Graph:
    def __init__(self):
        self.graph = defaultdict(list)


    def addEdges(self, u, v):
        self.graph[u].append(v)


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
g.addEdges(1,2)
g.addEdges(2,4)
g.addEdges(2,7)
g.addEdges(4,1)
g.addEdges(6,7)
g.dfs()