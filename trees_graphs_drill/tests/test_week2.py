from conftest import load
from ds import build_tree


def test_102_level_order():
    f = load("w2_102_level_order").level_order
    assert f(build_tree([3, 9, 20, None, None, 15, 7])) == [[3], [9, 20], [15, 7]]
    assert f(build_tree([1])) == [[1]]
    assert f(None) == []


def test_199_right_side_view():
    f = load("w2_199_right_side_view").right_side_view
    assert f(build_tree([1, 2, 3, None, 5, None, 4])) == [1, 3, 4]
    assert f(build_tree([1, 2, 3, 4])) == [1, 3, 4]       # left node visible at depth 2
    assert f(None) == []


def test_098_validate_bst():
    f = load("w2_098_validate_bst").is_valid_bst
    assert f(build_tree([2, 1, 3])) is True
    assert f(build_tree([5, 1, 4, None, None, 3, 6])) is False
    assert f(build_tree([5, 4, 6, None, None, 3, 7])) is False   # 3 violates root bound
    assert f(build_tree([2, 2, 2])) is False                      # duplicates invalid
    assert f(build_tree([2147483647])) is True


def test_230_kth_smallest():
    f = load("w2_230_kth_smallest").kth_smallest
    assert f(build_tree([3, 1, 4, None, 2]), 1) == 1
    t = build_tree([5, 3, 6, 2, 4, None, None, 1])
    assert [f(t, k) for k in range(1, 7)] == [1, 2, 3, 4, 5, 6]


def test_127_word_ladder():
    f = load("w2_127_word_ladder").ladder_length
    assert f("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]) == 5
    assert f("hit", "cog", ["hot", "dot", "dog", "lot", "log"]) == 0
    assert f("a", "c", ["a", "b", "c"]) == 2


def test_994_rotting_oranges():
    f = load("w2_994_rotting_oranges").oranges_rotting
    g = [[2, 1, 1], [1, 1, 0], [0, 1, 1]]
    assert f(g) == 4
    assert g == [[2, 1, 1], [1, 1, 0], [0, 1, 1]], "don't mutate the input"
    assert f([[2, 1, 1], [0, 1, 1], [1, 0, 1]]) == -1
    assert f([[0, 2]]) == 0
    assert f([[2, 1, 1], [1, 1, 1], [0, 1, 2]]) == 2           # multi-source


def test_1091_shortest_path_binary_matrix():
    f = load("w2_1091_shortest_path_binary_matrix").shortest_path_binary_matrix
    assert f([[0, 1], [1, 0]]) == 2
    assert f([[0, 0, 0], [1, 1, 0], [1, 1, 0]]) == 4
    assert f([[1, 0, 0], [1, 1, 0], [1, 1, 0]]) == -1
    assert f([[0]]) == 1
