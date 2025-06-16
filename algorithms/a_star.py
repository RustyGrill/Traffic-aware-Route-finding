import heapq

def heuristic(a, b):
    # Simple heuristic: assume each edge has weight ~1
    return abs(ord(a) - ord(b))

def a_star(graph, edge_weights, start, goal):
    open_set = [(0, start)]
    g_score = {node: float('inf') for node in graph}
    f_score = {node: float('inf') for node in graph}
    came_from = {node: None for node in graph}

    g_score[start] = 0
    f_score[start] = heuristic(start, goal)

    while open_set:
        _, current = heapq.heappop(open_set)

        if current == goal:
            break

        for neighbor in graph[current]:
            tentative_g = g_score[current] + edge_weights[(current, neighbor)]
            if tentative_g < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g
                f_score[neighbor] = tentative_g + heuristic(neighbor, goal)
                heapq.heappush(open_set, (f_score[neighbor], neighbor))

    # Reconstruct path
    path = []
    node = goal
    while node:
        path.append(node)
        node = came_from[node]
    path.reverse()

    return path, g_score[goal]
