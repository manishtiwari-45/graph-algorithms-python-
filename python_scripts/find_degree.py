# List of all nodes present in the graph
node_list = ['A', 'B', 'C', 'D', 'E', 'F']

# Graph representation using Adjacency List
# Each key is a node, and its value is the list of neighbors it's directly connected to
AdjList = {
    'A': ['B', 'D', 'E'],
    'B': ['A', 'D', 'C'],
    'C': ['B', 'D'],
    'D': ['A', 'B', 'C', 'E'],
    'E': ['A', 'D', 'F'],
    'F': ['E']
}

# Graph representation using Adjacency Matrix
# A 2D matrix where 1 represents an edge between nodes and 0 means no edge
adjMat = [
    [0, 1, 0, 1, 1, 0],  # Connections for A
    [1, 0, 1, 1, 0, 0],  # Connections for B
    [0, 1, 0, 1, 0, 0],  # Connections for C
    [1, 1, 1, 0, 1, 0],  # Connections for D
    [1, 0, 0, 1, 0, 1],  # Connections for E
    [0, 0, 0, 0, 1, 0]   # Connections for F
]

# Graph representation using Edge List
# Each tuple represents an edge between two nodes
EdgeList = [('A', 'B'), ('A', 'D'), ('A', 'E'), ('B', 'D'), ('B', 'C'),
            ('C', 'D'), ('D', 'E'), ('E', 'F')]

# Function to calculate the degree of each node in a graph
# Works for all three representations: Adjacency List, Adjacency Matrix, and Edge List
def node_degree(L):
    deg_dict = {}  # Dictionary to store node and its degree
    
    # If input is an Adjacency List (dictionary type)
    if type(L) == dict:
        for i in L:
            deg_dict[i] = len(L[i])  # Degree is the number of neighbors
    
    # If input is an Adjacency Matrix (list of lists)
    elif type(L) == list and type(L[0]) == list:
        for i in range(len(L)):
            count = 0
            for j in range(len(L[i])):
                if L[i][j] == 1:
                    count += 1  # Count number of 1s in the row
            deg_dict[node_list[i]] = count  # Assign degree to corresponding node

    # If input is an Edge List (list of tuples)
    elif type(L) == list and type(L[0]) == tuple:
        for node in node_list:
            deg_dict[node] = 0  # Initialize degree of all nodes to 0
        for i in range(len(L)):
            u = L[i][0]
            v = L[i][1]
            deg_dict[u] += 1  # Each edge increases degree of both nodes
            deg_dict[v] += 1

    return manual_sort(deg_dict)  # Sort degrees and return

# Function to sort the dictionary of degrees in ascending order using bubble sort
def manual_sort(deg_dict):
    keys = []
    values = []

    # Separate keys and values
    for i in deg_dict:
        keys.append(i)
        values.append(deg_dict[i])

    # Bubble sort based on values
    for i in range(len(values)):
        for j in range(i+1, len(values)):
            if values[i] > values[j]:
                # Swap values
                temp = values[i]
                values[i] = values[j]
                values[j] = temp

                # Swap corresponding keys
                temp_key = keys[i]
                keys[i] = keys[j]
                keys[j] = temp_key

    # Create sorted dictionary
    sorted_deg = {}
    for i in range(len(keys)):
        sorted_deg[keys[i]] = values[i]

    return sorted_deg

# Example: calculating degree using adjacency matrix
print(node_degree(adjMat))
