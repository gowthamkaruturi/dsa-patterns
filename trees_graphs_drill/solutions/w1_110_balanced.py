"""LC 110 Balanced Binary Tree — Pattern: tree DFS with sentinel (-1 = unbalanced).
https://leetcode.com/problems/balanced-binary-tree/
Balanced = every node's subtrees differ in height by at most 1. Aim for O(n)."""
from ds import TreeNode


def is_balanced(root: TreeNode | None) -> bool:
    def h(n):
        if not n:
            return 0
        l = h(n.left)
        if l < 0:
            return -1
        r = h(n.right)
        if r < 0 or abs(l - r) > 1:
            return -1
        return 1 + max(l, r)

    return h(root) >= 0
