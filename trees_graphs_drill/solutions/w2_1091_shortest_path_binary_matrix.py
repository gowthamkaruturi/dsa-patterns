"""LC 1091 Shortest Path in Binary Matrix — Pattern: BFS on grid, 8 directions.
https://leetcode.com/problems/shortest-path-in-binary-matrix/
Path of 0-cells from top-left to bottom-right; return number of CELLS, or -1."""
from collections import deque


def shortest_path_binary_matrix(grid: list[list[int]]) -> int:
    n = len(grid)
    if grid[0][0] or grid[n - 1][n - 1]:
        return -1
    q, seen = deque([(0, 0, 1)]), {(0, 0)}
    while q:
        r, c, d = q.popleft()
        if (r, c) == (n - 1, n - 1):
            return d
        for dr in (-1, 0, 1):
            for dc in (-1, 0, 1):
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < n and not grid[nr][nc] and (nr, nc) not in seen:
                    seen.add((nr, nc)); q.append((nr, nc, d + 1))
    return -1
