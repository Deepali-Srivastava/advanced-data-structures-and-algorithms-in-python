# Copyright (C) Deepali Srivastava - All Rights Reserved
# This code is part of DSA course available on CourseGalaxy.com  

from sys import maxsize as INFINITY

TEMPORARY = 1
PERMANENT = 2

class Vertex:
        def __init__(self, name):
           self.name = name

          
class DirectedWeightedGraph:

        def __init__(self, size=20):
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
                    if self._adj[i][j] !=0 :
                        e+=1
            return e


        def vertices(self):
            return [vertex.name for vertex in self._vertexList]


        def edges(self):
            edges = []
            for i in range(self._n):
                for j in range(self._n):
                   if self._adj[i][j] != 0:
                      edges.append( (self._vertexList[i].name, self._vertexList[j].name, self._adj[i][j]) )
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
                  
             self._vertexList.pop(u)
             self._n -= 1


        def insertEdge(self, s1, s2, w):
            u = self._getIndex(s1)
            v = self._getIndex(s2)
            if u is None:
                print("Start vertex not present in the graph, first insert the start vertex")
            elif v is None:
                print("End vertex not present  in the graph, first insert the end vertex")
            elif u == v:
                print("Not a valid edge") 
            elif self._adj[u][v] != 0 :
                print("Edge already present in the graph") 
            else:  
                self._adj[u][v] = w 
                
        
        def removeEdge(self, s1, s2):
             u = self._getIndex(s1)
             v = self._getIndex(s2)
             
             if u is None:
                print("Start vertex not present in the graph ")
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
                if self._adj[v][u] !=0 :
                    ind+=1
            return ind


        def _dijkstra(self, s):
       
            for v in range(self._n):
                self._vertexList[v].status = TEMPORARY
                self._vertexList[v].pathLength = INFINITY
                self._vertexList[v].predecessor = None
            

            self._vertexList[s].pathLength = 0

            while True:
                c = self._tempVertexMinPL()

                if c == None:
                    return

                self._vertexList[c].status = PERMANENT

                for v in range(self._n):
                   if self._adj[c][v]!=0  and self._vertexList[v].status == TEMPORARY:
                        if self._vertexList[c].pathLength + self._adj[c][v] < self._vertexList[v].pathLength:
                            self._vertexList[v].predecessor = c
                            self._vertexList[v].pathLength = self._vertexList[c].pathLength + self._adj[c][v]
                        
            
        def _tempVertexMinPL(self):
            min = INFINITY
            x = None
            for v in range(self._n):
                if self._vertexList[v].status == TEMPORARY and self._vertexList[v].pathLength < min:
                   min = self._vertexList[v].pathLength
                   x = v
            return x
        

        def findPaths(self, source):

            s = self._getIndex(source)
            if s is None:
               print("Vertex not present in the graph")
               return
           
            self._dijkstra(s)
           
            print("Source Vertex :", source)
                
            for v in range(self._n):
                print("Destination Vertex :", self._vertexList[v].name)
                if self._vertexList[v].pathLength == INFINITY :
                    print("There is no path from ", source , "to vertex", self._vertexList[v].name, "\n")
                else:
                    self._findPath(s,v)

                
        def _findPath(self, s, v):
             path = [] 
             sd = 0          
             count = 0              
                
             while v != s:
                count += 1
                path.append(v)
                u = self._vertexList[v].predecessor
                sd += self._adj[u][v]
                v = u   
             path.append(s)

             print("Shortest Path is : ", end = " ")
             for u in reversed(path):
                 print(u, end = " ")
             print("\nShortest distance is :", sd, "\n")
            

if __name__ == '__main__':

  g = DirectedWeightedGraph() 

  g.insertVertex("Zero")
  g.insertVertex("One")
  g.insertVertex("Two")
  g.insertVertex("Three")
  g.insertVertex("Four")
  g.insertVertex("Five")
  g.insertVertex("Six")
  g.insertVertex("Seven")
  g.insertVertex("Eight")

  g.insertEdge("Zero", "Three", 2)
  g.insertEdge("Zero", "One", 5)
  g.insertEdge("Zero", "Four", 8)
  g.insertEdge("One", "Four", 2)
  g.insertEdge("Two", "One", 3)
  g.insertEdge("Two", "Five", 4)
  g.insertEdge("Three", "Four", 7)
  g.insertEdge("Three", "Six", 8)
  g.insertEdge("Four", "Five", 9)
  g.insertEdge("Four", "Seven", 4)
  g.insertEdge("Five", "One", 6)
  g.insertEdge("Six", "Seven", 9)
  g.insertEdge("Seven", "Three", 5)
  g.insertEdge("Seven", "Five", 3)
  g.insertEdge("Seven", "Eight", 5)
  g.insertEdge("Eight", "Five", 3)

  g.findPaths("Zero")

      
