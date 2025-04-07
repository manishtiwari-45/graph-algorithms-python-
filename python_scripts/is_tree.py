# Function to check if the graph is a tree
# A graph is a tree if:
# 1. It has exactly n-1 edges for n nodes
# 2. It is fully connected (no disconnected parts)
# 3. It has no cycles

def is_tree(n, edges):
    # Tree must have exactly n-1 edges
    if len(edges) != n - 1:
        return False

    # Creating adjacency list
    adj = [[] for _ in range(n)]
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)

    visited = [0] * n

    # DFS function to detect cycle
    def explore(node, parent):
        visited[node] = 1
        for neighbour in adj[node]:
            if visited[neighbour] == 0:
                if not explore(neighbour, node):
                    return False
            elif neighbour != parent:
                return False  # Cycle detected
        return True

    # Start DFS from node 0
    if not explore(0, -1):
        return False

    # If any node remains unvisited, the graph is disconnected
    if any(v == 0 for v in visited):
        return False

    return True


# ✅ Test Case 1: Valid Tree
edges1 = [(0, 1), (0, 2), (1, 3), (1, 4)]
n1 = 5
print("Is the graph a tree?", is_tree(n1, edges1))  # Output: True

# ❌ Test Case 2: Graph with a cycle
edges2 = [(0, 1), (1, 2), (2, 0), (1, 3)]
n2 = 4
print("Is the graph a tree?", is_tree(n2, edges2))  # Output: False