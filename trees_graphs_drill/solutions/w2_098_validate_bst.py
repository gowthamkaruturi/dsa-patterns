"""LC 98 Validate Binary Search Tree — Pattern: DFS with (low, high) bounds, or in-order.
https://leetcode.com/problems/validate-binary-search-tree/
Strict: left < node < right for the WHOLE subtree, not just direct children."""
from ds import TreeNode


def is_valid_bst(root: TreeNode | None) -> bool:
    def ok(n, lo, hi):
        if not n:
            return True
        if not (lo < n.val < hi):
            return False
        return ok(n.left, lo, n.val) and ok(n.right, n.val, hi)

    return ok(root, float("-inf"), float("inf"))
