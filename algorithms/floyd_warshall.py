def floyd_warshall(graph, edge_weights):
    nodes = list(graph.keys())
    dist = {u: {v: float('inf') for v in nodes} for u in nodes}

    for node in nodes:
        dist[node][node] = 0

    for (u, v), w in edge_weights.items():
        dist[u][v] = min(dist[u][v], w)

    for k in nodes:
        for i in nodes:
            for j in nodes:
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

    return dist
