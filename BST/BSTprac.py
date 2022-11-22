class BST():
    def __init__(self, initial_value = None):
        self.value = initial_value
        if(self.value == None):
            self.left = None
            self.right = None
        else:
            self.left  = BST()
            self.right = BST()

    
    def insert(self, key):
        if(self.value == None):
            self.value = key
            self.left = BST()
            self.right = BST()
            return

        else:
            if(self.value == key):
                print(key, "already exists")
                return
        
            if(key > self.value):
                self.right.insert(key)
                return
            else:
                self.left.insert(key)
                return

    
    def inorder(self):
        if(self.value == None):
            return ([])
        else:
            return(self.left.inorder() + [self.value]+ self.right.inorder())

    def postorder(self):
        if(self.value == None):
            return ([])
        else:
            return(self.left.postorder() + self.right.postorder()+ [self.value])

    def preoder(self):
        if(self.value == None):
            return([])
        else:
            return ([self.value]+self.left.preoder() + self.right.preoder())

    
    def __str__(self):
        return(str(inorder()))
    
    def __str__(self):
        return(str(postorder()))
    
    def __str__(self):
        return(str(preoder()))


    def maxvalue(self):
        if(self.right.value == None):
            return (self.value)
        else:
            return (self.right.maxvalue())

    def minvalue(self):
        if(self.left.value == None):
            return (self.value)
        else:
            return (self.left.minvalue())


    def find(self,key):
        if self.key == key:
            return f"{self.key} exists."
        if(self.key > key):
            self.left.find(key)
            return
        else:
            self.right.find(key)
            return




b1 = BST()
print("DATA: ",[12,65,34,56,21])
print("------------------------------------------------")


for i in [12,65,34,56,21]:
    b1.insert(i)


print("Inorder: ",b1.inorder())
print("PreOrder: ",b1.preoder())
print("PostOrder: ",b1.postorder())
print("maxValue: ",b1.maxvalue())
print("minValue: ",b1.minvalue())
print("find:", b1.find(34))