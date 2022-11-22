class Node:
    def __init__(self, v = None):
        self.value = v
        self.next = None
        return

    def isempty(self):
        if self.value == None:
            return(True)
        else:
            return(False)

    def append(self,v):   # append, recursive
        if self.isempty():
            self.value = v
        elif self.next == None:
            newnode = Node(v)
            self.next = newnode
        else:
            self.next.append(v)
        return

# insert node in begining
    def insert(self,v):
        if self.isempty():
            self.value = v
            return
        newnode = Node(v)
        # Exchange values in self and newnode
        (self.value, newnode.value) = (newnode.value, self.value)
        (self.next, newnode.next) = (newnode, self.next)
        return
    
# Delete function
    def delete(self,v):   # delete, recursive
        if self.isempty():
            return

        if self.value == v:
            self.value = None
            if self.next != None:
                self.value = self.next.value
                self.next = self.next.next
            return 
        else:
            if self.next != None:
                self.next.delete(v)
                if self.next.value == None:
                    self.next = None
        return 
# Length function
    def length(self):
        if self.value == None:
            return(0)
        elif self.next == None:
            return(1)
        else:
            return(1+self.next.length())            

# display function
    def __str__(self):
        selflist = []
        if self.value == None:
            return(str(selflist))
        temp = self
        selflist.append(temp.value)
        while temp.next != None:
            temp = temp.next
            selflist.append(temp.value)
        return(str(selflist))

N=Node()
for i in [45,53,23,53]:
    N.insert(i)
for i in [35,40,92,50,67]:
    N.append(i)

# Before
print("-----------Before----------")
print(N)
print("length of the node is:",N.length())

N.delete(50)
N.append(38)

# after deletion
print("---------After Deletion-----------")
print("after :",N)
print("length of the node is:",N.length())
