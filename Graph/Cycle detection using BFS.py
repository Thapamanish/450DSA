from collections import defaultdict 
   
class Graph: 
   
    def __init__(self): 
        self.graph = defaultdict(list) 
  
   
    def addEdge(self,u,v): 
        self.graph[u].append(v)  
        self.graph[v].append(u) 


    def isCyclicUtil(self,v,visited): 
        queue = []
        queue.append(v)
        visited.add(v)
        parent = [-1] * len(self.graph)
  
        while queue:
            s = queue.pop(0)
            for neighbor in self.graph[s]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
                    parent[neighbor] = s
                elif parent[s] != neighbor:
                    return True

        return False


   
    def isCyclic(self):  
        visited = set()  
        for vertex in list(self.graph): 
            if vertex not in visited:
                if(self.isCyclicUtil(vertex ,visited))== True: 
                    return True
          
        return False
  


g = Graph() 
g.addEdge(0, 1)
g.addEdge(1, 2)
g.addEdge(2, 3) 
  
if g.isCyclic(): 
    print("Graph contains cycle")
else : 
    print ("Graph does not contain cycle ")



g1 = Graph() 
g1.addEdge(0,1) 
g1.addEdge(1,2) 
g1.addEdge(2,0) 

if g1.isCyclic(): 
    print ("Graph contains cycle")
else : 
    print("Graph does not contain cycle ")
   