from heapq import heappop, heappush
from math import inf


def shortest_path_from_source_to_all_nodes(graph: list[list[tuple[int, int]]], source: int):
    n = len(graph)
    distances = [inf] * n
    distances[source] = 0
    visited = [False] * n
    heap = [(0, source)]

    while heap:
        curr_dist, node = heappop(heap)

        if visited[node]:
            continue

        visited[node] = True

        for nei, nei_dist in graph[node]:
            if not visited[nei] and (new_dist := curr_dist + nei_dist) < distances[nei]:
                distances[nei] = new_dist
                heappush(heap, (new_dist, nei))
    
    return distances

if __name__ == "__main__":
    adj_mat = [
        [(1, 1), (2, 4)],
        [(0, 1), (2, 2), (3, 5)],
        [(0, 4), (1, 2), (3, 1)],
        [(1, 5), (2, 1)]
    ]
    print(shortest_path_from_source_to_all_nodes(adj_mat, 0))  # Output: [0, 1, 3, 4]
    print(shortest_path_from_source_to_all_nodes(adj_mat, 1))  # Output: [1, 0, 2, 3]
    print(shortest_path_from_source_to_all_nodes(adj_mat, 2))  # Output: [3, 2, 0, 1]
    print(shortest_path_from_source_to_all_nodes(adj_mat, 3))  # Output: [4, 5, 1, 1]