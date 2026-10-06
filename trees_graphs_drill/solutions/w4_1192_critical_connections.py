"""LC 1192 Critical Connections in a Network (HARD) — Pattern: Tarjan's bridges (discovery time + low-link).
https://leetcode.com/problems/critical-connections-in-a-network/
Undirected, nodes 0..n-1. Return all bridges in any order."""
import sys


def critical_connections(n: int, connections: list[list[int]]) -> list[list[int]]:
    sys.setrecursionlimit(max(10_000, 4 * n))
    g = [[] for _ in range(n)]
    for a, b in connections:
        g[a].append(b); g[b].append(a)
    disc, low, out, t = [-1] * n, [0] * n, [], [0]

    def dfs(u, parent):
        disc[u] = low[u] = t[0]; t[0] += 1
        for v in g[u]:
            if v == parent:
                continue
            if disc[v] == -1:
                dfs(v, u)
                low[u] = min(low[u], low[v])
                if low[v] > disc[u]:          # v's subtree can't reach u or above
                    out.append([u, v])
            else:
                low[u] = min(low[u], disc[v])

    for i in range(n):
        if disc[i] == -1:
            dfs(i, -1)
    return out
