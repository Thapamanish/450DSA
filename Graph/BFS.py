from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def bfsUtil(self, v, visited):
        queue = []
        queue.append(v)
        visited.add(v)

        while queue:
            s = queue.pop(0)
            print(s)
            for neighbor in self.graph[s]:
                if neighbor not in visited:
                    queue.append(neighbor)
                    visited.add(neigbhor)


    def bfs(self):
        visited = set()
        for vertex in list(self.graph):
            if vertex not in visited:
                self.bfsUtil(vertex, visited)



g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 7)
g.addEdge(6, 7)
 

g.bfs()