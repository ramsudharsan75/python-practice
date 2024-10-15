"""Djikstra's algorithm to find the shortest path in a weighted graph."""

from collections import deque
from heapq import heappop, heappush


def find_shortest_path(src, target, mat) -> list[int]:
    """Find the shortest path from src to target in a weighted graph."""
    n = len(mat)
    visited_distances = {}
    heap = [(0, src, src)]
    path = [i for i in range(n)]

    while heap:
        dist, node, parent = heappop(heap)
        path[node] = parent
        visited_distances[node] = dist

        if node == target:
            break

        for nei, wt in mat[node]:
            if nei in visited_distances:
                continue

            heappush(heap, (dist + wt, nei, node))

    res = deque([target])
    node = target

    while node != src:
        res.appendleft(path[node])
        node = path[node]

    return list(res)


adj_mat = {
    0: [(1, 0.1), (2, 0.2)],
    1: [(0, 0.1), (3, 0.3)],
    2: [(0, 0.2), (3, 0.3)],
    3: [(1, 0.3), (2, 0.3)],
}
print(find_shortest_path(0, 3, adj_mat))
