# Function to find the depth of a given node in a tree
# Depth = number of edges from the root node ('s1') to the given node

def find_depth(tree_node, node, curr=0):
    # Base case: if the node is root itself, depth is 0
    if node == "s1":  
        return curr

    # Recursive case: check each parent if it has the target node as child
    for parent, children in tree_node.items():
        if node in children:
            # Recur by moving up to the parent and increasing depth
            return find_depth(tree_node, parent, curr + 1)

    # If node not found in any child list
    return "node not found or INVALID input"


# ✅ Test Tree
Tree_nodes = {
    's1': ['s2', 's3', 's4'],
    's2': ['s5', 's6'],
    's4': ['s7', 's8', 's9'],
    's5': ['s10', 's11'],
    's6': ['s12'],
    's9': ['s13', 's14']
}

# ✅ Test Cases
print("Depth of s14:", find_depth(Tree_nodes, 's14'))   # Expected: 3
print("Depth of s1:", find_depth(Tree_nodes, 's1'))     # Expected: 0 (root)
print("Depth of xyz:", find_depth(Tree_nodes, 'xyz'))   # Expected: node not found or INVALID input
