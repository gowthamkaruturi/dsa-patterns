"""LC 743 Network Delay Time — Pattern: Dijkstra.
https://leetcode.com/problems/network-delay-time/
times[i] = (u, v, w), nodes 1..n, signal from k. Time for ALL nodes to receive it, or -1."""
import heapq
from collections import defaultdict


def network_delay_time(times: list[list[int]], n: int, k: int) -> int:
    g = defaultdict(list)
    for u, v, w in times:
        g[u].append((v, w))
    dist, pq = {}, [(0, k)]
    while pq:
        d, u = heapq.heappop(pq)
        if u in dist:
            continue
        dist[u] = d
        for v, w in g[u]:
            if v not in dist:
                heapq.heappush(pq, (d + w, v))
    return max(dist.values()) if len(dist) == n else -1
