"""LC 207 Course Schedule — Pattern: cycle detection in directed graph (3-color DFS or Kahn).
https://leetcode.com/problems/course-schedule/
prereqs[i] = [a, b] means take b before a. Can you finish all n courses?"""
from collections import deque


def can_finish(n: int, prereqs: list[list[int]]) -> bool:
    g, indeg = [[] for _ in range(n)], [0] * n
    for a, b in prereqs:
        g[b].append(a); indeg[a] += 1
    q = deque(i for i in range(n) if indeg[i] == 0)
    done = 0
    while q:
        u = q.popleft(); done += 1
        for v in g[u]:
            indeg[v] -= 1
            if indeg[v] == 0:
                q.append(v)
    return done == n
