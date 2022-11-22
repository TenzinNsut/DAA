# source : https://www.youtube.com/watch?v=SmOrBW22R2k
class Graph:
    # for creating adjacency list
    def __init__(self, num_nodes, edges):
        self.num_nodes = num_nodes
        self.data = [[] for _ in range(num_nodes)] # -> [[], [], [], [], [], [], [], [], [], []]
        for n1,n2 in edges: # -> since adjaceny list is pair - > n1,n2
            self.data[n1].append(n2)
            self.data[n2].append(n1)

    def __repr__(self):
        return "\n".join(["{}:{}".format(node,adjNode) for node,adjNode in enumerate(self.data)])

    def __str__(self):
        return self.__repr__()


# Driver code
num_nodes = 5
edges = [ (0,1),(0,4),(1,2),(1,3),(1,4),(2,3),(3,4)]

g1 = Graph(num_nodes, edges)
print(g1)
