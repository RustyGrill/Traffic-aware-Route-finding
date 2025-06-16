class DisjointSetUnion:
    def __init__(self):
        self.parent = {}

    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]

    def union(self, u, v):
        u_root = self.find(u)
        v_root = self.find(v)
        if u_root != v_root:
            self.parent[v_root] = u_root

    def add(self, u):
        if u not in self.parent:
            self.parent[u] = u

    def connected(self, u, v):
        return self.find(u) == self.find(v)
