# Function to find the height of a tree using recursion (DFS)
# Height of a tree = number of edges in the longest path from root to a leaf node

def find_height(tree_nodes, node):
    # Base Case: If current node has no children, it's a leaf → height = 0
    if len(tree_nodes[node]) == 0:
        return 0 

    max_h = 0  # To track the maximum height among all child subtrees

    # Recursive step: Check height of each child
    for child in tree_nodes[node]:
        child_h = find_height(tree_nodes, child)
        max_h = max(max_h, child_h)  # Take the max among all children

    return 1 + max_h  # Add 1 for the current level

# ✅ Test Tree

Tree_nodes = {
    's4': ['s2', 's5'],
    's2': ['s1', 's3'],
    's5': [],
    's1': [],
    's3': []
}

# Height = 2 (Longest path: s4 → s2 → s1 or s3)
print("Height of tree:", find_height(Tree_nodes, 's4'))  # Output: 2
