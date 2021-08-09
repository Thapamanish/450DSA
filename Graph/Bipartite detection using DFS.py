from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def bipartiteUtil(self, v, color):
        for neighbor in self.graph[v]:
            if color[neighbor] == -1:
                color[neighbor] = 1 - color[v]
                if not self.bipartiteUtil(neighbor, color):
                    return False

            elif color[neighbor] == color[v]:
                return False
        return True


    def bipartite(self):
        color = [-1] * len(self.graph)
        for vertex in list(self.graph):
            if color[vertex] == -1:
                color[vertex] = 0
                if self.bipartiteUtil(vertex, color):
                    return True
        return False

g = Graph() 
g.addEdge(0, 1)
g.addEdge(1, 2)
g.addEdge(2, 3)


  
if g.bipartite(): 
    print("Graph is bipartite")
else : 
    print ("Graph is not bipartite")



g1 = Graph() 
g1.addEdge(0,1) 
g1.addEdge(1,2) 
g1.addEdge(2,3)
g1.addEdge(3,4)
g1.addEdge(4,5)
g1.addEdge(5,3)


if g1.bipartite(): 
    print("Graph is bipartite")
else : 
    print ("Graph is not bipartite")
