import numpy as np
from typing import List, Any

place = np.array([])
coordinate = []


def aforestation(n, l):
    n = n * 0.01
    place = np.random.choice(a=[True, False], size=(l, l), p=[n, 1 - n])
    return place


def start(r):
    repeat = 1
    list = []
    while repeat != r:
        list.append([r, startfire(place)])
    return list


def startfire(place):
    result=0
    i = 0
    coordinate = []
    while i != place.shape[0] - 1:
        tree = place[:, i]
        result =  fire(tree, i, coordinate)
    i += 1
    return result


def fire(tree, i,coordinate):
    while all(tree) != True:
        for j in range(0, len(tree) - 1):
            if tree[j] == True:
                coordinate.append([i, j])
                tree[j + 1] = True
                tree[j - 1] = True
                coordinate.append([i, j + 1])
                coordinate.append([i, j - 1])
                fire(tree, i,coordinate)
    return coordinate

place = aforestation(20, 10)
print(place)
print(place.shape[0])
print(startfire(place))
