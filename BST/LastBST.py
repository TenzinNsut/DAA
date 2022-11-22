# consider -> self.value as root
class BST():
    # defining constructor
    def __init__(self,initil_Value=None):
        #root
        self.value = initil_Value
        # 1.) tree is empty
        if(self.value == None):
            self.right = None
            self.left = None
        # 2.) tree is not empty
        else:
            self.left = BST()
            self.right = BST()


# For insertion
    def insert(self, key):
        # 1.) root is empty
        if (self.value == None):
            self.value = key
            self.right = BST()
            self.left = BST()
            return
        else:
            # 2.) check if value alredy exists
            if (self.value == key):
                print(key," already exits in tree")
                return
            else:
                if(key>self.value):
                    self.right.insert(key)
                    return
                else:
                    self.left.insert(key)
                    return

# TREE TRAVERSALS

    # inorder
    def inorder(self):
        if(self.value == None):# if tree is empty
            return ([])
        else:
            return (self.left.inorder()+ [self.value]+ self.right.inorder()) # we need this as string --> def __str__

    # pre-order
    def preorder(self):
        if(self.value == None):
            return ([])
        else:
            return([self.value]+self.left.preorder()+self.right.preorder())

    # post-order
    def postorder(self):
        if(self.value == None):
            return([])
        else:
            return (self.left.postorder()+self.right.postorder()+[self.value])


# __str__(magic method) to convert your object to string
    
    # display inorder
    def __str__(self):
        return(str(self.inorder()))
    
     # display pre-order
    def __str__(self):
        return(str(self.preorder()))

    # display post-order
    def __str__(self):
        return(str(self.postorder()))



# min-value 
    def  minvalue(self):
        # if right subtree is emtpy-> return (root)
        if(self.left.value == None):
            return (self.value)
        else:
            return (self.left.minvalue()) #recusively call the left sub-tree

# max-value
    def maxvalue(self):
        # if right subtree is empty -> return (root)
        if(self.right.value==None):
            return (self.value)
        else:
            return(self.right.maxvalue())


    # To find a key/value
    def find(self,key):
        # 1.) Tree is empty
        if (self.value == None):
            print (key,"not found! ")
            return(False)

        # 2.) root == key
        if(self.value == key):
            print (key,"found!")
            return(True)

        # 3.) key > root --> search right-subtree
        if(key>self.value):
            self.right.find(key)

        # 4.) key < root ---> search left-subtree
        else:
            self.left.find(key)

    
    # To Delete a key/value
    def delete(self,key):
        if(self.value == None):
            print("tree is empty")
            return
        # deleting parent node  
        if(self.value == key):
            # leaf node
            if(self.left == None and self.right == None):
                self.value = None
                self.right = None
                self.left = None
                return

            if(self.left.value == None):
                self.value = self.right.value
                self.left = self.right.left
                self.right = self.right.right
                return
            else:
                self.value = self.left.maxvalue()
                self.left(self.left.maxvalue())

        if( key < self.value):
            self.left.delete(key)
            return
        
        if(key > self.value):
            self.right.delete(key)
            return



            









run1 = BST()

for i in [50,60,80,40,45,46,43,57,38]:
    run1.insert(i)

print([50,60,80,40,45,46,43,57,38])
print(run1.delete(38))
print("Inorder Traversal :",run1.inorder())
print("max-value: ",run1.maxvalue())
print(run1.find(50))

