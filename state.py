
import copy
import functools
from itertools import product

ECH = ' '

I = {
    'vline': 1,
    'hline': 0,
    'info': 2
}

G = {
    'vpos': 0,
    'hpos': 1,
    'str':  2
}

global CROSS_POINT
CROSS_POINT = 42

def make_state(string, cross_point):
    global CROSS_POINT
    v_line = [s for s in string]
    h_line = [ECH for s in string]
    CROSS_POINT = (cross_point[0], cross_point[1], len(string))
    h_line[cross_point[0]] = v_line[cross_point[1]]
    return [h_line, v_line]


def print_CROSS_POINT():
    print("Cross:", CROSS_POINT)


def state_to_tuple(state):
    return tuple(map(tuple, state))


def tuple_to_state(tuple_state):
    return list(map(list, tuple_state))


def get_neighbor_points(point):
    x, y = point
    hpos, vpos, size = CROSS_POINT
    if x != hpos and y != vpos:
        return set()

    neighbors = set()
    if x == hpos:
        if y > 0:
            neighbors.add((x, y-1))
        if y < size - 1:
            neighbors.add((x, y+1))
    if y == vpos:
        if x > 0:
            neighbors.add((x-1, y))
        if x < size - 1:
            neighbors.add((x+1, y))
    return neighbors


def set_value(state, point, value):
    if point[0] == CROSS_POINT[0]:
        state[1][point[1]] = value
    if point[1] == CROSS_POINT[1]:
        state[0][point[0]] = value
    return state


def get_value(state, point):
    if point[0] == CROSS_POINT[0]:
        return state[1][point[1]]
    if point[1] == CROSS_POINT[1]:
        return state[0][point[0]]
        

def swap(state, p1, p2):
    new_state = copy.deepcopy(state)
    value1 = get_value(new_state, p1)
    value2 = get_value(new_state, p2)
    if value1 != ECH and value2 != ECH:
        return None
    if value1 == ECH and value2 == ECH:
        return None
    set_value(new_state, p1, value2)
    set_value(new_state, p2, value1)
    return new_state


def l_1_norm(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])


def neighbors(state, points):
    transpositions = set()
    for p in points:
        transpositions.update([
            (p, np) for np in get_neighbor_points(p)
            if p < np 
        ])

    return {
        transposition: swap(state, *transposition)
        for transposition in transpositions
    }
