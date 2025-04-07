# Function to convert Adjacency List to Adjacency Matrix and Edge List
def AdjList_to_other(adjList, node_list):
    n = len(node_list)  # Total number of nodes

    # Initialize empty Adjacency Matrix with 0s
    adjMat = []
    for i in range(n):
        row = []
        for j in range(n):
            row.append(0)
        adjMat.append(row)

    edgeList = []  # Initialize empty Edge List

    # Fill Adjacency Matrix and create Edge List
    for u in adjList:
        for v in adjList[u]:
            i = node_list.index(u)
            j = node_list.index(v)
            adjMat[i][j] = 1  # Mark edge in the matrix

            # Avoid adding duplicate edges (undirected)
            if (v, u) not in edgeList:
                edgeList.append((u, v))

    return adjMat, edgeList  # Return both representations


# Function to convert Adjacency Matrix or Edge List to Adjacency List
def other_to_AdjList(data, node_list):
    adjList = {}  # Initialize empty Adjacency List
    for node in node_list:
        adjList[node] = []

    # If input is Adjacency Matrix
    if type(data[0]) == list:
        for i in range(len(data)):
            for j in range(len(data[i])):
                if data[i][j] == 1:
                    u = node_list[i]
                    v = node_list[j]
                    if v not in adjList[u]:  # Avoid duplicates
                        adjList[u].append(v)

    # If input is Edge List
    elif type(data[0]) == tuple:
        for i in range(len(data)):
            u = data[i][0]
            v = data[i][1]
            adjList[u].append(v)
            adjList[v].append(u)  # Since graph is undirected

    return adjList  # Return the converted Adjacency List


# Sample node list and Adjacency List for testing
node_list = ['a', 'b', 'c', 'd', 'e', 'f']

AdjList = {
    'a': ['b', 'd', 'e'],
    'b': ['a', 'd', 'c'],
    'c': ['b', 'd'],
    'd': ['a', 'b', 'c', 'e'],
    'e': ['a', 'd', 'f'],
    'f': ['e']
}


print(AdjList_to_other(AdjList,node_list))
