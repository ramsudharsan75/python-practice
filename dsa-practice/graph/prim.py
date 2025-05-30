from heapq import heappop, heappush
from math import inf


def get_minimum_spanning_tree_distance(graph: list[tuple[int, int]]) -> int:
    """Get the minimum spanning tree of a graph using Prim's algorithm."""
    mst_dist = 0
    n = len(graph)
    visited = [False] * n
    distances = [inf] * n
    distances[0] = 0
    heap = [(0, 0)]

    while heap:
        dist, node = heappop(heap)

        if visited[node]:
            continue

        visited[node] = True
        mst_dist += dist

        for nei_dist, nei in graph[node]:
            if not visited[nei] and distances[nei] > nei_dist:
                distances[nei] = nei_dist
                heappush(heap, (nei_dist, nei))

    return mst_dist


if __name__ == "__main__":
    adj_mat = [
        [(2, 1), (3, 2)],
        [(2, 0), (3, 2), (4, 3)],
        [(3, 0), (3, 1), (1, 3)],
        [(4, 1), (1, 2)],
    ]
    print(get_minimum_spanning_tree_distance(adj_mat))  # 6
