from random import randint as rand


def randBool(r, mxr):
    t = rand(0, mxr)
    return t <= r


def randCell(width, height):
    tw = rand(0, width - 1)
    th = rand(0, height - 1)
    return th, tw


def randCell2(x, y):
    moves = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    t = rand(0, 3)
    x2 = moves[t][0]
    y2 = moves[t][1]
    return x + x2, y + y2
