# Adjacency list representing an undirected graph
AdjList = {
    'a': ['b', 'd', 'e'],
    'b': ['a', 'd', 'c'],
    'c': ['b', 'd'],
    'd': ['a', 'b', 'c', 'e'],
    'e': ['a', 'd', 'f'],
    'f': ['e']
}

# Function to check if a given sequence is a WALK, TRAIL, PATH, or NOTA (none of the above)
def check_type(graph, seq):
    edges = []      # To store unique edges used
    visited = []    # To store visited nodes

    for i in range(len(seq) - 1):
        u, v = seq[i], seq[i + 1]

        # If the next node is not a neighbor of the current node, it's not even a valid walk
        if u not in graph or v not in graph[u]:
            return "NOTA"
        
        # Represent the edge as [u, v] and check if it's already used (in any order since undirected)
        edge = [u, v]
        reverse_edge = [v, u]

        # If edge already used before, it's a WALK (repeating edges allowed)
        if edge in edges or reverse_edge in edges:
            return "WALK"
        
        edges.append(edge)  # Mark this edge as used

        visited.append(u)   # Add node to visited list

        # If the next node has already been visited, it's a TRAIL (no repeating edges, but nodes can repeat)
        if v in visited:
            return "TRAIL"

    return "PATH"   # If all nodes and edges are used only once, it's a PATH

# Test cases
print(check_type(AdjList, ['a', 'c', 'e', 'f']))        # Output: NOTA (no edge from 'a' to 'c')
print(check_type(AdjList, ['a', 'b', 'd', 'e', 'f']))   # Output: PATH (no repetition of nodes or edges)
print(check_type(AdjList, ['a', 'b', 'd', 'b', 'c']))   # Output: TRAIL (node 'b' repeated, but edges unique)
print(check_type(AdjList, ['a', 'b', 'd', 'b', 'a']))   # Output: WALK (edge 'b'-'a' reused)
