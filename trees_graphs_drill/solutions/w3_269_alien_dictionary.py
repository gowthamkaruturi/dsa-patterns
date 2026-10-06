"""LC 269 Alien Dictionary (HARD) — Pattern: build edges from adjacent pairs, then topo sort.
https://leetcode.com/problems/alien-dictionary/
words are sorted in the alien language. Return any valid letter order containing
every letter that appears, or "" if invalid (cycle, or prefix like ["abc","ab"])."""
from collections import deque


def alien_order(words: list[str]) -> str:
    g = {c: set() for w in words for c in w}
    for a, b in zip(words, words[1:]):
        for x, y in zip(a, b):
            if x != y:
                g[x].add(y); break
        else:
            if len(a) > len(b):
                return ""
    indeg = {c: 0 for c in g}
    for u in g:
        for v in g[u]:
            indeg[v] += 1
    q = deque(c for c in g if indeg[c] == 0)
    out = []
    while q:
        u = q.popleft(); out.append(u)
        for v in g[u]:
            indeg[v] -= 1
            if indeg[v] == 0:
                q.append(v)
    return "".join(out) if len(out) == len(g) else ""
