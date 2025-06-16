import random
from algorithms.dijkstra import dijkstra
from algorithms.a_star import a_star
from algorithms.floyd_warshall import floyd_warshall
from algorithms.dsu import DisjointSetUnion

def create_sample_graph():
    return {
        'A': ['B', 'C'],
        'B': ['A', 'D'],
        'C': ['A', 'D'],
        'D': ['B', 'C', 'E'],
        'E': ['D'],
        'F': []  # Node F is disconnected for testing DSU
    }

def generate_traffic_weights(graph):
    edge_weights = {}
    for u in graph:
        for v in graph[u]:
            if (v, u) not in edge_weights:
                weight = random.randint(1, 10)
                edge_weights[(u, v)] = weight
                edge_weights[(v, u)] = weight
    return edge_weights

def print_graph(graph, edge_weights):
    print("📍 Graph with Traffic Weights:")
    for u in graph:
        for v in graph[u]:
            print(f"{u} -> {v} : {edge_weights[(u, v)]}")

def build_dsu(graph):
    dsu = DisjointSetUnion()
    for u in graph:
        dsu.add(u)
        for v in graph[u]:
            dsu.add(v)
            dsu.union(u, v)
    return dsu

def main():
    graph = create_sample_graph()
    edge_weights = generate_traffic_weights(graph)
    print_graph(graph, edge_weights)

    start = input("\nEnter start node: ").strip().upper()
    goal = input("Enter goal node: ").strip().upper()

    if start not in graph or goal not in graph:
        print("❌ Invalid start or goal node.")
        return

    # DSU check
    dsu = build_dsu(graph)
    if not dsu.connected(start, goal):
        print(f"\n⚠️ No path: {start} and {goal} are not connected in the graph.")
        return

    algo = input("Choose algorithm (1 = Dijkstra, 2 = A*, 3 = Floyd-Warshall): ").strip()

    if algo == '1':
        path, cost = dijkstra(graph, edge_weights, start, goal)
        print(f"\n✅ Path from {start} to {goal}: {' -> '.join(path)}")
        print(f"🧮 Total cost: {cost}")

    elif algo == '2':
        path, cost = a_star(graph, edge_weights, start, goal)
        print(f"\n✅ Path from {start} to {goal}: {' -> '.join(path)}")
        print(f"🧮 Total cost: {cost}")

    elif algo == '3':
        dist = floyd_warshall(graph, edge_weights)
        print("\n📊 All-Pairs Shortest Path Matrix:")
        for u in dist:
            for v in dist[u]:
                cost = dist[u][v]
                print(f"{u} → {v} : {'∞' if cost == float('inf') else cost}")
    else:
        print("❌ Invalid choice.")

if __name__ == "__main__":
    main()
