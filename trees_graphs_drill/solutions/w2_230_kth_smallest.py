"""LC 230 Kth Smallest Element in a BST — Pattern: iterative in-order (sorted order).
https://leetcode.com/problems/kth-smallest-element-in-a-bst/
k is 1-indexed. Stop early — don't build the full list."""
from ds import TreeNode


def kth_smallest(root: TreeNode, k: int) -> int:
    stack, n = [], root
    while stack or n:
        while n:
            stack.append(n); n = n.left
        n = stack.pop()
        k -= 1
        if k == 0:
            return n.val
        n = n.right
    raise ValueError("k out of range")
