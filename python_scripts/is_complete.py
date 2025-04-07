# Function to check if the given graph is a complete graph
# A complete graph is one where each node is connected to every other node

def complete_graph(graph, node_list):
    for node in node_list:
        # Each node should have exactly (n - 1) neighbors in a complete graph
        if node not in graph or len(graph[node]) != len(node_list) - 1:
            return False
    return True

# Test case 1: Given graph is not complete
node_list = ['a', 'b', 'c', 'd', 'e', 'f']
AdjList = {
    'a': ['b', 'd', 'e'],
    'b': ['a', 'd', 'c'],
    'c': ['b', 'd'],
    'd': ['a', 'b', 'c', 'e'],
    'e': ['a', 'd', 'f'],
    'f': ['e']
}

print("Is the graph complete? :", complete_graph(AdjList, node_list))  # Output: False
