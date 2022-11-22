"""------------------L I S T S----------------"""
l1 = [[]] * 4
print(l1) #output [[], [], [], []]
l1.append(1)
print(l1) #output [[], [], [], [], 1]
l1[0].append(1) 
print(l1) #output [[1], [1], [1], [1], 1]


# -----A N O T H E R - W A Y-------------
print(list(range(5))) #output [0, 1, 2, 3, 4]

l2 = [ _*2 for _ in range(10)] #l2 = [ return[x] for x[0] in range(10)]
print(l2) #output [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]   

l3 = [[] for _ in range(10)]
print(l3) #output [[], [], [], [], [], [], [], [], [], []]
l3[0].append(1)
print(l3) #output [[1], [], [], [], [], [], [], [], [], []]

edge = 6

for edge in edges:
    print(edge)

