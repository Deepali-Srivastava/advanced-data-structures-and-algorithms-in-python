# Copyright (C) Deepali Srivastava - All Rights Reserved
# This code is part of DSA course available on CourseGalaxy.com  

from math import ceil

class Node:
    def __init__(self,size):
        self.numKeys = 0
        self.key = [None] * size
        self.child = [None] * size
        
class BTree:
    M = 5
    MAX = M - 1
    MIN = ceil(M/2) - 1
 

    def __init__(self):
        self.root = None
    
    def isEmpty(self):
        return self.root == None
           
    def search(self, x):
        if self._search(x, self.root) == None:
             return False
        return True
       
    def _search(self, x, p):
        if p == None :        # Key x not present in the tree
            return None
      
        flag, n = self._searchNode(x, p)
        if flag == True:	# Key x found in node p 
            return p

        return self._search(x, p.child[n]) # Search in node p.child[n] 
        

    def _searchNode(self, x, p):
        if x < p.key[1] : # key x is less than leftmost key 
            return False,0

        n = p.numKeys
        while (x < p.key[n]) and n > 1 :
             n -= 1

        if x == p.key[n]:
             return True,n
        else:
             return False,n
        

    def inorder(self):
         self._inorder(self.root)
         print()
     

    def _inorder(self, p):
         if p == None:
            return

         i = 0
         while i < p.numKeys:
            self._inorder(p.child[i])
            print(p.key[i+1] , end = "  ")
            i += 1
            
         self._inorder( p.child[i] )


    def display(self):
        self._display(self.root, 0)
     

    def _display(self, p, blanks):
        if p != None :
             for i in range(blanks):
                 print(end = " ")

             for i in range(1,p.numKeys+1):
                    print(p.key[i] ,end=" ")
             print()

             for i in range(p.numKeys+1):
                    self._display(p.child[i], blanks + 10)

     
    def insert(self, x):
    
        taller, iKey, iKeyRchild = self._insert(x, self.root)

        if taller:  # Height increased by one, new root node has to be created 
            temp = Node(BTree.M)
            temp.child[0] = self.root
            self.root = temp

            self.root.numKeys = 1
            self.root.key[1] = iKey
            self.root.child[1] = iKeyRchild
                

    def _insert(self, x, p):

         if p == None:  #First Base case : key not found
            return True, x, None
    
         flag, n = self._searchNode(x, p)
         
         if flag == True : #Second Base Case : key found
             print("Key already present in the tree")
             return False, 0 , None #No need to insert the key
            

         flag, iKey, iKeyRchild = self._insert(x, p.child[n])

         if flag == True:
             if p.numKeys < BTree.MAX:
                 self._insertByShift(p, n, iKey, iKeyRchild)
                 return False,iKey, iKeyRchild #Insertion over
             else:
                 iKey, iKeyRchild = self._split(p, n, iKey, iKeyRchild )
                 return True,iKey, iKeyRchild  #Insertion not over : Median key yet to be inserted
         return False, iKey, iKeyRchild
        

    def _insertByShift(self, p, n, iKey, iKeyRchild):
         i = p.numKeys
         while i > n:
             p.key[i+1] = p.key[i]
             p.child[i+1] = p.child[i]
             i -= 1 

         p.key[n+1] = iKey
         p.child[n+1] = iKeyRchild
         p.numKeys += 1
        

    def _split(self, p, n,iKey, iKeyRchild):
         if n == BTree.MAX:
             lastKey = iKey
             lastChild = iKeyRchild
         else:
             lastKey = p.key[BTree.MAX]
             lastChild = p.child[BTree.MAX]

             i = p.numKeys-1
             while  i>n :
                 p.key[i + 1] = p.key[i]
                 p.child[i + 1] = p.child[i]
                 i -= 1 
    
             p.key[i+1] = iKey
             p.child[i+1] = iKeyRchild
            

         d = (BTree.M + 1) // 2
         medianKey = p.key[d]
         newNode = Node(BTree.M)
         newNode.numKeys = BTree.M - d

         newNode.child[0] = p.child[d]
         i=1
         j=d+1
         
         while j <= BTree.MAX :
             newNode.key[i] = p.key[j]
             newNode.child[i] = p.child[j]
             i += 1
             j += 1
            
         newNode.key[i] = lastKey
         newNode.child[i] = lastChild

         p.numKeys = d - 1

         iKey = medianKey
         iKeyRchild = newNode

         return iKey, iKeyRchild
        

    def delete(self, x):
         if self.root == None :
            print("Tree is empty")
            return

         self._delete(x, self.root)

         if self.root != None and self.root.numKeys == 0:  #Height of tree decreased by 1
            self.root = self.root.child[0]
        

    def _delete(self, x, p):

         flag, n = self._searchNode(x, p)

         if flag == True: # Key x found in node p 
            if p.child[n] == None:     # Node p is a leaf node 
                self._deleteByShift(p, n)
                return
            else:                    # Node p is a non-leaf node 
                 s = p.child[n]
                 while s.child[0] != None:
                    s = s.child[0]
                 p.key[n] = s.key[1]
                 self._delete(s.key[1], p.child[n])
         else:  # Key x not found in node p 
             if p.child[n] == None : # p is a leaf node 
                print("Value", x , " not present in the tree")
                return
             else:  # p is a non-leaf node 
                self._delete(x, p.child[n])

         if p.child[n].numKeys < BTree.MIN :
             self._restore(p,n)
        

    def _deleteByShift(self, p, n):
         for i in range(n+1,p.numKeys+1):  
             p.key[i-1] = p.key[i]
             p.child[i-1] = p.child[i]
         p.numKeys -= 1 
        

    # Called when p.child[n] becomes underflow 
    def _restore(self, p, n):
         if n!=0 and p.child[n-1].numKeys > BTree.MIN :
              self._borrowLeft(p, n)
         elif n!=p.numKeys and p.child[n+1].numKeys > BTree.MIN:
              self._borrowRight(p, n)
         else:
              if n!=0 :  #if there is a left sibling
                self._combine(p, n)    # combine with left sibling
              else:
                self._combine(p, n+1)  # combine with right sibling
            

    def _borrowLeft(self, p, n):
           underflowNode = p.child[n]
           leftSibling = p.child[n - 1]

           underflowNode.numKeys += 1 

           #Shift all the keys and children in underflowNode one position right
           for i in range(underflowNode.numKeys, 0, -1):            
                underflowNode.key[i+1] = underflowNode.key[i]
                underflowNode.child[i+1] = underflowNode.child[i]
            
           underflowNode.child[1] = underflowNode.child[0]

           # Move the separator key from parent node p to underflowNode 
           underflowNode.key[1] = p.key[n]

           # Move the rightmost key of node leftSibling to the parent node p 
           p.key[n] = leftSibling.key[leftSibling.numKeys]

           #Rightmost child of leftSibling becomes leftmost child of underflowNode 
           underflowNode.child[0] = leftSibling.child[leftSibling.numKeys]

           leftSibling.numKeys -= 1 
        

    def _borrowRight(self, p, n):
           underflowNode = p.child[n]
           rightSibling = p.child[n+1]

           # Move the separator key from parent node p to underflowNode 
           underflowNode.numKeys += 1
           underflowNode.key[underflowNode.numKeys] = p.key[n+1]

           # Leftmost child of rightSibling becomes the rightmost child of underflowNode 
           underflowNode.child[underflowNode.numKeys] = rightSibling.child[0]
 
           rightSibling.numKeys -= 1

           # Move the leftmost key from rightSibling to parent node p 
           p.key[n+1] = rightSibling.key[1]
           
           # Shift all the keys and children of rightSibling one position left 
           rightSibling.child[0] = rightSibling.child[1]
           for i in range(1,rightSibling.numKeys+1):
               rightSibling.key[i] = rightSibling.key[i + 1]
               rightSibling.child[i] = rightSibling.child[i + 1]


    def _combine(self, p, m):
            nodeA = p.child[m-1]
            nodeB = p.child[m]

            nodeA.numKeys += 1

            # Move the separator key from the parent node p to nodeA 
            nodeA.key[nodeA.numKeys] = p.key[m]

            # Shift the keys and children that are after separator key in node p one position left 
            for i in range(m, p.numKeys):
                p.key[i] = p.key[i+1]
                p.child[i] = p.child[i+1]
            
            p.numKeys -= 1

            # Leftmost child of nodeB becomes rightmost child of nodeA 
            nodeA.child[nodeA.numKeys] = nodeB.child[0]

            # Insert all the keys and children of nodeB at the end of nodeA 
            for i in range(1, nodeB.numKeys+1):
                nodeA.numKeys += 1
                nodeA.key[nodeA.numKeys] = nodeB.key[i]
                nodeA.child[nodeA.numKeys] = nodeB.child[i]


##############################################################################################
            
if __name__ == '__main__':

    tree = BTree()

    while True:
       
        print("1.Search")
        print("2.Insert")
        print("3.Delete") 
        print("4.Display") 
        print("5.Inorder Traversal")
        print("6.Quit")
        choice = int(input("Enter your choice : "))

        if choice == 1:
            key = int(input("Enter the key to be searched : "))
            if tree.search(key) == True:
                print("Key found")
            else:
                print("Key not found")
        elif choice == 2:
            key = int(input("Enter the key to be inserted : "))
            tree.insert(key)
        elif choice == 3:
            key = int(input("Enter the element to be deleted : ")) 
            tree.delete(key)
        elif choice == 4:
            tree.display()
        elif choice == 5:
            tree.inorder()
        elif choice == 6:
            break
        else:
            print("Wrong choice") 
        print()

