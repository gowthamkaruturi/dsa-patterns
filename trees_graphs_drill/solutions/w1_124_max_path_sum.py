"""LC 124 Binary Tree Maximum Path Sum (HARD) — Pattern: return-upward vs global answer.
https://leetcode.com/problems/binary-tree-maximum-path-sum/
Path = any node-to-node sequence (non-empty). Values may be negative."""
from ds import TreeNode


def max_path_sum(root: TreeNode) -> int:
    best = float("-inf")

    def gain(n):
        nonlocal best
        if not n:
            return 0
        l = max(gain(n.left), 0)         # drop negative branches
        r = max(gain(n.right), 0)
        best = max(best, n.val + l + r)
        return n.val + max(l, r)

    gain(root)
    return best
