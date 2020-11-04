import random
import math
import pylab as pl
import numpy as np
from matplotlib.colors import ListedColormap


def dist(a, b):
    return math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)


def generateData(numberOfClassEl, numberOfClasses):
    data = []
    for classNum in range(numberOfClasses):
        centerX, centerY = random.random() * 5.0, random.random() * 5.0
        for rowNum in range(numberOfClassEl):
            data.append([[random.gauss(centerX, 0.5), random.gauss(centerY, 0.5)], classNum])
    return data


def classifyKNN(trainData, testData, k, numberOfClasses):
    test_labels = []
    for test_point in testData:
        testDist = [[dist(test_point, trainData[i][0]), trainData[i][1]] for i in range(len(trainData))]
        stat = [0 for i in range(numberOfClasses)]
        for d in sorted(testDist)[0:k]:
            stat[d[1]] += 1
        test_labels.append(sorted(zip(stat, range(numberOfClasses)), reverse=True)[0][1])
    return test_labels


def showDataOnMesh(nClasses, nItemsInClass, k):
    def generateTestMesh(trainData):
        x_min = min([trainData[i][0][0] for i in range(len(trainData))]) - 1.0
        x_max = max([trainData[i][0][0] for i in range(len(trainData))]) + 1.0
        y_min = min([trainData[i][0][1] for i in range(len(trainData))]) - 1.0
        y_max = max([trainData[i][0][1] for i in range(len(trainData))]) + 1.0
        h = 0.05
        test_x, test_y = np.meshgrid(np.arange(x_min, x_max, h),
                                     np.arange(y_min, y_max, h))
        return [test_x, test_y]

    train_data = generateData(nItemsInClass, nClasses)
    test_mesh = generateTestMesh(train_data)
    test_mesh_labels = classifyKNN(train_data, zip(test_mesh[0].ravel(), test_mesh[1].ravel()), k, nClasses)
    class_colormap = ListedColormap(['#FF0000', '#00FF00', '#FFFFFF'])
    test_colormap = ListedColormap(['#FFAAAA', '#AAFFAA', '#AAAAAA'])
    pl.pcolormesh(test_mesh[0],
                  test_mesh[1],
                  np.asarray(test_mesh_labels).reshape(test_mesh[0].shape),
                  cmap=test_colormap)
    pl.scatter([train_data[i][0][0] for i in range(len(train_data))],
               [train_data[i][0][1] for i in range(len(train_data))],
               c=[train_data[i][1] for i in range(len(train_data))],
               cmap=class_colormap)
    pl.show()


nClasses, N = 3, 40
# k = [√N] округление к ближайшему целому
k = round(math.sqrt(N))
showDataOnMesh(nClasses, N, k)
