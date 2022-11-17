import numpy as np
from graph import ArenaGraph, PlayerGraph

class Player:
    X_POS = 0
    Y_POS = 0

class Arena:
    WIDTH = 9
    HEIGHT = 9
    MATRIX = []

    def __init__(self, WIDTH, HEIGHT):
        self.WIDTH = WIDTH
        self.MATRIX = HEIGHT
        self.createMatrix()

    def onEdge(self, positionX, positionY):
        if positionX == 0 or positionX == self.WIDTH+1:
            return True
        if positionY == 0 or positionY == self.HEIGHT+1:
            return True
        return False

    def createMatrix(self):
        self.MATRIX = []
        for i in range(self.WIDTH+2):
            col = []
            for j in range(self.HEIGHT+2):
                col.append('*')
            self.MATRIX.append(col)

        for i in range(self.WIDTH+2):
            for j in range(self.HEIGHT+2):
                if self.onEdge(i,j):
                    self.MATRIX[i][j] = 'o'
                elif (i == 1 or i == self.WIDTH) and (j <= 2 or j >= self.HEIGHT-1):
                    self.MATRIX[i][j] = '-'
                elif (j == 1 or j == self.HEIGHT) and (i <= 2 or i >= self.WIDTH-1):
                    self.MATRIX[i][j] = '-'
                elif (i % 2 == 0) and (j % 2 == 0):
                    self.MATRIX[i][j] = 'o'

    def drawnArena(self):
        ArenaGraph.draw(self.MATRIX, self.WIDTH+2, self.HEIGHT+2)