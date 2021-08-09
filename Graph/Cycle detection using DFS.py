from collections import defaultdict 
   
class Graph: 
   
    def __init__(self): 
        self.graph = defaultdict(list) 
  
   
    def addEdge(self,u,v): 
        self.graph[u].append(v)  
        self.graph[v].append(u) 


    def isCyclicUtil(self,v,visited, parent):
        visited.add(v)
        for neighbor in self.graph[v]:
            if neighbor not in visited:
                if(self.isCyclicUtil(neighbor, visited, v)):
                    return True
            elif parent != neighbor:
                return True 
        return False



   
    def isCyclic(self):  
        visited = set()  
        for vertex in list(self.graph): 
            if vertex not in visited:
                if(self.isCyclicUtil(vertex ,visited, -1))== True: 
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
g1.addEdge(2,3)
g1.addEdge(3,4)
g1.addEdge(4,5)
g1.addEdge(5,2)


if g1.isCyclic(): 
    print ("Graph contains cycle")
else : 
    print("Graph does not contain cycle ")
   