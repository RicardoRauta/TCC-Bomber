import numpy as np
from graph import ArenaGraph, PlayerGraph, BLOCK_SIZE

class Player:
    X_POS = 0
    Y_POS = 0
    ID = 0

    def __init__(self, ID, ARENA):
        self.ID = ID
        self.ARENA = ARENA
        
        if ID == 0:
            self.X_POS = 0
            self.Y_POS = 0
        elif ID == 1:
            self.X_POS = BLOCK_SIZE*ARENA.WIDTH - BLOCK_SIZE
            self.Y_POS = 0
        elif ID == 2:
            self.X_POS = 0
            self.Y_POS = BLOCK_SIZE*ARENA.HEIGHT - BLOCK_SIZE
        elif ID == 3:
            self.X_POS = BLOCK_SIZE*ARENA.WIDTH - BLOCK_SIZE
            self.Y_POS = BLOCK_SIZE*ARENA.HEIGHT - BLOCK_SIZE
        self.graph = PlayerGraph(ID)

    def update(self, userInputs):
        # userInputs[0] - 1 (se move)  0 (fica parado) - movimento
        # userInputs[1] - 1 (vertical) 0 (horizontal)  - direção
        # userInputs[2] - 1 (positivo) 0 (negativo)    - sentido
        # userInputs[3] - 1 (bomba)    0 (nada)        - bomba
        if userInputs[0] == 1:
            if userInputs[1] == 1:
                if userInputs[2] == 1:
                    self.Y_POS -= 1
                    self.graph.update("K_UP", self.X_POS, self.Y_POS)
                else:
                    self.Y_POS += 1
                    self.graph.update("K_DOWN", self.X_POS, self.Y_POS)
            else:
                if userInputs[2] == 1:
                    self.X_POS += 1
                    self.graph.update("K_RIGHT", self.X_POS, self.Y_POS)
                else:
                    self.X_POS += 1
                    self.graph.update("K_LEFT", self.X_POS, self.Y_POS)
        if userInputs[3] == 1:
            print("bomba")

    def drawn(self):
        self.graph.draw(self.ARENA.WIDTH, self.ARENA.HEIGHT)

class Bomb:
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

    def update(self):
        print("arena update")

    def drawn(self):
        ArenaGraph.draw(self.MATRIX, self.WIDTH+2, self.HEIGHT+2)
