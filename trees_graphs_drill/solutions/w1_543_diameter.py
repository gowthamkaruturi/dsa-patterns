"""LC 543 Diameter of Binary Tree — Pattern: tree DFS, return height / update global.
https://leetcode.com/problems/diameter-of-binary-tree/
Return the number of EDGES on the longest path between any two nodes."""
from ds import TreeNode


def diameter(root: TreeNode | None) -> int:
    best = 0

    def h(n):
        nonlocal best
        if not n:
            return 0
        l, r = h(n.left), h(n.right)
        best = max(best, l + r)          # path bends through n
        return 1 + max(l, r)             # parent can only extend one side

    h(root)
    return best
