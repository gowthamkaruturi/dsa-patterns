"""LC 994 Rotting Oranges — Pattern: multi-source BFS on a grid.
https://leetcode.com/problems/rotting-oranges/
0 empty, 1 fresh, 2 rotten. Minutes until no fresh remain, or -1."""
from collections import deque


def oranges_rotting(grid: list[list[int]]) -> int:
    R, C = len(grid), len(grid[0])
    q, fresh = deque(), 0
    for r in range(R):
        for c in range(C):
            if grid[r][c] == 2: q.append((r, c))
            elif grid[r][c] == 1: fresh += 1
    g = [row[:] for row in grid]
    minutes = 0
    while q and fresh:
        for _ in range(len(q)):
            r, c = q.popleft()
            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nr, nc = r + dr, c + dc
                if 0 <= nr < R and 0 <= nc < C and g[nr][nc] == 1:
                    g[nr][nc] = 2; fresh -= 1; q.append((nr, nc))
        minutes += 1
    return -1 if fresh else minutes
