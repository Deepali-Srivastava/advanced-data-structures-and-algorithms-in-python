# Copyright (C) Deepali Srivastava - All Rights Reserved
# This code is part of DSA course available on CourseGalaxy.com  


INITIAL = 0   
WAITING = 1
VISITED = 2

        
class Vertex:
        def __init__(self, name):
           self.name = name

          
class UndirectedGraph:

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
                for j in range(i):
                    if self._adj[i][j]!=0:
                        e+=1
            return e


        def vertices(self):
            return [vertex.name for vertex in self._vertexList]


        def edges(self):  
            edges = []
            for i in range(self._n):
                for j in range(i):
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
                self._adj[v][u] = 1
                
        
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
                self._adj[v][u] = 0


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

      
        def degree(self,s):
        
            u = self._getIndex(s)
            if u is None:
               print("Vertex not present in the graph")
               return

            deg = 0
            for v in range(self._n):
                if self._adj[u][v] != 0 :
                     deg += 1
            return deg
         
        def _bfsC(self, v, cN):
            from queue import Queue
            qu = Queue()
            qu.put(v)
            self._vertexList[v].state = WAITING

            while qu.qsize() != 0:
               v = qu.get()
               self._vertexList[v].state = VISITED
               self._vertexList[v].componentNumber = cN

               for i in range(self._n):
                  if self._adj[v][i]!=0 and self._vertexList[i].state == INITIAL: 
                     qu.put(i)
                     self._vertexList[i].state = WAITING

 
        def isConnected(self):
            
             for v in range(self._n):
                 self._vertexList[v].state = INITIAL
             
             cN = 1
             
             self._bfsC(0,cN)
                 
             for v in range(self._n):
                if self._vertexList[v].state == INITIAL:
                    cN += 1
                    self._bfsC(v,cN)

             if cN == 1:
                  print("Graph is connected")
                  return True
             else:
                  print("Graph is not connected, it has", cN , "connected components")
                  for v in range(self._n):
                       print(self._vertexList[v].name , "  " , self._vertexList[v].componentNumber)
                  return False

if __name__ == '__main__':

        g1 = UndirectedGraph() 
        g1.insertVertex("Zero")
        g1.insertVertex("One")
        g1.insertVertex("Two")
        g1.insertVertex("Three")
        g1.insertVertex("Four")
        g1.insertVertex("Five")
        g1.insertVertex("Six")
        g1.insertVertex("Seven")
        g1.insertVertex("Eight")
        g1.insertVertex("Nine")

        g1.insertEdge("Zero", "One")
        g1.insertEdge("Zero", "Seven")
        g1.insertEdge("One", "Two")
        g1.insertEdge("One", "Four")
        g1.insertEdge("One", "Five")
        g1.insertEdge("Two", "Three")
        g1.insertEdge("Two", "Five")
        g1.insertEdge("Three", "Six")
        g1.insertEdge("Four", "Seven")
        g1.insertEdge("Five", "Six")
        g1.insertEdge("Five", "Seven")
        g1.insertEdge("Five", "Eight")
        g1.insertEdge("Six", "Nine")
        g1.insertEdge("Seven", "Eight")
        g1.insertEdge("Eight", "Nine")

        g1.isConnected()

        g2 = UndirectedGraph()

        g2.insertVertex("Zero")
        g2.insertVertex("One")
        g2.insertVertex("Two")
        g2.insertVertex("Three")
        g2.insertVertex("Four")
        g2.insertVertex("Five")
        g2.insertVertex("Six")
        g2.insertVertex("Seven")
        g2.insertVertex("Eight")
        g2.insertVertex("Nine")
        g2.insertVertex("Ten")
        g2.insertVertex("Eleven")
        g2.insertVertex("Twelve")
        g2.insertVertex("Thirteen")
        g2.insertVertex("Fourteen")
        g2.insertVertex("Fifteen")
        g2.insertVertex("Sixteen")

        g2.insertEdge("Zero", "One")
        g2.insertEdge("Zero", "Two")
        g2.insertEdge("Zero", "Three")
        g2.insertEdge("One", "Three")
        g2.insertEdge("Two", "Five")
        g2.insertEdge("Three", "Four")
        g2.insertEdge("Four", "Five")
        g2.insertEdge("Six", "Seven")
        g2.insertEdge("Six", "Eight")
        g2.insertEdge("Seven", "Ten")
        g2.insertEdge("Eight", "Nine")
        g2.insertEdge("Nine", "Ten")
        g2.insertEdge("Eleven", "Twelve")
        g2.insertEdge("Eleven", "Fourteen")
        g2.insertEdge("Eleven", "Fifteen")
        g2.insertEdge("Twelve", "Thirteen")
        g2.insertEdge("Thirteen", "Fourteen")
        g2.insertEdge("Fourteen", "Sixteen")

        g2.isConnected()


   
