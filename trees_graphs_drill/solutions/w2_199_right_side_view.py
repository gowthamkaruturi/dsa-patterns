"""LC 199 Binary Tree Right Side View — Pattern: BFS level order, keep last per level.
https://leetcode.com/problems/binary-tree-right-side-view/"""
from collections import deque
from ds import TreeNode


def right_side_view(root: TreeNode | None) -> list[int]:
    if not root:
        return []
    out, q = [], deque([root])
    while q:
        for i in range(len(q)):
            n = q.popleft()
            if i == 0:
                out.append(n.val)        # enqueue right first, so index 0 is rightmost
            if n.right: q.append(n.right)
            if n.left: q.append(n.left)
    return out
