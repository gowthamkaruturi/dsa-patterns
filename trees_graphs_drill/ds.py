"""Shared data structures + builders so tests can use LeetCode-style inputs."""
from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val, self.left, self.right = val, left, right

    def __repr__(self):
        return f"TreeNode({self.val})"


def build_tree(values: list) -> Optional[TreeNode]:
    """LeetCode level-order list -> tree. [3,9,20,None,None,15,7]"""
    if not values or values[0] is None:
        return None
    root = TreeNode(values[0])
    q, i = deque([root]), 1
    while q and i < len(values):
        node = q.popleft()
        if i < len(values) and values[i] is not None:
            node.left = TreeNode(values[i]); q.append(node.left)
        i += 1
        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i]); q.append(node.right)
        i += 1
    return root


def tree_to_list(root: Optional[TreeNode]) -> list:
    """Tree -> LeetCode level-order list (trailing Nones trimmed)."""
    out, q = [], deque([root])
    while q:
        node = q.popleft()
        if node:
            out.append(node.val); q.append(node.left); q.append(node.right)
        else:
            out.append(None)
    while out and out[-1] is None:
        out.pop()
    return out


def find_node(root: Optional[TreeNode], val) -> Optional[TreeNode]:
    if not root:
        return None
    if root.val == val:
        return root
    return find_node(root.left, val) or find_node(root.right, val)


class Node:
    """Graph node for Clone Graph (LC 133)."""
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


def build_graph(adj: list) -> Optional[Node]:
    """1-indexed adjacency list -> node 1. [[2,4],[1,3],[2,4],[1,3]]"""
    if not adj:
        return None
    nodes = [Node(i + 1) for i in range(len(adj))]
    for i, nbrs in enumerate(adj):
        nodes[i].neighbors = [nodes[j - 1] for j in nbrs]
    return nodes[0]


def graph_to_adj(node: Optional[Node]) -> tuple[list, set]:
    """node -> (1-indexed adjacency list, set of object ids seen)."""
    if not node:
        return [], set()
    seen, q = {node.val: node}, deque([node])
    while q:
        u = q.popleft()
        for v in u.neighbors:
            if v.val not in seen:
                seen[v.val] = v; q.append(v)
    adj = [[v.val for v in seen[i].neighbors] for i in range(1, len(seen) + 1)]
    return adj, {id(n) for n in seen.values()}
