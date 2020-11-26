import pygame
from sklearn import svm
import matplotlib.pyplot as plt
import numpy as np

pygame.init()
screen = pygame.display.set_mode((700, 500))
screen.fill((255, 255, 255))
pygame.display.update()

coords_x = []
coords_y = []
coords = []
clust = []

play = True
while play:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                pygame.draw.circle(screen, (255, 0, 0), event.pos, 10)
                pygame.display.update()
                clust.append(0)
            elif event.button == 3:
                pygame.draw.circle(screen, (0, 255, 0), event.pos, 10)
                pygame.display.update()
                clust.append(1)
            coords_x.append(event.pos[0])
            coords_y.append(event.pos[1])
            coords.append(event.pos)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                clf = svm.SVC(C=1.0, kernel='linear')
                clf.fit(coords, clust)

                w = clf.coef_[0]
                a = -w[0] / w[1]
                xx = np.linspace(0, 700, 2)
                yy = a * xx - (clf.intercept_[0]) / w[1]

                plt.axis([0.0, 600.0, 600.0, 0.0])
                plt.plot(xx, yy, c='r')
                plt.scatter(coords_x, coords_y, c=clust)
                plt.xlabel("x")
                plt.ylabel("y")
                plt.show()
