# Function to count the number of leaf nodes in an undirected graph
# A leaf node is defined as a node with degree 1 (i.e., connected to only one other node)

def count_leaf_nodes(n, edges):
    # Step 1: Create an adjacency matrix of size n x n initialized with 0
    adj = []
    for i in range(n):
        temp = []
        for j in range(n):
            temp.append(0)
        adj.append(temp)
    
    # Step 2: Fill the adjacency matrix with edges
    for u, v in edges:
        adj[u][v] = 1
        adj[v][u] = 1

    # Step 3: Count nodes with degree 1 (leaf nodes)
    leaf_count = 0
    for i in range(n):
        degree = 0
        for j in range(n):
            if adj[i][j] == 1:
                degree += 1
        # Leaf condition: degree = 1
        # Also handle single isolated node case: n == 1 and degree == 0
        if degree == 1 or (n == 1 and degree == 0):
            leaf_count += 1

    return leaf_count


# ✅ Test Case 
n = 5
edges = [(0, 1), (0, 2), (1, 3), (1, 4)]
# Leaf nodes: 2, 3, 4 → Total = 3
print("Leaf nodes:", count_leaf_nodes(n, edges))
