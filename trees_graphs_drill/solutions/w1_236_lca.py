"""LC 236 Lowest Common Ancestor of a Binary Tree — Pattern: tree DFS, bubble found nodes up.
https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/
p and q are guaranteed to exist in the tree. Return the LCA node."""
from ds import TreeNode


def lca(root: TreeNode | None, p: TreeNode, q: TreeNode) -> TreeNode | None:
    if not root or root is p or root is q:
        return root
    l, r = lca(root.left, p, q), lca(root.right, p, q)
    if l and r:
        return root
    return l or r
