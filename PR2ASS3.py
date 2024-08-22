class UnionFind:
     def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
     def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]
def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)
        
        if root_u != root_v:
            if self.rank[root_u] > self.rank[root_v]:
                self.parent[root_v] = root_u
            elif self.rank[root_u] < self.rank[root_v]:
                self.parent[root_u] = root_v
            else:
                self.parent[root_v] = root_u
                self.rank[root_u] += 1

def kruskal(n, edges):
    uf = UnionFind(n)
    edges.sort(key=lambda x: x[2])  # Sort edges by weight
    mst_weight = 0
    mst_edges = []

    for u, v, weight in edges:
        if uf.find(u) != uf.find(v):
            uf.union(u, v)
            mst_edges.append((u, v, weight))
            mst_weight += weight
    
    return mst_weight, mst_edges

def print_graph_and_mst(n, edges, mst_edges):
    print("\nGraph Edges:")
    for u, v, w in edges:
        print(f"Edge ({u}, {v}) with weight {w}")

    print("\nMinimum Spanning Tree Edges:")
    for u, v, w in mst_edges:
        print(f"Edge ({u}, {v}) with weight {w}")

    if __name__ == "__main__":
        n = int(input("Enter the number of vertices: "))
        edges = []
        print("Enter edges in the format: vertex1 vertex2 weight")
        print("Type 'done' when finished.")
    
    while True:
        line = input()
        if line.lower() == 'done':
            break
        u, v, w = map(int, line.split())
        edges.append((u, v, w))
    
    mst_weight, mst_edges = kruskal(n, edges)
    print(f"\nMinimum cost of the MST: {mst_weight}")
    print_graph_and_mst(n, edges, mst_edges)
