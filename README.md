# 🛣️ Traffic-aware Path Finding

A **DSA-powered route planner** with a live-updating **desktop GUI** that visualizes paths between map locations using classic graph algorithms. Includes real-time **traffic simulation** by dynamically changing road weights.

---

## 🔧 Features

- 🧭 **Shortest Path Finding** using **Dijkstra** and **A\***  
- 🌐 **All-Pairs Shortest Paths** using **Floyd-Warshall**  
- 🚦 **Traffic Simulation** with random dynamic weights  
- 📈 **Live Graph Visualization** using `networkx` & `matplotlib`  
- 🧩 **Connectivity Checks** via **Disjoint Set Union (DSU)**  
- 💻 **Desktop GUI** built with **Tkinter**

---

## 📚 Algorithms Used

| Algorithm           | Purpose                        |
|---------------------|--------------------------------|
| Dijkstra            | Single-source shortest path    |
| A* Search           | Heuristic pathfinding          |
| Floyd-Warshall      | All-pairs shortest paths       |
| Disjoint Set Union  | Connectivity checks            |

---

## 🚀 How to Run

```bash
git clone https://github.com/yourusername/Traffic-aware-path-finding
cd Traffic-aware-path-finding
python gui.py
