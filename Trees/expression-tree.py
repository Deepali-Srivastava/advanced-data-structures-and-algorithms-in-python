# Copyright (C) Deepali Srivastava - All Rights Reserved
# This code is part of DSA course available on CourseGalaxy.com  

class Node:
    def __init__(self,value):
        self.info = value 
        self.lchild = None
        self.rchild = None


class ExpressionTree:

     def __init__(self):
        self.root = None

         
     def buildTree(self, postfix):
        from queue import LifoQueue
        stack = LifoQueue()
        
        for i in range(len(postfix)):
            if isOperator( postfix[i] ):
                t = Node( postfix[i] )
                t.rchild = stack.get()
                t.lchild = stack.get()
                stack.put(t)
            else: # operand
                t = Node(postfix[i])
                stack.put(t)
        self.root = stack.get()
       
        
     def prefix(self):
        self._preorder(self.root)
        print()
        

     def _preorder(self, p):
        if p == None:
            return
        print(p.info, end = " ")
        self._preorder(p.lchild)
        self._preorder(p.rchild)
        

     def postfix(self):
        self._postorder(self.root)
        print()
        

     def _postorder(self,p):
        if p == None:
            return
        self._postorder(p.lchild)
        self._postorder(p.rchild)
        print(p.info, end = " ")
        

     def parenthesizedInfix(self):
         self._inorder(self.root)
         print()
      

     def _inorder(self, p):
         if p == None:
            return

         if isOperator(p.info):
            print("(", end = "")

         self._inorder(p.lchild)
         print(p.info, end = " ")
         self._inorder(p.rchild)

         if isOperator(p.info):
            print(")",end = "")

       
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


     def evaluate(self):
        if self.root == None:
            return 0
        else:
            return self._evaluate(self.root)


     def _evaluate(self, p):
        if not isOperator(p.info) :
            return ord(p.info)-48

        leftValue = self._evaluate(p.lchild)
        rightValue = self._evaluate(p.rchild)
    
        if p.info=='+':
           return leftValue + rightValue
        elif p.info=='-':
           return leftValue - rightValue
        elif p.info=='*':
           return leftValue * rightValue
        else:
           return leftValue // rightValue


def isOperator(c):
    if c == '+' or c == '-' or c == '*' or c == '/' or c == '^':
        return True
    return False
    
##############################################################################################
if __name__ == '__main__':

    tree = ExpressionTree()
      
    postfix = "54+12*3*-"
  
    tree.buildTree(postfix)
    tree.display()
    
    print("Prefix : ")
    tree.prefix()
    
    print("Postfix : ")
    tree.postfix()
    
    print("Infix : ")
    tree.parenthesizedInfix()
        
    print("Value : " , tree.evaluate() )

   
        

