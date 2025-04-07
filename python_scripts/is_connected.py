from collections import deque

# Function to check if the graph is connected or not using BFS
# A graph is connected if all nodes are reachable from any starting node

def is_connected(graph, node_list):
    visited = []  # list to keep track of visited nodes
    Q = deque()   # queue for BFS

    # Start BFS from the first node in the node list
    Q.append(node_list[0])
    visited.append(node_list[0])

    while Q:
        node = Q.popleft()
        if node in graph:
            for neighbor in graph[node]:
                if neighbor not in visited:
                    visited.append(neighbor)
                    Q.append(neighbor)

    # If all nodes are visited, graph is connected
    return len(visited) == len(node_list)


# Test case 1: Connected graph
node_list = ['a', 'b', 'c', 'd', 'e', 'f']
AdjList = {
    'a': ['b', 'd', 'e'],
    'b': ['a', 'd', 'c'],
    'c': ['b', 'd'],
    'd': ['a', 'b', 'c', 'e'],
    'e': ['a', 'd', 'f'],
    'f': ['e']
}
print("Is the graph connected? :", is_connected(AdjList, node_list))  # Output: True