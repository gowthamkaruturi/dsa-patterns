"""LC 210 Course Schedule II — Pattern: topological sort (Kahn's algorithm).
https://leetcode.com/problems/course-schedule-ii/
Return ANY valid order of all n courses, or [] if impossible."""
from collections import deque


def find_order(n: int, prereqs: list[list[int]]) -> list[int]:
    g, indeg = [[] for _ in range(n)], [0] * n
    for a, b in prereqs:
        g[b].append(a); indeg[a] += 1
    q = deque(i for i in range(n) if indeg[i] == 0)
    order = []
    while q:
        u = q.popleft(); order.append(u)
        for v in g[u]:
            indeg[v] -= 1
            if indeg[v] == 0:
                q.append(v)
    return order if len(order) == n else []
