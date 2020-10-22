import matplotlib.pyplot as plt
import numpy as np


def dist(x1, y1, x2, y2):
    return np.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


def recalc_c(x, y, x_c, y_c, matrix, k, m):
    for j in range(k):
        numerator_x = 0
        numerator_y = 0
        denominator = 0
        for i in range(len(x)):
            numerator_x += x[i] * matrix[i][j] ** m
            numerator_y += y[i] * matrix[i][j] ** m
            denominator += matrix[i][j] ** m
        x_c[j] = numerator_x / denominator
        y_c[j] = numerator_y / denominator


def calculate_matrix(x, y, x_c, y_c, k, m):
    matrix = [[0] * k for i in range(len(x))]
    for i in range(len(x)):
        for j in range(k):
            for l in range(k):
                matrix[i][j] += (dist(x[i], y[i], x_c[j], y_c[j]) / dist(x[i], y[i], x_c[l], y_c[l])) ** (2 / m - 1)
            matrix[i][j] = 1 / matrix[i][j]
    return matrix


def find_max_element(matrix, new_matrix, n, k):
    max_element = 0
    for i in range(0, n):
        for j in range(0, k):
            temp = abs(matrix[i][j] - new_matrix[i][j])
            if (temp > max_element):
                max_element = temp
    return max_element


def с_means(x, y, n, k, m, epsilon):
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
    plt.scatter(x_c, y_c, color='r')

    matrix = calculate_matrix(x, y, x_c, y_c, k, m)
    iteration_count = 2
    while (True):
        recalc_c(x, y, x_c, y_c, matrix, k, m)
        new_matrix = calculate_matrix(x, y, x_c, y_c, k, m)
        if (find_max_element(matrix, new_matrix, n, k) < epsilon):
            break
        else:
            matrix = new_matrix
            iteration_count += 1
    return iteration_count


n = 100
k = 4
m = 2
epsilon = 0.01
x = np.random.randint(1, n, n)
y = np.random.randint(1, n, n)
print("total iteration count", с_means(x, y, n, k, m, epsilon))
