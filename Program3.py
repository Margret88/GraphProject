class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.edges = []

    def add_edge(self, u, v, weight):
        self.edges.append((weight, u, v))

    def find(self, parent, i):
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])

    def union(self, parent, rank, x, y):
        root_x = self.find(parent, x)
        root_y = self.find(parent, y)

        if rank[root_x] < rank[root_y]:
            parent[root_x] = root_y
        elif rank[root_x] > rank[root_y]:
            parent[root_y] = root_x
        else:
            parent[root_y] = root_x
            rank[root_x] += 1

    def kruskal_mst(self):
        # Sort edges by weight
        self.edges.sort()
        parent = []
        rank = []
        
        # Initialize parent and rank arrays
        for node in range(self.vertices):
            parent.append(node)
            rank.append(0)

        mst = []
        mst_cost = 0

        for edge in self.edges:
            weight, u, v = edge
            root_u = self.find(parent, u)
            root_v = self.find(parent, v)

            # If including this edge doesn't form a cycle
            if root_u != root_v:
                mst.append(edge)
                mst_cost += weight
                self.union(parent, rank, root_u, root_v)

        return mst, mst_cost



graph = Graph(6)

# Add edges (u, v) with weights (costs)
graph.add_edge(0, 1, 10)  # Edge between city 0 and city 1 with cost 10
graph.add_edge(0, 2, 15)
graph.add_edge(1, 2, 5)
graph.add_edge(1, 3, 20)
graph.add_edge(2, 3, 30)
graph.add_edge(3, 4, 10)
graph.add_edge(4, 5, 5)
graph.add_edge(3, 5, 25)

# Find MST and its cost
mst_edges, mst_cost = graph.kruskal_mst()

print("Edges in the Minimum Spanning Tree:")
for edge in mst_edges:
    print(f"{edge[1]} -- {edge[2]} == {edge[0]}")

print(f"Total cost of MST: {mst_cost}")