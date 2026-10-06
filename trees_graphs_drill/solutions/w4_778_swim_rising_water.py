"""LC 778 Swim in Rising Water (HARD) — Pattern: Dijkstra minimizing the MAX on the path (minimax).
https://leetcode.com/problems/swim-in-rising-water/
Return the least time t to go from (0,0) to (n-1,n-1)."""
import heapq


def swim_in_water(grid: list[list[int]]) -> int:
    n = len(grid)
    pq, seen = [(grid[0][0], 0, 0)], {(0, 0)}
    while pq:
        t, r, c = heapq.heappop(pq)
        if (r, c) == (n - 1, n - 1):
            return t
        for nr, nc in ((r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)):
            if 0 <= nr < n and 0 <= nc < n and (nr, nc) not in seen:
                seen.add((nr, nc))
                heapq.heappush(pq, (max(t, grid[nr][nc]), nr, nc))
    return -1
