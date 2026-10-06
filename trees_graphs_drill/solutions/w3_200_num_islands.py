"""LC 200 Number of Islands — Pattern: grid DFS/BFS flood fill (connected components).
https://leetcode.com/problems/number-of-islands/
grid cells are "1" (land) / "0" (water). Don't assume you may mutate the input."""


def num_islands(grid: list[list[str]]) -> int:
    if not grid:
        return 0
    R, C = len(grid), len(grid[0])
    seen, count = set(), 0
    for r in range(R):
        for c in range(C):
            if grid[r][c] == "1" and (r, c) not in seen:
                count += 1
                stack = [(r, c)]; seen.add((r, c))
                while stack:
                    y, x = stack.pop()
                    for ny, nx in ((y + 1, x), (y - 1, x), (y, x + 1), (y, x - 1)):
                        if 0 <= ny < R and 0 <= nx < C and grid[ny][nx] == "1" and (ny, nx) not in seen:
                            seen.add((ny, nx)); stack.append((ny, nx))
    return count
