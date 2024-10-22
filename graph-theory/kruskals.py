"""Kruskal's algorithm to find Minimum Spanning Tree of a given connected, undirected and weighted graph."""


def find_minimum_spanning_tree(edges, n):
    """Find Minimum Spanning Tree of a given connected, undirected and weighted graph."""
    parent = [i for i in range(n)]
    rank = [0] * n

    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])

        return parent[x]

    def union(u, v):
        if rank[u] > rank[v]:
            parent[v] = u
        elif rank[u] < rank[v]:
            parent[u] = v
        else:
            parent[v] = u
            rank[u] += 1

    edges.sort(key=lambda x: x[2])
    mst = []

    for u, v, _ in edges:
        x = find(u)
        y = find(v)

        if x != y:
            union(x, y)
            mst.append((u, v))

    return mst


edges = [
    [0, 1, 10],
    [0, 2, 6],
    [0, 3, 5],
    [1, 3, 15],
    [2, 3, 4],
]

print(find_minimum_spanning_tree(edges, 4))
