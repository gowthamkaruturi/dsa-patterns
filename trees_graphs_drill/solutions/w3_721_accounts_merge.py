"""LC 721 Accounts Merge — Pattern: Union-Find over emails (entity resolution).
https://leetcode.com/problems/accounts-merge/
Return [name, *sorted emails] per merged account, in any account order."""
from collections import defaultdict


def accounts_merge(accounts: list[list[str]]) -> list[list[str]]:
    parent, owner = {}, {}

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]; x = parent[x]
        return x

    for name, *emails in accounts:
        for e in emails:
            parent.setdefault(e, e); owner[e] = name
        for e in emails[1:]:
            parent[find(e)] = find(emails[0])
    groups = defaultdict(list)
    for e in parent:
        groups[find(e)].append(e)
    return [[owner[root]] + sorted(es) for root, es in groups.items()]
