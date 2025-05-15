from matplotlib import pyplot as plt
import time
from DenseGraph import DenseGraph
from SparseGraph import SparseGraph
from CyclicGraph import CyclicGraph
from DFS import dfs
from BFS import bfs
from FloydWarshall import floyd_warshall
from Dijkstra import dijkstra
from Kurskal import kruskal_algorithm, extract_edges_from_adj_matrix
from Prim import prim_algorithm


def time_algorithm(algorithm, graph):
    start = time.perf_counter()
    algorithm(graph)
    end = time.perf_counter()
    return end - start


def test_graph_performance(graph_class, sizes):
    dfs_times = []
    bfs_times = []

    for size in sizes:
        graph = graph_class(size)
        dfs_time = time_algorithm(dfs, graph.get_adj_matrix())
        bfs_time = time_algorithm(bfs, graph.get_adj_list())

        dfs_times.append(dfs_time)
        bfs_times.append(bfs_time)

        print(f"{label} | Size: {size} | DFS: {dfs_time:.6f}s | BFS: {bfs_time:.6f}s")

    return dfs_times, bfs_times

# ----------- Sizes to Test and Plotting -----------

def plot_graph_times(sizes, dfs_times, bfs_times, title):
    plt.figure(figsize=(10, 6))
    plt.plot(sizes, dfs_times, label="DFS", marker='o', color='blue')
    plt.plot(sizes, bfs_times, label="BFS", marker='x', color='green')
    plt.title(f"{title} Graph - DFS vs BFS Execution Time")
    plt.xlabel("Number of Vertices")
    plt.ylabel("Time (seconds)")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()


sizes = [10, 50, 100, 200, 300, 500]

# Test each graph type
graph_types = [
    (SparseGraph, "Sparse"),
    (DenseGraph, "Dense"),
    (CyclicGraph, "Cyclic")
]

def plot_combined_graphs(sizes, all_times):
    plt.figure(figsize=(12, 8))

    for label, dfs_times, bfs_times in all_times:
        plt.plot(sizes, dfs_times, label=f"{label} DFS", linestyle='-', marker='o')
        plt.plot(sizes, bfs_times, label=f"{label} BFS", linestyle='--', marker='x')

    plt.title("DFS vs BFS Execution Time Across Graph Types")
    plt.xlabel("Number of Vertices")
    plt.ylabel("Time (seconds)")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

# ----------- Collect All Timings and Plot Summary -----------

all_results = []

for graph_class, label in graph_types:
    dfs_times, bfs_times = test_graph_performance(graph_class, sizes)
    plot_graph_times(sizes, dfs_times, bfs_times, label)
    all_results.append((label, dfs_times, bfs_times))

# Final Combined Plot
plot_combined_graphs(sizes, all_results)



def test_floyd_warshall_performance(graph_class, sizes, label):
    fw_times = []

    for size in sizes:
        graph = graph_class(size)
        matrix = graph.get_adj_matrix()
        # Deep copy of the matrix to avoid modifying the original
        matrix_copy = [row[:] for row in matrix]

        start = time.perf_counter()
        floyd_warshall(matrix_copy)
        end = time.perf_counter()
        elapsed = end - start
        fw_times.append(elapsed)

        print(f"{label} | Size: {size} | Floyd-Warshall: {elapsed:.6f}s")

    return fw_times


def test_dijkstra_performance(graph_class, sizes, label):
    dijkstra_times = []

    for size in sizes:
        graph = graph_class(size)
        start = time.perf_counter()
        dijkstra(graph.get_adj_matrix(), 0)
        end = time.perf_counter()
        elapsed = end - start
        dijkstra_times.append(elapsed)
        print(f"{label} | Size: {size} | Dijkstra: {elapsed:.6f}s")

    return dijkstra_times

def plot_fw_vs_dijkstra(sizes, fw_times, dijkstra_times, label):
    plt.figure(figsize=(10, 6))
    plt.plot(sizes, fw_times, label="Floyd-Warshall", marker='o', color='red')
    plt.plot(sizes, dijkstra_times, label="Dijkstra", marker='x', color='purple')
    plt.title(f"{label} Graph - Floyd-Warshall vs Dijkstra Execution Time")
    plt.xlabel("Number of Vertices")
    plt.ylabel("Time (seconds)")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()


combined_results = []

for graph_class, label in graph_types:
    fw_times = test_floyd_warshall_performance(graph_class, sizes, label)
    dijkstra_times = test_dijkstra_performance(graph_class, sizes, label)
    plot_fw_vs_dijkstra(sizes, fw_times, dijkstra_times, label)

    combined_results.append((label, fw_times, dijkstra_times))


def plot_all_algorithms_comparison(sizes, combined_results):
    plt.figure(figsize=(12, 8))
    for label, fw_times, dijkstra_times in combined_results:
        plt.plot(sizes, fw_times, label=f"{label} Floyd-Warshall", linestyle='-', marker='o')
        plt.plot(sizes, dijkstra_times, label=f"{label} Dijkstra", linestyle='--', marker='x')

    plt.title("Floyd-Warshall vs Dijkstra - All Graph Types")
    plt.xlabel("Number of Vertices")
    plt.ylabel("Time (seconds)")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

# plot_all_algorithms_comparison(sizes, combined_results)


def test_kruskal_performance(graph_class, sizes, label):
    times = []
    for size in sizes:
        graph = graph_class(size)
        edges = extract_edges_from_adj_matrix(graph.get_adj_matrix())
        start = time.perf_counter()
        kruskal_algorithm(size, edges)
        end = time.perf_counter()
        elapsed = end - start
        times.append(elapsed)
        print(f"{label} | Size: {size} | Kruskal: {elapsed:.6f}s")
    return times

def test_prim_performance(graph_class, sizes, label):
    times = []
    for size in sizes:
        graph = graph_class(size)
        matrix = graph.get_adj_matrix()
        start = time.perf_counter()
        prim_algorithm(matrix)
        end = time.perf_counter()
        elapsed = end - start
        times.append(elapsed)
        print(f"{label} | Size: {size} | Prim: {elapsed:.6f}s")
    return times

def plot_prim_vs_kruskal(sizes, prim_times, kruskal_times, label):
    plt.figure(figsize=(10, 6))
    plt.plot(sizes, prim_times, label="Prim's Algorithm", marker='o', color='orange')
    plt.plot(sizes, kruskal_times, label="Kruskal's Algorithm", marker='x', color='brown')
    plt.title(f"{label} Graph - Prim vs Kruskal Execution Time")
    plt.xlabel("Number of Vertices")
    plt.ylabel("Time (seconds)")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()


prim_kruskal_results = []

for graph_class, label in graph_types:
    prim_times = test_prim_performance(graph_class, sizes, label)
    kruskal_times = test_kruskal_performance(graph_class, sizes, label)
    plot_prim_vs_kruskal(sizes, prim_times, kruskal_times, label)
    prim_kruskal_results.append((label, prim_times, kruskal_times))

def plot_all_mst_algorithms_comparison(sizes, results):
    plt.figure(figsize=(12, 8))
    for label, prim_times, kruskal_times in results:
        plt.plot(sizes, prim_times, label=f"{label} Prim", linestyle='-', marker='o')
        plt.plot(sizes, kruskal_times, label=f"{label} Kruskal", linestyle='--', marker='x')

    plt.title("Prim vs Kruskal - All Graph Types")
    plt.xlabel("Number of Vertices")
    plt.ylabel("Time (seconds)")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

plot_all_mst_algorithms_comparison(sizes, prim_kruskal_results)
