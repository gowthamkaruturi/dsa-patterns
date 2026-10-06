"""LC 787 Cheapest Flights Within K Stops — Pattern: Bellman-Ford limited to k+1 rounds
(or BFS by levels). Plain Dijkstra is WRONG here — figure out why.
https://leetcode.com/problems/cheapest-flights-within-k-stops/
Return cheapest price src->dst with at most k stops, or -1."""


def find_cheapest_price(n: int, flights: list[list[int]], src: int, dst: int, k: int) -> int:
    INF = float("inf")
    cost = [INF] * n
    cost[src] = 0
    for _ in range(k + 1):
        nxt = cost[:]                       # relax from the PREVIOUS round only
        for u, v, w in flights:
            if cost[u] + w < nxt[v]:
                nxt[v] = cost[u] + w
        cost = nxt
    return -1 if cost[dst] == INF else cost[dst]
