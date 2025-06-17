import tkinter as tk
from tkinter import ttk
from algorithms.dijkstra import dijkstra
from algorithms.a_star import a_star
from algorithms.floyd_warshall import floyd_warshall, reconstruct_path
import random
import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# ----------- Graph & Weights ------------

nodes = ['A', 'B', 'C', 'D', 'E']
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'C', 'D'],
    'C': ['A', 'B', 'D', 'E'],
    'D': ['B', 'C', 'E'],
    'E': ['C', 'D']
}
edge_weights = {
    ('A', 'B'): 4, ('B', 'A'): 4,
    ('A', 'C'): 2, ('C', 'A'): 2,
    ('B', 'C'): 5, ('C', 'B'): 5,
    ('B', 'D'): 10, ('D', 'B'): 10,
    ('C', 'D'): 3, ('D', 'C'): 3,
    ('C', 'E'): 7, ('E', 'C'): 7,
    ('D', 'E'): 1, ('E', 'D'): 1
}

# ----------- GUI Setup ------------

window = tk.Tk()
window.title("PathPilot GUI - Traffic Aware Route Finder")
window.geometry("800x600")

start_var = tk.StringVar()
goal_var = tk.StringVar()
output_text = tk.StringVar()

# Dropdowns
frame = tk.Frame(window)
frame.pack(pady=10)
tk.Label(frame, text="Start:").grid(row=0, column=0)
ttk.Combobox(frame, textvariable=start_var, values=nodes).grid(row=0, column=1, padx=10)
tk.Label(frame, text="Goal:").grid(row=0, column=2)
ttk.Combobox(frame, textvariable=goal_var, values=nodes).grid(row=0, column=3, padx=10)

# ----------- Graph Drawing ------------
G = nx.DiGraph()
for node in graph:
    for neighbor in graph[node]:
        G.add_edge(node, neighbor, weight=edge_weights[(node, neighbor)])

fig, ax = plt.subplots(figsize=(5, 4))
canvas = FigureCanvasTkAgg(fig, master=window)
canvas.get_tk_widget().pack()
pos = nx.spring_layout(G)

def draw_graph():
    ax.clear()
    edge_labels = {(u, v): edge_weights[(u, v)] for u, v in G.edges()}
    nx.draw(G, pos, ax=ax, with_labels=True, node_color='skyblue', node_size=700, font_weight='bold')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, ax=ax)
    canvas.draw()

def simulate_traffic():
    for edge in edge_weights:
        edge_weights[edge] = random.randint(1, 15)
    for u, v in G.edges():
        G[u][v]['weight'] = edge_weights[(u, v)]
    output_text.set("🚦 Traffic updated! Run a pathfinding algorithm.")
    draw_graph()

def run_dijkstra():
    start, goal = start_var.get(), goal_var.get()
    if not start or not goal:
        output_text.set("Please select both start and goal.")
        return
    path, cost = dijkstra(graph, edge_weights, start, goal)
    output_text.set(f"Dijkstra: {' -> '.join(path)} (Cost: {cost})")

def run_a_star():
    start, goal = start_var.get(), goal_var.get()
    if not start or not goal:
        output_text.set("Please select both start and goal.")
        return
    path, cost = a_star(graph, edge_weights, start, goal)
    output_text.set(f"A*: {' -> '.join(path)} (Cost: {cost})")

def run_floyd():
    start, goal = start_var.get(), goal_var.get()
    if not start or not goal:
        output_text.set("Please select both start and goal.")
        return
    dist_matrix, next_node = floyd_warshall(graph, edge_weights)
    if dist_matrix[start][goal] == float('inf'):
        output_text.set("No path exists.")
    else:
        path = reconstruct_path(next_node, start, goal)
        output_text.set(f"Floyd-Warshall: {' -> '.join(path)} (Cost: {dist_matrix[start][goal]})")

# Buttons
button_frame = tk.Frame(window)
button_frame.pack(pady=10)
tk.Button(button_frame, text="🚦 Simulate Traffic", command=simulate_traffic).grid(row=0, column=0, padx=10)
tk.Button(button_frame, text="Dijkstra", command=run_dijkstra).grid(row=0, column=1, padx=10)
tk.Button(button_frame, text="A* Search", command=run_a_star).grid(row=0, column=2, padx=10)
tk.Button(button_frame, text="Floyd-Warshall", command=run_floyd).grid(row=0, column=3, padx=10)

# Output label
tk.Label(window, textvariable=output_text, font=("Consolas", 12), fg="darkblue").pack(pady=10)

# Initial draw
draw_graph()

# Run app
window.mainloop()
