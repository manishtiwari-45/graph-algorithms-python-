AdjList = {
    'a': ['b', 'd', 'e'],
    'b': ['a', 'd', 'c'],
    'c': ['b', 'd'],
    'd': ['a', 'b', 'c', 'e'],
    'e': ['a', 'd', 'f'],
    'f': ['e']
}

def check_type(graph, seq):
    edges = []
    visited = []

    for i in range(len(seq) - 1):
        u, v = seq[i], seq[i + 1]
        if u not in graph or v not in graph[u]:
            return "NOTA"
        
        edge = [u, v]
        reverse_edge = [v, u]

        if edge in edges or reverse_edge in edges:
            return "WALK"
        
        edges.append(edge)

        visited.append(u)
        if v in visited:
            return "TRAIL"

    return "PATH"

print(check_type(AdjList, ['a', 'c', 'e', 'f']))        
print(check_type(AdjList, ['a', 'b', 'd', 'e', 'f']))  
print(check_type(AdjList, ['a', 'b', 'd', 'b', 'c']))   
print(check_type(AdjList, ['a', 'b', 'd', 'b', 'a']))  