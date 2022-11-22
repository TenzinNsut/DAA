# Binary Search tree


class BST:
    def __init__(self,inval):
        self.value = inval
        if(self.inval == None):
            self.left = None
            self.right = None
        else:
            self.left=BST()
            self.right=BST()


# insertion
    def insert(self,val):
        if (self.value==None):
            val = self.value
            self.left=BST()
            self.right=BST()
        else:
            if self.value == val:
                print("Value already exits")
                return
            else:
                if self.value < val:
                    self.right.insert(val)
                    return
                else:
                    self.left.insert(val)
                    return





# '__str__' is used for string representation of object
# '__repr__' is used for object representation of string

# here '[self.value]' is root

# Inorder traversal
# left->root>right
    def inorder(self):
        if self.value == None:
            return([])
        else:
            return(self.left.inorder()+[self.value]+self.right.inorder())

# Display Inorer traversal
    def __str__(self):
        return(str(self.inorder()))


# Post order traversal
# left-> right-> root
    def postorder(self):
        if self.value ==None:
            return([])

        else:
            return (self.left.postorder()+self.right.postorder()+[self.value])

# Display post order
    def __str__(self):
        return(str(self.postorder()))
    



# PreOrder traversal
# root->left->right
    def preorder(self):
        if self.value == None:
            return([])
        else:
            return ([self.value]+self.left.preorder()+self.right.preorder())

    def __str__(self):
        return(str(self.preorder()))


    

# Searching
    def search(self,val):
        if self.value == None:
            print(val," is not present in the BST")
            return (False)
        # key is the root value
        if self.value == val:  
            print(val,"found!")
            return(True)
        if val>self.value:
            self.right.search(val)
        else:
            self.left.search(val)
