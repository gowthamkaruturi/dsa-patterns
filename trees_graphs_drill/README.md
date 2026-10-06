# Trees & Graphs: 4-week drill

26 problems, 8 templates, about 1 hour a day. Every problem has a stub in
`problems/`, a pytest suite in `tests/`, and a reference answer in
`solutions/`. Don't open `solutions/` until your tests pass or you've spent
40 minutes on a problem.

```bash
pip install pytest
python templates.py                          # self-check the 8 templates
pytest -m week1                              # run one week
pytest -k 124                                # run one problem
pytest -x                                    # stop at first failure
TARGET=solutions pytest                      # verify the reference answers (26 pass)
```

## Daily loop

1. **Warm-up (5 min):** rewrite one template from `templates.py` from memory in a scratch file.
2. **Name the pattern before writing any code.** The stub docstrings leave the pattern out on purpose. Write it as the first comment in the function, e.g. `# Kahn topo sort: edge b->a, cycle if order is short`.
3. **Solve, then run `pytest -k <LC number>`.** The edge-case tests are the traps interviewers use.
4. **Log it in the tracker.** A solve schedules a review in 3 days; passing that schedules one in 7, then 21. A failed review resets to 1 day.
5. **Review days:** delete your solution with `git checkout problems/<file>` and solve it again cold.

## Layout

| Path | What |
|---|---|
| `templates.py` | The 8 templates with self-checks |
| `ds.py` | `TreeNode`, `Node`, `build_tree([3,9,20,None,None,15,7])`, `tree_to_list`, `build_graph` |
| `problems/wN_<lc>_<name>.py` | Your stubs (start here) |
| `tests/test_weekN.py` | Tests, including edge cases you have to handle |
| `solutions/` | Reference answers, with the pattern named in each docstring |

## Weeks

| Week | Patterns | Problems |
|---|---|---|
| 1 | Tree DFS: return-upward value vs global answer | 104, 543, 110, 113, 124, 236, 297 |
| 2 | BFS levels, BST bounds, in-order | 102, 199, 98, 230, 127, 994, 1091 |
| 3 | Graph DFS, topo sort, Union-Find | 200, 133, 207, 210, 269, 684, 721 |
| 4 | Dijkstra, Bellman-Ford, MST, minimax, Tarjan | 743, 787, 1584, 778, 1192 |

LC 269 (Alien Dictionary) is a LeetCode Premium problem. The local tests cover it fully.

## You're done when

- You write all 8 templates from memory in under 15 minutes total.
- Each week's suite passes with no peeking at `solutions/`.
- You can explain why plain Dijkstra fails on 787, why 124 clamps branches at 0, and why `low[v] > disc[u]` marks a bridge in 1192.
