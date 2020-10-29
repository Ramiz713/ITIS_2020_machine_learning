import matplotlib.pyplot as plt
import numpy as np
import sys
from enum import Enum


class Flag(Enum):
    GREEN = 0
    YELLOW = 1
    RED = 2
    UNKNOWN = -1


def dist(x1, y1, x2, y2):
    return np.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


n = 100
x = np.random.randint(1, 100, n)
y = np.random.randint(1, 100, n)
eps, minPts = 10, 3
flags = []
for i in range(0, n):
    neighb = -1
    for j in range(0, n):
        if dist(x[i], y[i], x[j], y[j]) < eps:
            neighb += 1
    if neighb >= minPts:
        flags.append(Flag.GREEN.value)
    else:
        flags.append(Flag.UNKNOWN.value)
for i in range(0, n):
    if flags[i] == Flag.UNKNOWN.value:
        for j in range(0, n):
            if flags[j] == Flag.GREEN.value and dist(x[i], y[i], x[j], y[j]) < eps:
                flags[i] = Flag.YELLOW.value
                break
    if flags[i] == Flag.UNKNOWN.value:
        flags[i] = Flag.RED.value
clusters = np.zeros(n)
cl = 1
for i in range(0, n):
    if flags[i] == Flag.GREEN.value:
        if clusters[i] == 0:
            clusters[i] = cl
            cl += 1
        for j in range(0, n):
            if dist(x[i], y[i], x[j], y[j]) < eps:
                clusters[j] = clusters[i]
for i in range(0, n):
    if flags[i] == Flag.YELLOW.value:
        min_dist = eps
        nearest_point_index = i
        for j in range(0, n):
            cur_dist = dist(x[i], y[i], x[j], y[j])
            if (flags[j] == Flag.GREEN.value and cur_dist < min_dist):
                nearest_point_index = j
                min_dist = cur_dist
        clusters[i] = clusters[nearest_point_index]
print(clusters)
for i in range(0, n):
    if (flags[i] == Flag.RED.value):
        plt.scatter(x[i], y[i], c='r')
    if (flags[i] == Flag.GREEN.value):
        plt.scatter(x[i], y[i], c='green')
    if (flags[i] == Flag.YELLOW.value):
        plt.scatter(x[i], y[i], c='yellow')
plt.show()
for i in range(0, n):
    if (flags[i] == Flag.RED.value):
        plt.scatter(x[i], y[i], c='r')
    else:
        clr = (clusters[i] + 1) / cl
        plt.scatter(x[i], y[i], color=(clr, 0.2, clr ** 2))
plt.show()
