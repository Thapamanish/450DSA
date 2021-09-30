  
from collections import defaultdict 

class Graph:
    def __init__(self, vertices):
        self.graph = defaultdict(list)
        self.V = vertices

    def addEdge(self, u, v):
        self.graph[u].append(v)


    def cycleDetect(self):
        inDegree = [0] * self.V

        for vertex in self.graph:
            for neighbor in self.graph[vertex]:
                inDegree[neighbor] += 1

        queue = []
        for vertex in range(self.V):
            if inDegree[vertex] == 0:
                queue.append(vertex)

        cnt = 0


        while queue:
            s = queue.pop(0)

            for neighbor in self.graph[s]:
                inDegree[neighbor] -= 1
                if inDegree[neighbor] == 0:
                    queue.append(neighbor)

            cnt += 1


        if cnt == self.V:
            return False
        else:
            return True
            



g = Graph(6)
g.addEdge(5, 2);
g.addEdge(5, 0);
g.addEdge(4, 0);
g.addEdge(4, 1);
g.addEdge(2, 3);
g.addEdge(3, 1);

if g.cycleDetect():
    print("Cycle detected")
else:
    print("Cycle not detected")