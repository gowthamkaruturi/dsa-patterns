from conftest import load
from ds import build_graph, graph_to_adj


def test_200_num_islands():
    f = load("w3_200_num_islands").num_islands
    g = [["1", "1", "0", "0", "0"], ["1", "1", "0", "0", "0"], ["0", "0", "1", "0", "0"], ["0", "0", "0", "1", "1"]]
    snapshot = [r[:] for r in g]
    assert f(g) == 3
    assert g == snapshot, "don't mutate the input"
    assert f([["1", "1", "1"], ["0", "1", "0"], ["1", "1", "1"]]) == 1
    assert f([["0"]]) == 0


def test_133_clone_graph():
    f = load("w3_133_clone_graph").clone_graph
    adj = [[2, 4], [1, 3], [2, 4], [1, 3]]
    orig = build_graph(adj)
    _, orig_ids = graph_to_adj(orig)
    copy = f(orig)
    copy_adj, copy_ids = graph_to_adj(copy)
    assert copy_adj == adj
    assert not (orig_ids & copy_ids), "clone must not reuse original nodes"
    assert f(None) is None
    assert graph_to_adj(f(build_graph([[]])))[0] == [[]]


def _valid_order(n, prereqs, order):
    pos = {c: i for i, c in enumerate(order)}
    return sorted(order) == list(range(n)) and all(pos[b] < pos[a] for a, b in prereqs)


def test_207_course_schedule():
    f = load("w3_207_course_schedule").can_finish
    assert f(2, [[1, 0]]) is True
    assert f(2, [[1, 0], [0, 1]]) is False
    assert f(5, [[1, 4], [2, 4], [3, 1], [3, 2]]) is True
    assert f(3, [[0, 1], [1, 2], [2, 0]]) is False
    assert f(1, []) is True


def test_210_course_schedule_ii():
    f = load("w3_210_course_schedule_ii").find_order
    for n, pre in ((2, [[1, 0]]), (4, [[1, 0], [2, 0], [3, 1], [3, 2]]), (1, []), (3, [])):
        assert _valid_order(n, pre, f(n, pre))
    assert f(2, [[1, 0], [0, 1]]) == []


def _valid_alien(words, order):
    if sorted(order) != sorted(set("".join(words))):
        return False
    rank = {c: i for i, c in enumerate(order)}
    key = lambda w: [rank[c] for c in w]
    return all(key(a) <= key(b) for a, b in zip(words, words[1:]))


def test_269_alien_dictionary():
    f = load("w3_269_alien_dictionary").alien_order
    for words in (["wrt", "wrf", "er", "ett", "rftt"], ["z", "x"], ["z", "z"], ["ab", "adc"]):
        assert _valid_alien(words, f(words)), words
    assert f(["z", "x", "z"]) == ""          # cycle
    assert f(["abc", "ab"]) == ""            # prefix after longer word


def test_684_redundant_connection():
    f = load("w3_684_redundant_connection").find_redundant_connection
    assert f([[1, 2], [1, 3], [2, 3]]) == [2, 3]
    assert f([[1, 2], [2, 3], [3, 4], [1, 4], [1, 5]]) == [1, 4]


def test_721_accounts_merge():
    f = load("w3_721_accounts_merge").accounts_merge
    accounts = [
        ["John", "johnsmith@mail.com", "john_newyork@mail.com"],
        ["John", "johnsmith@mail.com", "john00@mail.com"],
        ["Mary", "mary@mail.com"],
        ["John", "johnnybravo@mail.com"],
    ]
    expected = [
        ["John", "john00@mail.com", "john_newyork@mail.com", "johnsmith@mail.com"],
        ["Mary", "mary@mail.com"],
        ["John", "johnnybravo@mail.com"],
    ]
    assert sorted(f(accounts)) == sorted(expected)
    # transitive link: A-B in one account, B-C in another, C-D in a third
    chain = [["Al", "a", "b"], ["Al", "c", "d"], ["Al", "b", "c"]]
    assert f(chain) == [["Al", "a", "b", "c", "d"]]
