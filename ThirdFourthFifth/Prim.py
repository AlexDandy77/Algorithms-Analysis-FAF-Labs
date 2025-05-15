def prim_algorithm(adj_matrix):
    size = len(adj_matrix)
    in_mst = [False] * size
    key = [float('inf')] * size
    parent = [-1] * size

    key[0] = 0  # Start from vertex 0

    for _ in range(size):
        u = min((v for v in range(size) if not in_mst[v]), key=lambda v: key[v], default=-1)
        if u == -1:
            break
        in_mst[u] = True

        for v in range(size):
            if 0 < adj_matrix[u][v] < key[v] and not in_mst[v]:
                key[v] = adj_matrix[u][v]
                parent[v] = u

    mst = [(parent[i], i, adj_matrix[parent[i]][i]) for i in range(1, size) if parent[i] != -1]
    return mst
