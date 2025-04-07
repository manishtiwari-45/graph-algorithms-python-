# Function to generate a spanning tree from a connected graph using DFS
# A spanning tree connects all nodes with minimum possible edges (n - 1 edges for n nodes)

def spanning_tree(n, edges):
    # Creating adjacency list
    adj = [[] for _ in range(n)]
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)

    visited = [0] * n
    tree_edges = []

    # DFS to explore nodes and build tree
    def explore(node):
        visited[node] = 1
        for neighbour in adj[node]:
            if visited[neighbour] == 0:
                tree_edges.append((node, neighbour))
                explore(neighbour)

    # Start DFS from node 0
    explore(0)

    return tree_edges


# ✅ Test Case 1: Connected graph with extra edges
edges1 = [(0, 1), (0, 2), (1, 2), (1, 3), (3, 4)]
n1 = 5
tree1 = spanning_tree(n1, edges1)

print("Spanning Tree Edges:")
for edge in tree1:
    print(edge)
# Output: Should contain 4 edges connecting all 5 nodes