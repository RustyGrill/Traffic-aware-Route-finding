import random
from algorithms.dijkstra import dijkstra  # ✅ import added

def create_sample_graph():
    graph = {
        'A': ['B', 'C'],
        'B': ['A', 'D'],
        'C': ['A', 'D'],
        'D': ['B', 'C', 'E'],
        'E': ['D']
    }
    return graph

def generate_traffic_weights(graph):
    edge_weights = {}
    for u in graph:
        for v in graph[u]:
            weight = random.randint(1, 10)
            edge_weights[(u, v)] = weight
    return edge_weights

def print_graph(graph, edge_weights):
    print("\n📍 Map with Simulated Traffic:")
    for u in graph:
        for v in graph[u]:
            print(f"{u} ➜ {v} : {edge_weights[(u, v)]}")

def main():
    graph = create_sample_graph()
    edge_weights = generate_traffic_weights(graph)
    print_graph(graph, edge_weights)

    start = input("\nEnter start node: ").strip().upper()
    goal = input("Enter goal node: ").strip().upper()

    if start not in graph or goal not in graph:
        print("❌ Invalid nodes.")
        return

    path, cost = dijkstra(graph, edge_weights, start, goal)
    print(f"\n✅ Shortest path from {start} to {goal}: {' -> '.join(path)}")
    print(f"🧮 Total cost: {cost}")

if __name__ == "__main__":
    main()
