"""LC 133 Clone Graph — Pattern: DFS/BFS with old->new hashmap (handles cycles).
https://leetcode.com/problems/clone-graph/
Return a deep copy: no node in the result may be an original node object."""
from ds import Node


def clone_graph(node: Node | None) -> Node | None:
    if not node:
        return None
    copies = {node: Node(node.val)}
    stack = [node]
    while stack:
        u = stack.pop()
        for v in u.neighbors:
            if v not in copies:
                copies[v] = Node(v.val); stack.append(v)
            copies[u].neighbors.append(copies[v])
    return copies[node]
