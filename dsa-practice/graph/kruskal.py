def get_minimum_spanning_tree_distance(
    edges: list[tuple[int, int, int]], n: int
) -> int:
    """Get the minimum spanning distance of a graph using Kruskal's algorithm."""
    parent = [i for i in range(n)]
    rank = [0] * n

    def find(u: int) -> int:
        if parent[u] != u:
            parent[u] = find(parent[u])

        return parent[u]

    def union(u: int, v: int) -> None:
        if rank[u] > rank[v]:
            parent[v] = u
        elif rank[u] < rank[v]:
            parent[u] = v
        else:
            parent[v] = u
            rank[u] += 1

    edges.sort()
    mst_dist = 0

    for dist, u, v in edges:
        u_parent = find(u)
        v_parent = find(v)

        if u_parent != v_parent:
            mst_dist += dist
            union(u_parent, v_parent)

    return mst_dist


if __name__ == "__main__":
    edges_list = [
        (1, 0, 1),
        (2, 0, 2),
        (3, 1, 2),
        (4, 1, 3),
        (5, 2, 3),
    ]

    print(get_minimum_spanning_tree_distance(edges_list, 5))  # Output: 7
