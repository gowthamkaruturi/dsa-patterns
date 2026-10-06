"""LC 297 Serialize and Deserialize Binary Tree (HARD) — Pattern: pre-order DFS with null markers.
https://leetcode.com/problems/serialize-and-deserialize-binary-tree/
Any string format works as long as deserialize(serialize(t)) rebuilds t exactly."""
from ds import TreeNode


def serialize(root: TreeNode | None) -> str:
    out = []

    def dfs(n):
        if not n:
            out.append("#"); return
        out.append(str(n.val)); dfs(n.left); dfs(n.right)

    dfs(root)
    return ",".join(out)


def deserialize(data: str) -> TreeNode | None:
    it = iter(data.split(","))

    def build():
        v = next(it)
        if v == "#":
            return None
        n = TreeNode(int(v))
        n.left, n.right = build(), build()
        return n

    return build()
