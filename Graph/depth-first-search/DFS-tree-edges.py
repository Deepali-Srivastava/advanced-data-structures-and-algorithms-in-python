# Copyright (C) Deepali Srivastava - All Rights Reserved
# This code is part of DSA course available on CourseGalaxy.com  

INITIAL = 0
VISITED = 1
        
class Vertex:
        def __init__(self, name):
           self.name = name
           	  
class DirectedGraph:

        def __init__(self,size=20):
           self._adj = [  [0 for column in range(size)]  for row in range(size) ]
           self._n = 0
           self._vertexList = []
           

        def display(self):
            for i in range(self._n):
                for j in range(self._n):
                   print( self._adj[i][j], end =' ')
                print()


        def numVertices(self):
            return self._n


        def numEdges(self):
            e = 0
            for i in range(self._n):
                for j in range(self._n):
                    if self._adj[i][j]!=0:
                        e+=1
            return e


        def vertices(self):
            return [vertex.name for vertex in self._vertexList]


        def edges(self):
            edges = []
            for i in range(self._n):
                for j in range(self._n):
                   if self._adj[i][j] != 0:
                      edges.append( (self._vertexList[i].name, self._vertexList[j].name) )
            return edges


        def _getIndex(self,s):
            index = 0
            for name in (vertex.name for vertex in self._vertexList):
                if s == name:
                   return index
                index += 1
            return None


        def insertVertex(self,name):
            if name in (vertex.name for vertex in self._vertexList): ######## 
                print("Vertex with this name already present in the graph")
                return
                
            self._vertexList.append( Vertex(name) )  
            self._n += 1


        def removeVertex(self,name):
             u = self._getIndex(name)
             if u is None:
                print("Vertex not present in the graph")
                return
        
             self._adj.pop(u)

             for i in range(self._n):
                  self._adj[i].pop(u)
                  
             for i,vertex in enumerate(self._vertexList):
               if name == vertex.name:
                   self._vertexList.pop(i)
             self._n -= 1
               
    
        def insertEdge(self, s1, s2):
            u = self._getIndex(s1)
            v = self._getIndex(s2)
            if u is None:
                print("Start vertex not present in the graph, first insert the start vertex")
            elif v is None:
                print("End vertex not present in the graph, first insert the end vertex")
            elif u == v:
                print("Not a valid edge") 
            elif self._adj[u][v] != 0 :
    	        print("Edge already present in the graph") 
            else:  
                self._adj[u][v] = 1
                
        
        def removeEdge(self, s1,s2):
             u = self._getIndex(s1)
             v = self._getIndex(s2)
             if u is None:
                print("Start vertex not present in the graph")
             elif v is None:
                print("End vertex not present in the graph")
             elif self._adj[u][v] == 0:
                print("Edge not present in the graph")
             else:	  
                self._adj[u][v] = 0


        def isAdjacent(self, s1, s2):
            u = self._getIndex(s1)
            v = self._getIndex(s2)
            if u is None:
                print("Start vertex not present in the graph")
                return False
            elif v is None:
                print("End vertex not present in the graph")
                return False
            return False if self._adj[u][v] == 0 else True   

      
        def outdegree(self, s):
            u = self._getIndex(s)
            if u is None:
               print("Vertex not present in the graph")
               return
        
            outd = 0
            for v in range(self._n):
                if self._adj[u][v] != 0 :
                   outd+=1
            return outd
             

        def indegree(self, s):
            u = self._getIndex(s)
            if u is None:
               print("Vertex not present in the graph")
               return
        
            ind = 0

            for v in range(self._n):
                if self._adj[v][u] != 0 :
                    ind+=1
            return ind

        def dfsTreeEdges(self):
            s = input("Enter starting vertex for Depth First Search : ")
            u = self._getIndex(s)
            if u is None:
                 print("Vertex not present in the graph")
                 return
  
            for v in range(self._n):
                self._vertexList[v].state = INITIAL
                self._vertexList[v].predecessor = None
                     
            self._dfs1(u)

            for v in range(self._n):
                if self._vertexList[v].state == INITIAL:
                     self._dfs1(v)    
                           
            print("Tree Edges : ")
            for v in range(self._n):
                u = self._vertexList[v].predecessor
                if u != None:
                    print("(", self._vertexList[u].name ,", ", self._vertexList[v].name , ")" )
                
 
        def _dfs1(self,v):
             from queue import LifoQueue
             st = LifoQueue()
             st.put(v)
             
             while st.qsize() !=0 :
                  v = st.get()

                  if self._vertexList[v].state == INITIAL:
                       print(self._vertexList[v].name, end = " ")
                       self._vertexList[v].state = VISITED

                  for i in range(self._n-1,-1,-1):
                      if self._adj[v][i]!=0 and self._vertexList[i].state == INITIAL:
                          st.put(i)
                          self._vertexList[i].predecessor = v  # only this line added
             print()


       
        def dfsTraversal(self):
            s = input("Enter starting vertex for Depth First Search : ")
            u = self._getIndex(s)
            if u is None:
                print("Vertex not present in the graph")
                return

            for v in range(self._n):
                self._vertexList[v].state = INITIAL
            
            self._dfs( u )

        def _dfs(self,v):
             from queue import LifoQueue
             st = LifoQueue()
             st.put(v)
             
             while st.qsize() !=0 :
                  v = st.get()

                  if self._vertexList[v].state == INITIAL:
                       print(self._vertexList[v].name, end = " ")
                       self._vertexList[v].state = VISITED

                  for i in range(self._n-1,-1,-1):
                      if self._adj[v][i]!=0 and self._vertexList[i].state == INITIAL:
                          st.put(i)
                          
             print()
             

        def dfsTraversalAll(self):
            s = input("Enter starting vertex for Depth First Search : ")
            u = self._getIndex(s)
            if u is None:
                 print("Vertex not present in the graph")
                 return

            for v in range(self._n):
                self._vertexList[v].state = INITIAL
                    
            self._dfs(u)

            for v in range(self._n):
                if self._vertexList[v].state == INITIAL:
                     self._dfs(v)    
        

if __name__ == '__main__':

     g = DirectedGraph()

     g.insertVertex("Zero")
     g.insertVertex("One")
     g.insertVertex("Two")
     g.insertVertex("Three")
     g.insertVertex("Four")
     g.insertVertex("Five")
     g.insertVertex("Six")
     g.insertVertex("Seven")
     g.insertVertex("Eight")
     g.insertVertex("Nine")
     g.insertVertex("Ten")
     g.insertVertex("Eleven")

     g.insertEdge("Zero", "One")
     g.insertEdge("Zero", "Three")
     g.insertEdge("One", "Two")
     g.insertEdge("One", "Four")
     g.insertEdge("One", "Five")
     g.insertEdge("Two", "Five")
     g.insertEdge("Two", "Seven")
     g.insertEdge("Three", "Six")
     g.insertEdge("Four", "Three")
     g.insertEdge("Five", "Three")
     g.insertEdge("Five", "Six")
     g.insertEdge("Five", "Eight")
     g.insertEdge("Seven", "Eight")
     g.insertEdge("Seven", "Ten")
     g.insertEdge("Eight", "Eleven")
     g.insertEdge("Nine", "Six")
     g.insertEdge("Eleven", "Nine")

     g.dfsTreeEdges()
     
  
   
