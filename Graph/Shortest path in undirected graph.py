from collections import defaultdict

class Graph:
    def __init__(self, vertices):
        self.graph = defaultdict(list)
        self.V = vertices

    def addEdge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def shortestPath(self, src):
        queue = []
        dist = [1000000] * self.V

        dist[src] = 0
        queue.append(src)
        while queue:
            s = queue.pop(0)
            for neighbor in self.graph[s]:
                if dist[s] + 1 < dist[neighbor]:
                    dist[neighbor]  = dist[s] + 1
                    queue.append(neighbor)

        print(*dist)



g = Graph(8)
g.addEdge(0,1)
g.addEdge(0,3)
g.addEdge(1,2)
g.addEdge(3,4)
g.addEdge(3,7)
g.addEdge(4,5)
g.addEdge(4,6)
g.addEdge(4,7)
g.addEdge(5,6)
g.addEdge(6,7)


g.shortestPath(0)