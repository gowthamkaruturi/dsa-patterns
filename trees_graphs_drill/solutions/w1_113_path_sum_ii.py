"""LC 113 Path Sum II — Pattern: tree DFS + backtracking (pre-order, push/pop path).
https://leetcode.com/problems/path-sum-ii/
Return every root-to-LEAF path whose values sum to target, left-to-right order."""
from ds import TreeNode


def path_sum(root: TreeNode | None, target: int) -> list[list[int]]:
    out, path = [], []

    def dfs(n, remaining):
        if not n:
            return
        path.append(n.val)
        remaining -= n.val
        if not n.left and not n.right and remaining == 0:
            out.append(path[:])
        dfs(n.left, remaining)
        dfs(n.right, remaining)
        path.pop()

    dfs(root, target)
    return out
