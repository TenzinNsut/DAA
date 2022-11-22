class Node:

    def __init__(self, initial_Value = None):
        self.value = initial_Value
        self.next = None
        return
    
    def isempty(self):
        if (self.value == None):
            return (True)
        else:
            return (False)

# insert in the next node
    def append(self,data):
        # if node is empty --> insert value
        if self.isempty():
            self.value = data

        elif self.next == None:
            # create a new node
            newnode = Node(data)
            self.next = newnode
        else:
            self.next.append(data)
            # newnode.append(v)
        return

# inserting node in the begging
    def insert(self,data):
        

            
