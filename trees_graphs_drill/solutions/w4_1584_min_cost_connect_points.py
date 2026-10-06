"""LC 1584 Min Cost to Connect All Points — Pattern: MST (Prim's on a dense graph, or Kruskal + DSU).
https://leetcode.com/problems/min-cost-to-connect-all-points/
Edge weight = Manhattan distance."""


def min_cost_connect_points(points: list[list[int]]) -> int:
    n = len(points)
    in_tree, best, total = [False] * n, [float("inf")] * n, 0
    best[0] = 0
    for _ in range(n):                       # O(n^2) Prim: optimal for complete graphs
        u = min((i for i in range(n) if not in_tree[i]), key=best.__getitem__)
        in_tree[u] = True; total += best[u]
        x, y = points[u]
        for v in range(n):
            if not in_tree[v]:
                d = abs(x - points[v][0]) + abs(y - points[v][1])
                if d < best[v]:
                    best[v] = d
    return total
