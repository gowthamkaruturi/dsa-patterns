"""LC 684 Redundant Connection — Pattern: Union-Find; first edge joining an existing set.
https://leetcode.com/problems/redundant-connection/
Nodes are 1..n. If several answers, return the one that appears LAST in edges."""


def find_redundant_connection(edges: list[list[int]]) -> list[int]:
    parent = list(range(len(edges) + 1))

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]; x = parent[x]
        return x

    for a, b in edges:
        ra, rb = find(a), find(b)
        if ra == rb:
            return [a, b]
        parent[ra] = rb
    return []
