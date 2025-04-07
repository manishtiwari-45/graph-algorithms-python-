# Function to check if the given undirected graph can represent a Binary Tree
# In a binary tree:
# - Root node (assumed as node 0 here) has at most 2 children → degree ≤ 2
# - Other nodes can have 1 parent and up to 2 children → degree ≤ 3

def is_binary_tree(n, edges):
    # Step 1: Create an adjacency list
    adj = []
    for i in range(n):
        temp = []
        adj.append(temp)

    # Step 2: Fill the adjacency list with undirected edges
    for e in edges:
        u = e[0]
        v = e[1]
        adj[u].append(v)
        adj[v].append(u)

    # Step 3: Check degree condition for binary tree
    for i in range(n):
        count = 0
        for j in range(len(adj[i])):
            count += 1
        # For root (assumed node 0), max 2 neighbors
        if i == 0:
            if count > 2:
                return False
        else:
            # Other nodes can have at most 3 neighbors (1 parent + 2 children)
            if count > 3:
                return False

    return True


# ✅ Test Case 1 (Valid Binary Tree)
edges1 = [(0, 1), (0, 2), (1, 3), (1, 4)]
n1 = 5
# All degrees valid → It's a binary tree
print("Yes" if is_binary_tree(n1, edges1) else "No")