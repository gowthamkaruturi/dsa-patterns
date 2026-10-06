"""LC 104 Maximum Depth of Binary Tree — Pattern: tree DFS (post-order).
https://leetcode.com/problems/maximum-depth-of-binary-tree/
Return the number of nodes on the longest root-to-leaf path."""
from ds import TreeNode


def max_depth(root: TreeNode | None) -> int:
    if not root:
        return 0
    return 1 + max(max_depth(root.left), max_depth(root.right))
