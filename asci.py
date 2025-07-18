import math
from collections import defaultdict

def connectedSum(graph_nodes, graph_from, graph_to):
    # Build the adjacency list
    graph = defaultdict(list)
    for u, v in zip(graph_from, graph_to):
        graph[u].append(v)
        graph[v].append(u)

    visited = [False] * (graph_nodes + 1)  # Indexing nodes starting from 1

    # Function to perform DFS to find all nodes in a connected component
    def dfs(node):
        stack = [node]
        count = 0
        while stack:
            current = stack.pop()
            if not visited[current]:
                visited[current] = True
                count += 1
                for neighbor in graph[current]:
                    if not visited[neighbor]:
                        stack.append(neighbor)
        return count

    total_sum = 0

    # Loop over each node to find connected components
    for node in range(1, graph_nodes + 1):
        if not visited[node]:  # If not visited, this is a new component
            component_size = dfs(node)
            if component_size > 0:
                # Calculate the sum of ceil(sqrt(size of component * 7))
                total_sum += math.ceil(math.sqrt(component_size))

    return total_sum

# Test the function with the provided input
graph_nodes = 10
graph_from = [1, 1, 2, 3, 7]
graph_to = [2, 3, 4, 5, 8]

# Expected output: 8
print(connectedSum(graph_nodes, graph_from, graph_to))
