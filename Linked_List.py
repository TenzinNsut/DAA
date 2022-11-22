# For creating NewNode
class Node:
    def __init__(self,data):
        self.data = data
        self.ref = None

# define head and set it to empty(initially), For linking nodes
class LinkedList:
    def __init__(self):
        self.head = None

# For traversal of linked list
    def printLL(self):
        if self.head is None: #check is linked list is empty or not
            print("The linked list is empty")
        else:
            n = self.head
            while n is not None:
                print(n.data) #print the data inside the node
                n = n.ref #point to next node
        
    def inBeg(self,data):
        newNode = Node(data) #Creat a newnode with node class and insert the data inside it
        newNode.ref = self.head #reffernce, Newnode will point to old head node, NewNode reffernce will store, address of old head node
        self.head = newNode #This Node will be considerd as the head node


l1 = LinkedList()
l1.inBeg(12)
l1.inBeg(45)
l1.inBeg(32)
l1.inBeg(76)
l1.inBeg(234)
l1.inBeg(1542)
l1.printLL()

