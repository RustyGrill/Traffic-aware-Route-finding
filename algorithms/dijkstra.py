import heapq

def dijkstra(graph, edge_weights, start, goal):
    pq = [(0, start)]
    dist = {node: float('inf') for node in graph}
    parent = {node: None for node in graph}
    dist[start] = 0

    while pq:
        cost, u = heapq.heappop(pq)

        if u == goal:
            break

        for v in graph[u]:
            weight = edge_weights[(u, v)]
            if dist[u] + weight < dist[v]:
                dist[v] = dist[u] + weight
                parent[v] = u
                heapq.heappush(pq, (dist[v], v))

    # Reconstruct path
    path = []
    curr = goal
    while curr:
        path.append(curr)
        curr = parent[curr]
    path.reverse()

    return path, dist[goal]
