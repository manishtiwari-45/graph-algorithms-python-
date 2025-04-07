# List of nodes
node_list = ['a', 'b', 'c', 'd', 'e', 'f']

# Adjacency List representation of graph
AdjList = {
    'a': ['b', 'd', 'e'],
    'b': ['a', 'd', 'c'],
    'c': ['b', 'd'],
    'd': ['a', 'b', 'c', 'e'],
    'e': ['a', 'd', 'f'],
    'f': ['e']
}

# Function to check if two nodes are adjacent (directly connected)
def is_adjacent(graph, v1, v2):
    if v1 in graph:
        for neighbor in graph[v1]:
            if neighbor == v2:
                return True  # If v2 is found in v1's neighbors, they are adjacent
    return False  # Otherwise, not adjacent

# Test cases
print(is_adjacent(AdjList, 'a', 'c'))  # Output: False (no edge between a and c)
print(is_adjacent(AdjList, 'a', 'b'))  # Output: True (edge exists between a and b)
