def kruskal_algorithm(size, edges):
    parent = list(range(size))
    rank = [0] * size

    def find(i):
        if parent[i] != i:
            parent[i] = find(parent[i])
        return parent[i]

    def union(x, y):
        xroot = find(x)
        yroot = find(y)
        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot
        else:
            parent[yroot] = xroot
            rank[xroot] += 1

    mst = []
    edges = sorted(edges, key=lambda x: x[2])  # Sort by weight

    for u, v, weight in edges:
        if find(u) != find(v):
            mst.append((u, v, weight))
            union(u, v)

    return mst


def extract_edges_from_adj_matrix(adj_matrix):
    size = len(adj_matrix)
    edges = []
    for i in range(size):
        for j in range(i + 1, size):  # avoid double-counting (undirected graph)
            weight = adj_matrix[i][j]
            if weight != 0 and weight != float('inf'):
                edges.append((i, j, weight))
    return edges
