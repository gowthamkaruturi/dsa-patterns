"""The 8 templates. Goal: rewrite each from memory in under 2 minutes.

Drill: open a blank file, write all 8, then run `python templates.py` against
your version (copy it over this one) — the self-checks at the bottom must pass.
"""
from collections import deque, defaultdict
import heapq


# 1. Tree DFS: post-order "return info upward" (most tree problems)
def tree_height(node):
    if not node:
        return 0                                  # base case = identity value
    l, r = tree_height(node.left), tree_height(node.right)
    # combine: update a global answer here if the path can "bend" through node
    return 1 + max(l, r)                          # return what the PARENT needs


# 2. BFS level order: shortest path in unweighted graphs, tree levels
def bfs_levels(start, graph):
    q, seen, dist = deque([start]), {start}, {start: 0}
    level = 0
    while q:
        level += 1
        for _ in range(len(q)):                   # one full level per outer loop
            u = q.popleft()
            for v in graph[u]:
                if v not in seen:
                    seen.add(v)                   # mark when ENQUEUED, not when popped
                    dist[v] = level
                    q.append(v)
    return dist


# 3. Directed-graph DFS with 3 colors: cycle detection
def has_cycle(n, graph):
    state = [0] * n                               # 0=unvisited, 1=on stack, 2=done

    def dfs(u):
        state[u] = 1
        for v in graph[u]:
            if state[v] == 1:
                return True                       # back edge = cycle
            if state[v] == 0 and dfs(v):
                return True
        state[u] = 2
        return False

    return any(state[i] == 0 and dfs(i) for i in range(n))


# 4. Topological sort (Kahn's): dependency ordering
def topo(n, edges):
    g, indeg = defaultdict(list), [0] * n
    for a, b in edges:                            # a must come before b
        g[a].append(b); indeg[b] += 1
    q = deque(i for i in range(n) if indeg[i] == 0)
    order = []
    while q:
        u = q.popleft(); order.append(u)
        for v in g[u]:
            indeg[v] -= 1
            if indeg[v] == 0:
                q.append(v)
    return order if len(order) == n else []       # short = cycle


# 5. Union-Find: components, Kruskal, "are these linked?"
class DSU:
    def __init__(self, n):
        self.p, self.r = list(range(n)), [0] * n

    def find(self, x):
        while self.p[x] != x:
            self.p[x] = self.p[self.p[x]]         # path halving
            x = self.p[x]
        return x

    def union(self, a, b):
        a, b = self.find(a), self.find(b)
        if a == b:
            return False
        if self.r[a] < self.r[b]:
            a, b = b, a
        self.p[b] = a
        self.r[a] += self.r[a] == self.r[b]       # union by rank
        return True


# 6. Dijkstra: weighted shortest path, non-negative weights
def dijkstra(src, graph):                         # graph[u] = [(v, w), ...]
    dist, pq = {src: 0}, [(0, src)]
    while pq:
        d, u = heapq.heappop(pq)
        if d > dist.get(u, float("inf")):
            continue                              # stale heap entry
        for v, w in graph[u]:
            if d + w < dist.get(v, float("inf")):
                dist[v] = d + w
                heapq.heappush(pq, (d + w, v))
    return dist


# 7. BST in-order (iterative): visits keys in sorted order, can stop early
def inorder(root):
    stack, node = [], root
    while stack or node:
        while node:
            stack.append(node); node = node.left
        node = stack.pop()
        yield node.val
        node = node.right


# 8. Grid as implicit graph: no adjacency list, neighbors computed on the fly
DIRS4 = ((1, 0), (-1, 0), (0, 1), (0, -1))


def grid_neighbors(r, c, R, C):
    for dr, dc in DIRS4:
        nr, nc = r + dr, c + dc
        if 0 <= nr < R and 0 <= nc < C:
            yield nr, nc


if __name__ == "__main__":
    from ds import build_tree

    t = build_tree([4, 2, 6, 1, 3, 5, 7])
    assert tree_height(t) == 3
    assert list(inorder(t)) == [1, 2, 3, 4, 5, 6, 7]

    g = {0: [1, 2], 1: [3], 2: [3], 3: []}
    assert bfs_levels(0, g) == {0: 0, 1: 1, 2: 1, 3: 2}
    assert has_cycle(4, g) is False
    assert has_cycle(3, {0: [1], 1: [2], 2: [0]}) is True

    order = topo(4, [(0, 1), (0, 2), (1, 3), (2, 3)])
    assert order[0] == 0 and order[-1] == 3
    assert topo(2, [(0, 1), (1, 0)]) == []

    d = DSU(5)
    assert d.union(0, 1) and d.union(1, 2) and not d.union(0, 2)
    assert d.find(0) == d.find(2) != d.find(3)

    wg = {"a": [("b", 4), ("c", 1)], "c": [("b", 1)], "b": []}
    assert dijkstra("a", wg) == {"a": 0, "b": 2, "c": 1}

    assert sorted(grid_neighbors(0, 0, 3, 3)) == [(0, 1), (1, 0)]
    print("all 8 templates OK")
