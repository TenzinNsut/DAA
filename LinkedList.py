# https://www.youtube.com/watch?v=B-zO18TJKYQ

# For creating a node
class Node:
    def __init__(self,data):
        self.data = data
        self.ref = None


# For linking the nodes, setting head node to none
class LinkedList:
    def __init__(self):
        self.head = None


    # for traversal of node
    def printLL(self):
        if self.head is None:
            print("The linked list is empty")
        else:
            n = self.head
            while n is not None:
                print(n.data)
                n = n.ref


# To insert data at the begining of linked list
    def inBeg(self,data):
        newNode = Node(data) #create a newnode
        newNode.ref = self.head #refer to the address of old node
        self.head=newNode  #point head to the new node
    







l1 = LinkedList()
l1.inBeg(12)
l1.inBeg(24)
l1.inBeg(323)
l1.printLL()



























