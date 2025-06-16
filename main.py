import random

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

if __name__ == "__main__":
    main()
