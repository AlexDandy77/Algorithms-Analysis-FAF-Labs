def dijkstra(adj_matrix, start_vertex):
    size = len(adj_matrix)
    distances = [float('inf')] * size
    distances[start_vertex] = 0
    visited = [False] * size

    for _ in range(size):
        min_distance = float('inf')
        u = None
        for i in range(size):
            if not visited[i] and distances[i] < min_distance:
                min_distance = distances[i]
                u = i

        if u is None:
            break

        visited[u] = True

        for v in range(size):
            if adj_matrix[u][v] != 0 and not visited[v]:
                alt = distances[u] + adj_matrix[u][v]
                if alt < distances[v]:
                    distances[v] = alt

    return distances