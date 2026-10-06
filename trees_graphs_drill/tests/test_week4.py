from conftest import load


def test_743_network_delay():
    f = load("w4_743_network_delay").network_delay_time
    assert f([[2, 1, 1], [2, 3, 1], [3, 4, 1]], 4, 2) == 2
    assert f([[1, 2, 1]], 2, 1) == 1
    assert f([[1, 2, 1]], 2, 2) == -1
    assert f([[1, 2, 10], [1, 3, 1], [3, 2, 1]], 3, 1) == 2     # longer hop count is cheaper


def test_787_cheapest_flights():
    f = load("w4_787_cheapest_flights").find_cheapest_price
    fl = [[0, 1, 100], [1, 2, 100], [2, 0, 100], [1, 3, 600], [2, 3, 200]]
    assert f(4, fl, 0, 3, 1) == 700
    fl2 = [[0, 1, 100], [1, 2, 100], [0, 2, 500]]
    assert f(3, fl2, 0, 2, 1) == 200
    assert f(3, fl2, 0, 2, 0) == 500
    # trap for plain Dijkstra: cheap path to node 2 uses too many stops
    fl3 = [[0, 1, 1], [1, 2, 1], [0, 2, 5], [2, 3, 1]]
    assert f(4, fl3, 0, 3, 1) == 6
    assert f(2, [[0, 1, 5]], 1, 0, 3) == -1


def test_1584_min_cost_connect_points():
    f = load("w4_1584_min_cost_connect_points").min_cost_connect_points
    assert f([[0, 0], [2, 2], [3, 10], [5, 2], [7, 0]]) == 20
    assert f([[3, 12], [-2, 5], [-4, 1]]) == 18
    assert f([[0, 0]]) == 0


def test_778_swim_rising_water():
    f = load("w4_778_swim_rising_water").swim_in_water
    assert f([[0, 2], [1, 3]]) == 3
    g = [[0, 1, 2, 3, 4], [24, 23, 22, 21, 5], [12, 13, 14, 15, 16], [11, 17, 18, 19, 20], [10, 9, 8, 7, 6]]
    assert f(g) == 16
    assert f([[0]]) == 0


def _norm(edges):
    return sorted(tuple(sorted(e)) for e in edges)


def test_1192_critical_connections():
    f = load("w4_1192_critical_connections").critical_connections
    assert _norm(f(4, [[0, 1], [1, 2], [2, 0], [1, 3]])) == [(1, 3)]
    assert _norm(f(2, [[0, 1]])) == [(0, 1)]
    assert _norm(f(6, [[0, 1], [1, 2], [2, 0], [1, 3], [3, 4], [4, 5], [5, 3]])) == [(1, 3)]
    assert f(3, [[0, 1], [1, 2], [2, 0]]) == []
