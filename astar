
from state import *
import itertools
import random
import time



def min_l_1_norm(points1, points2):
    assert(len(points1) == len(points2))
    if len(points1) == 1:
        return l_1_norm(points1[0], points2[0])
    if len(points1) == 2:
        a = l_1_norm(points1[0], points2[0]) + l_1_norm(points1[1], points2[1])
        b = l_1_norm(points1[0], points2[1]) + l_1_norm(points1[1], points2[0])
        if a < b:
            return a
        return b

    raise Exception("Not implemented! " + str(points1) + " vs " + str(points2))


def make_points(string, cross_pos):
    return set(
        [(x, cross_pos[1]) for x in range(len(string))] + 
        [(cross_pos[0], y) for y in range(len(string))]
    )


def make_dist(string, cross_pos):

    symbols = {s:[] for s in string}
    points = make_points(string, cross_pos)
    chars = {s:[] for s in string}
    for i in range(len(string)):
        symbols[string[i]].append( (i, cross_pos[1]) )
    
    def manhattan(state):
        for s in symbols:
            chars[s] = []
        for p in points:
            ch = get_value(state, p)
            if ch != ECH:
                chars[ch].append( p )
        
        acc = 0
        for s in symbols:
            acc += min_l_1_norm(symbols[s], chars[s])
        return acc
        
    return manhattan


def astar_solve(string, cross_pos):
    print_CROSS_POINT()
    dist = make_dist(string, cross_pos)

    closed = {}
    states_q = {}
    init_state = make_state(string, cross_pos)
    
    print_CROSS_POINT()

    iter_counter = 0
    states_q[dist(init_state)] = { (state_to_tuple(init_state), ()) }
    q_size = 1
    points = make_points(string, cross_pos)

    
    while len(states_q) > 0:
        d = min(states_q.keys())
        tuple_state, trace = states_q[d].pop()
        state = tuple_to_state(tuple_state)

        q_size -= 1

        if len(states_q[d]) == 0:
            del states_q[d]
        
        if tuple_state not in closed:
            closed[tuple_state] = trace
        else:
            if len(closed[tuple_state]) > len(trace):
                closed[tuple_state] = trace
        
        
        print('===============================================', iter_counter, d)
        iter_counter += 1
        ns = neighbors(state, points)
        for act in ns:
            neighbor = ns[act]
            if neighbor != None:
                nd = dist(neighbor)
                tr = tuple(list(trace) + [act])
                if nd == 0:
                    print("Return:", neighbor)
                    return tr
                nd += len(tr)
                tuple_neighbor = state_to_tuple(neighbor)
                if tuple_neighbor not in closed:
                    print('.', end='')
                    q_size += 1
                    if nd not in states_q:
                        states_q[nd] = { (tuple_neighbor, tr) }
                    else:
                        states_q[nd].add( (tuple_neighbor, tr) )

        print('\n' + str(q_size))
        print(str(len(closed)))
        if len(closed) >= 5000:
            break
    
    print("Failed!")
    # for state in closed:
    #     print(state, closed[state])

result = astar_solve("МАНИФЕСТАЦИЯ", (9, 9))
print(result)
