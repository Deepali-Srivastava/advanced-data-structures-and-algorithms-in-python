# Copyright (C) Deepali Srivastava - All Rights Reserved
# This code is part of DSA course available on CourseGalaxy.com  

class Node:
    def __init__(self,value):
        self.info = value 
        self.lchild = None
        self.rchild = None
        self.balance = 0

class AVLTree:

    taller = False
    shorter = False
    
    def __init__(self):
        self.root = None


    def isEmpty(self,x):
        return self.root == None


    def display(self):
        self._display(self.root,0)
        print()
        

    def _display(self,p,level):
        if p is None:
            return
        self._display(p.rchild, level+1)
        print()

        for i in range(level):
            print("    ", end='')
        print(p.info)
        self._display(p.lchild, level+1) 

    
    def inorder(self):
        self._inorder(self.root)
        print()


    def _inorder(self, p):
        if p is None :
            return
        self._inorder(p.lchild)
        print(p.info, end = " ")
        self._inorder(p.rchild) 


    def insert(self,x):
        self.root = self._insert(self.root, x)
                 

    def _insert(self,p,x):
        if p is None:
            p = Node(x)
            AVLTree.taller = True
        elif x < p.info:
            p.lchild = self._insert(p.lchild, x)
            if AVLTree.taller == True:
                p = self._insertionLeftSubtreeCheck(p)
        elif x > p.info :
            p.rchild = self._insert(p.rchild, x)
            if AVLTree.taller == True:
                p = self._insertionRightSubtreeCheck(p)
        else:
            print(x," already present in the tree")
            AVLTree.taller = False
        return p

    def _insertionLeftSubtreeCheck(self, p):
         if p.balance == 0:     # Case L_1 : was balanced  
              p.balance = 1 # now left heavy 
         elif p.balance == -1:  # Case L_2 : was right heavy   
              p.balance = 0 # now balanced 
              AVLTree.taller = False
         else:  # p.balance = 0 Case L_3 : was left heavy    
              p = self._insertionLeftBalance(p)   # Left Balancing 
              AVLTree.taller = False
         return p
        

    def _insertionRightSubtreeCheck(self, p):
         if p.balance == 0:    # Case R_1 : was balanced    
            p.balance = -1  # now right heavy 
         elif p.balance == 1:   # Case R_2 : was left heavy   
            p.balance = 0   # now balanced  
            AVLTree.taller = False
         else: # p.balance == 1  Case R_3: Right heavy    
            p = self._insertionRightBalance(p)    # Right Balancing
            AVLTree.taller = False
         return p

    def _insertionLeftBalance(self, p):
          a = p.lchild
          if a.balance == 1:  # Case L_3A : Insertion in AL   
                p.balance = 0
                a.balance = 0
                p = self._rotateRight(p)
          else:     #  Case L_3B : Insertion in AR  
                b = a.rchild
                if b.balance == 1:  # Case L_3B2 : Insertion in BL  
                    p.balance = -1
                    a.balance = 0
                elif b.balance == -1:   # Case L_3B2 : Insertion in BR     
                    p.balance = 0
                    a.balance = 1
                else:       # b.balance == 0   Case L_3B2 : B is the newly inserted node   
                    p.balance = 0
                    a.balance = 0
                b.balance = 0
                p.lchild = self._rotateLeft(a)
                p = self._rotateRight(p)
          return p
      
     
    def _insertionRightBalance(self,p):
            a = p.rchild
            if a.balance == -1:  # Case R_3A : Insertion in AR   
                p.balance = 0
                a.balance = 0
                p = self._rotateLeft(p)
            else:       # Case R_3B : Insertion in AL  
                b = a.lchild
                if b.balance == -1:    # Insertion in BR  
                    p.balance = 1
                    a.balance = 0
                elif  b.balance == 1:  # Insertion in BL  
                    p.balance = 0
                    a.balance = -1
                else:     # B is the newly inserted node  
                    p.balance = 0
                    a.balance = 0
                    
                b.balance = 0
                p.rchild = self._rotateRight(a)
                p = self._rotateLeft(p)
            return p
        

    def _rotateLeft(self, p):
        a = p.rchild
        p.rchild = a.lchild
        a.lchild = p
        return a
     
    def _rotateRight(self, p):
         a = p.lchild
         p.lchild = a.rchild
         a.rchild = p
         return a

           
    def delete(self,x):
        self.root = self._delete(self.root, x) 


    def _delete(self, p, x):
        if p is None:
            print(x , "  not found")
            AVLTree.shorter = False
            return p 
         
        if x < p.info:  # delete from left subtree
            p.lchild = self._delete(p.lchild, x)
            if AVLTree.shorter == True :
                p = self._deletionLeftSubtreeCheck(p)
        elif x > p.info: # delete from right subtree
            p.rchild = self._delete(p.rchild, x)
            if AVLTree.shorter == True :
                p = self._deletionRightSubtreeCheck(p)
        else:
            # key to be deleted is found
            if p.lchild is not None  and p.rchild is not None:  # 2 children
                s = p.rchild
                while s.lchild is not None:
                    s = s.lchild
                p.info = s.info
                p.rchild = self._delete(p.rchild,s.info)
                if AVLTree.shorter == True :
                    p = self._deletionRightSubtreeCheck(p)
            else:   # 1 child or no child
                if p.lchild is not None: # only left child
                    ch = p.lchild
                else:  # only right child or no child 
                     ch = p.rchild
                p = ch
                AVLTree.shorter = True
        return p


    def _deletionLeftSubtreeCheck(self, p):
       if p.balance == 0:    # Case L_1 : was balanced         
            p.balance = -1  # now right heavy   
            AVLTree.shorter = False
       elif p.balance == 1: # Case L_2 : was left heavy      
            p.balance = 0   # now balanced  
       else: # p.balance == -1  Case L_3 : was right heavy     
            p = self._deletionRightBalance(p) #Right Balancing 
       return p

       
    def _deletionRightSubtreeCheck(self, p):
        if p.balance == 0:  # Case R_1 : was balanced       
            p.balance = 1   # now left heavy  
            AVLTree.shorter = False
        elif p.balance == -1:   # Case R_2 : was right heavy    
            p.balance = 0   # now balanced  
        else:     #p.balance == 1    Case R_3 : was left heavy      
            p = self._deletionLeftBalance(p)  #Left Balancing 
        return p
        
    def _deletionLeftBalance(self, p):
          a = p.lchild
          if a.balance == 0:  # Case R_3A  
             a.balance = -1
             AVLTree.shorter = False
             p = self._rotateRight(p)
          elif a.balance == 1:   # Case R_3B 
             p.balance = 0
             a.balance = 0
             p = self._rotateRight(p)
          else :            # Case R_3C  
             b = a.rchild
             if b.balance == 0: # Case R_3C1  
                 p.balance = 0
                 a.balance = 0
             elif b.balance == -1:  # Case R_3C2 
                 p.balance = 0
                 a.balance = 1
             else:          # Case R_3C3  
                 p.balance = -1
                 a.balance = 0
             b.balance = 0
             p.lchild = self._rotateLeft(a)
             p = self._rotateRight(p)
          return p
        
    def _deletionRightBalance(self, p):
        a = p.rchild
        if a.balance == 0 : # Case L_3A
            a.balance = 1
            AVLTree.shorter = False
            p = self._rotateLeft(p)
        elif a.balance == -1 :  # Case L_3B  
            p.balance = 0
            a.balance = 0
            p = self._rotateLeft(p)
        else:       # Case L_3C 
            b = a.lchild
            if b.balance == 0: # Case L_3C1 
                p.balance = 0
                a.balance = 0
            elif b.balance == 1: # Case L_3C2  
                p.balance = 0
                a.balance = -1
            else: # b.balance = -1: # Case L_3C3  
                p.balance = 1
                a.balance = 0
            b.balance = 0
            p.rchild = self._rotateRight(a)
            p = self._rotateLeft(p)
        return p
  
       
    

   
##############################################################################################

if __name__ == '__main__':

    tree = AVLTree()
             
    while True:
        print("1.Display Tree") 
        print("2.Insert a new node") 
        print("3.Delete a node")
        print("4.Inorder Traversal") 
        print("5.Quit")
        choice = int(input("Enter your choice : "))
        
        if choice == 1:
            tree.display()
        elif choice == 2:
            x = int(input("Enter the key to be inserted : "))
            tree.insert(x)
        elif choice == 3:
            x = int(input("Enter the key to be deleted : ")) 
            tree.delete(x)
        elif choice == 4:
            tree.inorder()
        elif choice == 5:
            break
        else:
            print("Wrong choice") 
        print()
        

