"""Prim's algorithm to find the minimum spanning tree of a graph."""

from heapq import heappop, heappush
from math import inf


def find_minimum_spanning_tree(adj_mat) -> list[int]:
    """Find the minimum spanning tree using Prim's algorithm."""
    visited = set()
    n = len(adj_mat)
    distance = [inf] * n
    parent = [i for i in range(n)]
    heap = [(0, 0, 0)]

    while heap:
        dist, node, dad = heappop(heap)
        visited.add(node)
        distance[node] = dist
        parent[node] = dad

        for nei, wt in adj_mat[node]:
            if nei in visited:
                continue

            heappush(heap, (wt, nei, node))

    return parent


adj_mat = {
    0: [(1, 0.1), (2, 0.2)],
    1: [(0, 0.1), (3, 0.3)],
    2: [(0, 0.2), (3, 0.3)],
    3: [(1, 0.3), (2, 0.3)],
}
print(find_minimum_spanning_tree(adj_mat))
