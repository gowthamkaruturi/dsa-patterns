"""LC 102 Binary Tree Level Order Traversal — Pattern: BFS, one level per outer loop.
https://leetcode.com/problems/binary-tree-level-order-traversal/"""
from collections import deque
from ds import TreeNode


def level_order(root: TreeNode | None) -> list[list[int]]:
    if not root:
        return []
    out, q = [], deque([root])
    while q:
        level = []
        for _ in range(len(q)):
            n = q.popleft()
            level.append(n.val)
            if n.left: q.append(n.left)
            if n.right: q.append(n.right)
        out.append(level)
    return out
