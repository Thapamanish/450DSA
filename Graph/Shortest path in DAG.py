from collections import defaultdict

class Graph:
    def __init__(self, vertices):
        self.graph = defaultdict(list)
        self.V = vertices

    def addEdge(self, u, v, w):
        self.graph[u].append((v,w))

    def topologicalsortUtil(self, v, visited, stack):
        visited[v] = True

        if v in self.graph.keys():
            for neighbor, weight in self.graph[v]:
                if visited[neighbor] == False:
                    self.topologicalsortUtil(neighbor, visited, stack)

        stack.append(v)

    def shortestPath(self, s):
        visited = [False] * self.V
        stack = []

        for i in range(self.V):
            if visited[i] == False:
                self.topologicalsortUtil(s, visited, stack)

        dist = [float('inf')] * self.V
        dist[s] = 0

        while stack:
            i = stack.pop()

            for neighbor, weight in self.graph[i]:
                if dist[i] + weight < dist[neighbor]:
                    dist[neighbor] = dist[i] + weight

        print(*dist)

g = Graph(6)
g.addEdge(0, 1, 5)
g.addEdge(0, 2, 3)
g.addEdge(1, 3, 6)
g.addEdge(1, 2, 2)
g.addEdge(2, 4, 4)
g.addEdge(2, 5, 2)
g.addEdge(2, 3, 7)
g.addEdge(3, 4, -1)
g.addEdge(4, 5, -2)
g.shortestPath(1)
 