
"""Question:  whether the graph is a tree of not
  
            1---0---3
           /        |
          2         4

"""


# Time complexity: O(n) 
                  
# Auxiliary Space: O(n) i.e. height of the tree

# intution : use cycle detection algorithm using DFS

from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)



    def addEdge(self, u, v):
        self.graph[u].append(v)
        self.graph[v]. append(u)




    def isTreeUtil(self, v, visited, parent):
        visited.add(v)
        for neighbor in self.graph[v]:
            if neighbor not in visited:
                if self.isTreeUtil(neighbor, visited, v) == True:
                    return True

            elif parent != neighbor:
                return True

        return False

    def isTree(self):
        visited = set()
        for vertex in list(self.graph):
            if vertex not in visited:

                if self.isTreeUtil(vertex, visited, -1) == True:
                    return True

        return False





g1 = Graph() 
g1.addEdge(0,1) 
# g1.addEdge(1,2) 
g1.addEdge(2, 0) 
g1.addEdge(0,3)
g1.addEdge(3,4)
print('Is graph a Tree : ',not g1.isTree())


