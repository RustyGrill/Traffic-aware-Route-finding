import math

def floyd_warshall(graph, edge_weights):
    nodes = list(graph.keys())
    dist = {u: {v: math.inf for v in nodes} for u in nodes}
    next_node = {u: {v: None for v in nodes} for u in nodes}

    # Initialize distances with edge weights
    for u in nodes:
        dist[u][u] = 0
        for v in graph[u]:
            dist[u][v] = edge_weights[(u, v)]
            next_node[u][v] = v

    # Floyd-Warshall algorithm
    for k in nodes:
        for i in nodes:
            for j in nodes:
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
                    next_node[i][j] = next_node[i][k]

    return dist, next_node

def reconstruct_path(next_node, start, end):
    if next_node[start][end] is None:
        return None  # No path
    path = [start]
    while start != end:
        start = next_node[start][end]
        path.append(start)
    return path
