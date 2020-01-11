import random

class Point:
    def __init__(point, value, place):
        point.value = value
        point.place = place

    def _eq_(point1, point2):
        return point1.value == point2.value and point1.place == point2.place

    def soed(point):
        if point.place == 1:
            sosedi = [2]
        elif point.place == 2:
            sosedi = [1, 3]
        elif point.place == 3:
            sosedi = [2, 4]
        elif point.place == 4:
            sosedi = [3, 5]
        elif point.place == 5:
            sosedi = [4, 6]
        elif point.place == 6:
            sosedi = [5, 7]
        elif point.place == 7:
            sosedi = [6, 8]
        elif point.place == 8:
            sosedi = [7, 9]
        elif point.place == 9:
            sosedi = [8, 10]
        elif point.place == 10:
            sosedi = [9, 11, 13, 23]
        elif point.place == 11:
            sosedi = [10, 12]
        elif point.place == 12:
            sosedi = [11]
        elif point.place == 13:
            sosedi = [10, 14]
        elif point.place == 14:
            sosedi = [13]
        elif point.place == 15:
            sosedi = [16]
        elif point.place == 16:
            sosedi = [15, 17]
        elif point.place == 17:
            sosedi = [16, 18]
        elif point.place == 18:
            sosedi = [17, 19]
        elif point.place == 19:
            sosedi = [18, 20]
        elif point.place == 20:
            sosedi = [19, 21]
        elif point.place == 21:
            sosedi = [20, 22]
        elif point.place == 22:
            sosedi = [21, 23]
        elif point.place == 23:
            sosedi = [22, 10]        
        return sosedi


class Vector:
    def __init__(vector, a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w):
        point1 = Point(a, 1)
        point2 = Point(b, 2)
        point3 = Point(c, 3)
        point4 = Point(d, 4)
        point5 = Point(e, 5)
        point6 = Point(f, 6)
        point7 = Point(g, 7)
        point8 = Point(h, 8)
        point9 = Point(i, 9)
        point10 = Point(j, 10)
        point11 = Point(k, 11)
        point12 = Point(l, 12)
        point13 = Point(m, 13)
        point14 = Point(n, 14)
        point15 = Point(o, 15)
        point16 = Point(p, 16)
        point17 = Point(q, 17)
        point18 = Point(r, 18)
        point19 = Point(s, 19)
        point20 = Point(t, 20)
        point21 = Point(u, 21)
        point22 = Point(v, 22)
        point23 = Point(w, 23)
        vector.value = [point1, point2, point3, point4, point5, point6, point7, point8, point9, point10, point11,
                        point12, point13, point14, point15, point16, point17, point18, point19, point20, point21, point22,
                        point23]

    def getLength(vector1, vector2):
        length = 0
        for points1 in vector1.value:
            dif = []
            count = 0
            for points2 in vector2.value:
                if points1.value == points2.value:
                    delta = abs(points1.place - points2.place)
                    dif.append(delta)
                    count = count + 1
            dif.sort
            num = random.choice(dif)
            length = length + num
        return length/10

    def swap(vector, a, b):
        for points in vector.value:
            if points.place == a:
                pointa = points
            if points.place == b:
                pointb = points
        pointa.place = b
        pointb.place = a
        vector.value[a - 1] = pointb
        vector.value[b - 1] = pointa
        if pointa.value == pointb.value:
            return None
        else:
            return vector


class PathFinding:
    class Node:
        def __init__(node, parent, vector):
            node.parent = parent
            node.vector = vector
            node.f = 0.0
            node.g = 0.0
            node.h = 0.0

        def generateChildren(node, vector):
            children = []
            vectorst = vector
            for points in vectorst.value:
                if points.value == 0:
                    sosedi = Point.soed(points)
                    for sosed in sosedi:
                        vectorstart = Vector(vector.value[0].value, vector.value[1].value, vector.value[2].value,
                                             vector.value[3].value, vector.value[4].value, vector.value[5].value,
                                             vector.value[6].value, vector.value[7].value, vector.value[8].value,
                                             vector.value[9].value, vector.value[10].value, vector.value[11].value,
                                             vector.value[12].value, vector.value[13].value, vector.value[14].value,
                                             vector.value[15].value, vector.value[16].value, vector.value[17].value,
                                             vector.value[18].value, vector.value[19].value, vector.value[20].value,
                                             vector.value[21].value, vector.value[22].value)
                        vectorbuf = vectorstart.swap(points.place, sosed)
                        if vectorbuf:
                            child = node.generateChild(vectorbuf)
                            children.append(child)
            return children

        def generateChild(node, vector):
            return PathFinding.Node(node, vector)

    @staticmethod
    def getPath(vector_from, vector_to):

        root = PathFinding.Node(None, vector_from)
        root.g = 0.0
        root.h = root.vector.getLength(vector_to)
        root.f = root.g + root.h

        open_set = [root]
        closed_set = []

        while open_set:
            open_set.sort(key=lambda node: node.f)
            best_node = open_set[0]

            if best_node.vector == vector_to:
                path = []
                node = best_node
                while node:
                    path.insert(0, node.vector)
                    node = node.parent
                return path

            open_set.remove(best_node)
            closed_set.append(best_node)
            ex_bn = [best_node.vector.value[0].value, best_node.vector.value[1].value, best_node.vector.value[2].value,
                     best_node.vector.value[3].value, best_node.vector.value[4].value, best_node.vector.value[5].value,
                     best_node.vector.value[6].value, best_node.vector.value[7].value, best_node.vector.value[8].value,
                     best_node.vector.value[9].value, best_node.vector.value[10].value, best_node.vector.value[11].value,
                     best_node.vector.value[12].value, best_node.vector.value[13].value, best_node.vector.value[14].value,
                     best_node.vector.value[15].value, best_node.vector.value[16].value, best_node.vector.value[17].value,
                     best_node.vector.value[18].value, best_node.vector.value[19].value, best_node.vector.value[20].value,
                     best_node.vector.value[21].value, best_node.vector.value[22].value]
            print(best_node.h, best_node.f, best_node.g, ex_bn)

            vectorcurr = best_node.vector
            children = best_node.generateChildren(vectorcurr)
            good_children = children
            for person in children:
                ex_ch = [person.vector.value[0].value, person.vector.value[1].value, person.vector.value[2].value,
                         person.vector.value[3].value, person.vector.value[4].value, person.vector.value[5].value,
                         person.vector.value[6].value, person.vector.value[7].value, person.vector.value[8].value,
                         person.vector.value[9].value, person.vector.value[10].value, person.vector.value[11].value,
                         person.vector.value[12].value, person.vector.value[13].value, person.vector.value[14].value,
                         person.vector.value[15].value, person.vector.value[16].value, person.vector.value[17].value,
                         person.vector.value[18].value, person.vector.value[19].value, person.vector.value[20].value,
                         person.vector.value[21].value, person.vector.value[22].value]
                for nodes in closed_set:
                    ex_cs = [nodes.vector.value[0].value, nodes.vector.value[1].value, nodes.vector.value[2].value,
                             nodes.vector.value[3].value, nodes.vector.value[4].value, nodes.vector.value[5].value,
                             nodes.vector.value[6].value, nodes.vector.value[7].value, nodes.vector.value[8].value,
                             nodes.vector.value[9].value, nodes.vector.value[10].value, nodes.vector.value[11].value,
                             nodes.vector.value[12].value, nodes.vector.value[13].value, nodes.vector.value[14].value,
                             nodes.vector.value[15].value, nodes.vector.value[16].value, nodes.vector.value[17].value,
                             nodes.vector.value[18].value, nodes.vector.value[19].value, nodes.vector.value[20].value,
                             nodes.vector.value[21].value, nodes.vector.value[22].value]
                    if ex_ch == ex_cs:
                        if person in good_children:
                            good_children.remove(person)

            for child in good_children:
                child.g = best_node.g + 1
                child.h = child.vector.getLength(vector_to)
                child.f = child.g + child.h

                ex = [child.vector.value[0].value, child.vector.value[1].value, child.vector.value[2].value,
                      child.vector.value[3].value, child.vector.value[4].value, child.vector.value[5].value,
                      child.vector.value[6].value, child.vector.value[7].value, child.vector.value[8].value,
                      child.vector.value[9].value, child.vector.value[10].value, child.vector.value[11].value,
                      child.vector.value[12].value, child.vector.value[13].value, child.vector.value[14].value,
                      child.vector.value[15].value, child.vector.value[16].value, child.vector.value[17].value,
                      child.vector.value[18].value, child.vector.value[19].value, child.vector.value[20].value,
                      child.vector.value[21].value, child.vector.value[22].value]


                child_from_open_set = None
                for node_from_open_set in open_set:
                    ex_nfos = [node_from_open_set.vector.value[0].value, node_from_open_set.vector.value[1].value,
                               node_from_open_set.vector.value[2].value, node_from_open_set.vector.value[3].value,
                               node_from_open_set.vector.value[4].value, node_from_open_set.vector.value[5].value,
                               node_from_open_set.vector.value[6].value, node_from_open_set.vector.value[7].value,
                               node_from_open_set.vector.value[8].value, node_from_open_set.vector.value[9].value,
                               node_from_open_set.vector.value[10].value, node_from_open_set.vector.value[11].value,
                               node_from_open_set.vector.value[12].value, node_from_open_set.vector.value[13].value,
                               node_from_open_set.vector.value[14].value, node_from_open_set.vector.value[15].value,
                               node_from_open_set.vector.value[16].value, node_from_open_set.vector.value[17].value,
                               node_from_open_set.vector.value[18].value, node_from_open_set.vector.value[19].value,
                               node_from_open_set.vector.value[20].value, node_from_open_set.vector.value[21].value,
                               node_from_open_set.vector.value[22].value]
                    if ex == ex_nfos:
                        child_from_open_set = node_from_open_set

                open_set.append(child)

                if child_from_open_set:
                    if child_from_open_set.g >= child.g:
                        open_set.remove(child_from_open_set)
                    else:
                        open_set.remove(child)

        return []


vector_from = Vector('М', 'А', 'Н', 'И', 'Ф', 'Е', 'С', 'Т', 'А', 'Ц', 'И', 'Я', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0) 
vector_to = Vector(0, 0, 0, 0, 0, 0, 0, 0, 0, 'Ц', 0, 0, 'И', 'Я', 'М', 'А', 'Н', 'И', 'Ф', 'Е', 'С', 'Т', 'А')
path = PathFinding.getPath(vector_from, vector_to)
print(path)