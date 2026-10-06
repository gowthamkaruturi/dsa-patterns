from conftest import load
from ds import build_tree, tree_to_list, find_node


def test_104_max_depth():
    f = load("w1_104_max_depth").max_depth
    assert f(build_tree([3, 9, 20, None, None, 15, 7])) == 3
    assert f(build_tree([1, None, 2])) == 2
    assert f(None) == 0


def test_543_diameter():
    f = load("w1_543_diameter").diameter
    assert f(build_tree([1, 2, 3, 4, 5])) == 3
    assert f(build_tree([1, 2])) == 1
    # longest path does NOT pass through the root
    assert f(build_tree([1, 2, None, 3, 4, 5, None, None, 6, 7, None, None, 8])) == 6


def test_110_balanced():
    f = load("w1_110_balanced").is_balanced
    assert f(build_tree([3, 9, 20, None, None, 15, 7])) is True
    assert f(build_tree([1, 2, 2, 3, 3, None, None, 4, 4])) is False
    assert f(None) is True
    # root looks balanced, subtree isn't
    assert f(build_tree([1, 2, 2, 3, None, None, 3, 4, None, None, 4])) is False


def test_113_path_sum_ii():
    f = load("w1_113_path_sum_ii").path_sum
    t = build_tree([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, 5, 1])
    assert f(t, 22) == [[5, 4, 11, 2], [5, 8, 4, 5]]
    assert f(build_tree([1, 2, 3]), 5) == []
    assert f(build_tree([1, 2]), 1) == []          # root alone is not a leaf
    assert f(build_tree([-2, None, -3]), -5) == [[-2, -3]]


def test_124_max_path_sum():
    f = load("w1_124_max_path_sum").max_path_sum
    assert f(build_tree([1, 2, 3])) == 6
    assert f(build_tree([-10, 9, 20, None, None, 15, 7])) == 42
    assert f(build_tree([-3])) == -3
    assert f(build_tree([2, -1])) == 2


def test_236_lca():
    f = load("w1_236_lca").lca
    t = build_tree([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4])
    assert f(t, find_node(t, 5), find_node(t, 1)).val == 3
    assert f(t, find_node(t, 5), find_node(t, 4)).val == 5
    assert f(t, find_node(t, 7), find_node(t, 6)).val == 5


def test_297_serialize():
    m = load("w1_297_serialize")
    for vals in ([1, 2, 3, None, None, 4, 5], [], [1], [-1, None, -2, None, -3], [10, 200, 3000]):
        s = m.serialize(build_tree(vals))
        assert isinstance(s, str)
        assert tree_to_list(m.deserialize(s)) == vals
