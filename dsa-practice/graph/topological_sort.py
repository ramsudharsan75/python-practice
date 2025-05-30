from collections import deque


def topo_sort_using_dfs_in_reverse(graph: list[int, int], n: int):
    """Do topological sort using DFS"""
    visited = set()
    res = []

    def dfs(node: int):
        visited.add(node)

        for nei in graph[node]:
            if nei not in visited:
                dfs(nei)

        res.append(node)

    for i in range(n):
        if i not in visited:
            dfs(i)

    return res[::-1]


def topo_sort_using_kahn_indegree(graph: dict[int, list[int]], n: int):
    """Do topological sort using Kahn's algorithm"""
    indegrees = [0] * n

    q = set(i for i in range(n))
    res = []

    for neis in graph.values():
        for nei in neis:
            indegrees[nei] += 1
            q.discard(nei)

    q = deque(q)

    while q:
        node = q.popleft()
        res.append(node)

        for nei in graph[node]:
            indegrees[nei] -= 1

            if indegrees[nei] == 0:
                q.append(nei)

    return res


if __name__ == "__main__":
    adj_list = {0: [1, 2], 1: [2], 2: [3], 3: [4], 4: []}
    print(topo_sort_using_dfs_in_reverse(adj_list, 5))  # Output: [0, 1, 2, 3, 4]
    print(topo_sort_using_kahn_indegree(adj_list, 5))  # Output: [0, 1, 2, 3, 4]
