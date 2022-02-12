# Copyright (C) Deepali Srivastava - All Rights Reserved
# This code is part of DSA course available on CourseGalaxy.com  

class Node:
    def __init__(self,value):
        self.info = value 
        self.left = None
        self.right = None
        self.leftThread = True
        self.rightThread = True


class ThreadedBinaryTree:

    def __init__(self):
        self.root = None
    

    def _inorderPredecessor(self, p):
        if p.leftThread == True: 
            return p.left
        else:
            p = p.left
            while p.rightThread == False:
                    p = p.right
            return p
    
  
    def _inorderSuccessor(self, p):
        if p.rightThread == True:
            return p.right 
        else:
            p = p.right
            while p.leftThread == False:
                    p = p.left
            return p
            
             
    def inorder(self):
        if self.root == None:
            print("Tree is empty")
            return       
                
        #Find the leftmost node of the tree
        p = self.root
        while p.leftThread == False:
            p = p.left
    
        while p!=None:
            print(p.info, end = " ")
            if p.rightThread == True:
                p = p.right
            else:
                p = p.right
                while p.leftThread == False:
                    p = p.left
        print()


    def insert(self, x):
        p = self.root
        par = None
    
        while p!=None :
            par = p
            if x < p.info:
                if p.leftThread == False:
                    p = p.left
                else:
                    break
            elif x > p.info:
              if p.rightThread == False:
                    p = p.right
              else:
                    break
            else:
               print(x , " already present in the tree")
               return

        temp = Node(x)
        if par == None:
            self.root = temp
        elif x < par.info: #inserted as left child
            temp.left = par.left
            temp.right = par
            par.leftThread = False
            par.left = temp
        else:  #inserted as right child
            temp.left = par
            temp.right = par.right
            par.rightThread = False
            par.right = temp
   
    def delete(self, x):
        p = self.root
        par = None

        while p != None:
            if x == p.info:
                break
            par = p
            if x < p.info:
                if p.leftThread == False:
                    p = p.left
                else:
                    break
            else:
                if p.rightThread == False:
                    p = p.right
                else:
                    break
         
        if p == None or p.info != x:
            print(x , " not found")
            return
        
                    
        if p.leftThread == False and p.rightThread == False: #Case C: 2 children
            #Find inorder successor and its parent
            ps = p
            s = p.right

            while s.leftThread == False:
                ps = s
                s = s.left
            
            p.info = s.info
            p = s
            par = ps
        

        #Case A : No child
        if p.leftThread == True and p.rightThread == True:
            if par == None:
                self.root = None
            elif p == par.left:
                par.leftThread = True
                par.left = p.left
            else:
                par.rightThread = True
                par.right = p.right
            return
        
        #Case B : 1 child
        if p.leftThread == False: #node to be deleted has left child 
            ch = p.left
        else:               #node to be deleted has right child 
            ch = p.right

        if par == None:   #node to be deleted is root node
            self.root = ch
        elif p == par.left: #node is left child of its parent
            par.left = ch
        else:  #node is right child of its parent
            par.right = ch

        pred = self._inorderPredecessor(p)
        succ = self._inorderSuccessor(p)

        if p.leftThread == False: #if p has left child, right is a thread 
            pred.right = succ
        else:  #p has right child,left is a thread
            succ.left = pred
    
   


#############################################################################################


if __name__ == '__main__':
            
    tree = ThreadedBinaryTree()

    while True:
        print("1.Insert a new node") 
        print("2.Delete a node")
        print("3.Inorder Traversal") 
        print("4.Quit")
        choice = int(input("Enter your choice : "))
        
        if choice == 1:
            x = int(input("Enter the key to be inserted : "))
            tree.insert(x)
        elif choice == 2:
            x = int(input("Enter the element to be deleted : ")) 
            tree.delete(x)
        elif choice == 3:
            tree.inorder()
        elif choice == 4:
            break
        else:
            print("Wrong choice") 
        print()

