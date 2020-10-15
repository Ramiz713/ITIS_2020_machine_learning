import matplotlib.pyplot as plt
import numpy as np
import random


def visualize_cluster(k, x, y, x_c, y_c, clust):
    color = ["#" + ''.join([random.choice('0123456789ABCDEF') for j in range(6)])
             for i in range(k)]
    for i in range(0, k):
        x_points = []
        y_points = []
        for j in range(0, len(x)):
            if clust[j] == i:
                x_points.append(x[j])
                y_points.append(y[j])
        plt.scatter(x_points, y_points, color=color[i])
    plt.scatter(x_c, y_c, color='black')
    plt.show()


def dist(x1, y1, x2, y2):
    return np.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


def cluster(k, x, y, x_c, y_c):
    clust = []
    for i in range(0, len(x)):
        min = dist(x[i], y[i], x_c[0], y_c[0])
        min_numb = 0
        for j in range(1, k):
            if min > dist(x[i], y[i], x_c[j], y_c[j]):
                min = dist(x[i], y[i], x_c[j], y_c[j])
                min_numb = j
        clust.append(min_numb)
    return clust


def recalc_c(k, x, y, x_c, y_c, clust):
    for i in range(0, k):
        average_x = 0
        average_y = 0
        count = 0
        for j in range(0, len(x)):
            if clust[j] == i:
                count += 1
                average_x += x[j]
                average_y += y[j]
        x_c[i] = average_x / count
        y_c[i] = average_y / count


def total_dist_criterion(k, x, y, x_c, y_c, clust):
    total_dist = 0
    for i in range(0, k):
        for j in range(0, len(x)):
            if clust[j] == i:
                total_dist += dist(x[j], y[j], x_c[i], y_c[i])
    return total_dist


def k_means(k, x, y):
    x_cc = np.mean(x)
    y_cc = np.mean(y)
    r = []
    for i in range(0, n):
        r.append(dist(x[i], y[i], x_cc, y_cc))
    R = max(r)
    x_c, y_c = [], []
    for i in range(0, k):
        x_c.append(R * np.cos(2 * np.pi * i / k) + x_cc)
        y_c.append(R * np.sin(2 * np.pi * i / k) + y_cc)
    plt.scatter(x, y)
    plt.scatter(x_c, y_c, color='r')

    clust = cluster(k, x, y, x_c, y_c)
    recalc_c(k, x, y, x_c, y_c, clust)
    new_clust = cluster(k, x, y, x_c, y_c)
    while clust != new_clust:
        clust = new_clust
        recalc_c(k, x, y, x_c, y_c, clust)
        new_clust = cluster(k, x, y, x_c, y_c)

    visualize_cluster(k, x, y, x_c, y_c, clust)
    return total_dist_criterion(k, x, y, x_c, y_c, new_clust)


n = 100
x = np.random.randint(1, 100, n)
y = np.random.randint(1, 100, n)
k = 3
prev_result = k_means(k - 1, x, y)
current_result = k_means(k, x, y)
next_result = k_means(k + 1, x, y)
falling_speed = abs(current_result - next_result) / abs(prev_result - current_result)
print(falling_speed)
while (True):
    prev_result = current_result
    current_result = next_result
    next_result = k_means(k + 2, x, y)
    new_falling_speed = abs(current_result - next_result) / abs(prev_result - current_result)
    print(new_falling_speed)
    if (new_falling_speed < falling_speed):
        falling_speed = new_falling_speed
    else:
        break
    k += 1
print("Optimal count of k is ",k)
