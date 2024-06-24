#### MATRIX ####
grid = [[0, 0, 0, 0],
        [1, 1, 0, 0],
        [0, 0, 0, 1],
        [0, 1, 0, 0]]


#### ADJACENCY LIST ####
# GraphNode used for adjacency list
class GraphNode:
    def __init__(self, val):
        self.val = val
        self.neighbors = []
        
#### ADJACENCY MATRIX 
adjMatrix = [[0, 0, 0, 0],
             [1, 1, 0, 0],
             [0, 0, 0, 1],
             [0, 1, 0, 0]]

# an edge exists from v1 to v2
adjMatrix[v1][v2] = 1

# an edge exists from v2 to v1
adjMatrix[v2][v1] = 1

# No edge exists from v1 to v2
adjMatrix[v1][v2] = 0

# No edge exists from v2 to v1
adjMatrix[v2][v1] = 0
