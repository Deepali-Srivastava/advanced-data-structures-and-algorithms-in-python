# Copyright (C) Deepali Srivastava - All Rights Reserved
# This code is part of DSA course available on CourseGalaxy.com  

class Vertex:
        def __init__(self, name):
           self.name = name

          
class UndirectedWeightedGraph:

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
                print("First vertex not present in the graph")
            elif v is None:
                print("Second vertex not present in the graph")
            elif u == v:
                print("Not a valid edge") 
            elif self._adj[u][v] != 0 :
                print("Edge already present in the graph") 
            else:  
                self._adj[u][v] = w
                self._adj[v][u] = w
                
        
        def removeEdge(self, s1,s2):
             u = self._getIndex(s1)
             v = self._getIndex(s2)
             if u is None:
                print("First vertex not present in the graph")
             elif v is None:
                print("Second vertex not present in the graph")
             elif self._adj[u][v] == 0:
                print("Edge not present in the graph")
             else:        
                self._adj[u][v] = 0
                self._adj[v][u] = 0


        def isAdjacent(self, s1, s2):
            u = self._getIndex(s1)
            v = self._getIndex(s2)
            if u is None:
                print("First vertex not present in the graph")
                return False
            elif v is None:
                print("Second vertex not present in the graph")
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


        def kruskals(self):
           edgesList = []

           for u in range(self._n):
              for v in range(self._n):
                 if self._adj[u][v] != 0:
                    edgesList.append( (u,v,self._adj[u][v]) )
                        

           edgesList = sorted(edgesList, key = lambda item: item[2], reverse = True)  
           
           for v in range(self._n):
              self._vertexList[v].father = None
           
           r1 = None
           r2 = None
           edgesInTree = 0  
           wtTree = 0
           
           while len(edgesList)!=0  and edgesInTree < self._n-1 :
                edge = edgesList.pop()
                v1 = edge[0]
                v2 = edge[1]
                        
                v = v1
                while self._vertexList[v].father != None :
                     v = self._vertexList[v].father
                r1 = v
                    
                v = v2
                while self._vertexList[v].father!=None :
                      v = self._vertexList[v].father
                r2 = v

                if r1 != r2 :  #Edge (v1,v2) is included
                    edgesInTree += 1
                    print(self._vertexList[v1].name , "->"  , self._vertexList[v2].name ) 
                    wtTree += edge[2]
                    self._vertexList[r2].father = r1
                         
           if edgesInTree < self._n-1:
                 print("Graph is not connected, no spanning tree possible")
                 return
                        
           print("Weight of Minimum Spanning Tree is " , wtTree)
            


if __name__ == '__main__':

  g = UndirectedWeightedGraph() 

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

  g.insertEdge("Zero", "One", 19)
  g.insertEdge("Zero", "Three", 14)
  g.insertEdge("Zero", "Four", 12)
  g.insertEdge("One", "Two", 20)
  g.insertEdge("One", "Four", 18)
  g.insertEdge("Two", "Four", 17)
  g.insertEdge("Two", "Five", 15)
  g.insertEdge("Two", "Nine", 29)
  g.insertEdge("Three", "Four", 13)
  g.insertEdge("Three", "Six", 28)
  g.insertEdge("Four", "Five", 16)
  g.insertEdge("Four", "Six", 21)
  g.insertEdge("Four", "Seven", 22)
  g.insertEdge("Four", "Eight", 24)
  g.insertEdge("Five", "Eight", 26)
  g.insertEdge("Five", "Nine", 27)
  g.insertEdge("Six", "Seven", 23)
  g.insertEdge("Seven", "Eight", 30)
  g.insertEdge("Eight", "Nine", 35)

  g.kruskals()
