import numpy as np
from graph import ArenaGraph, PlayerGraph, BombGraph, BLOCK_SIZE, PLAYER_SIZE
import pygame

TIME_SPEED = 1
DEBUG = False

class Player:
    X_POS = 0
    Y_POS = 0
    ID = 0

    def __init__(self, ID, ARENA):
        self.ID = ID
        self.ARENA = ARENA
        self.BOMBS = []
        self.speed = 1
        self.bomb_power = 1

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
        self.graph = PlayerGraph(ID, self.X_POS, self.Y_POS)
        
    def update(self, userInputs):
        # userInputs[0] - 1 (se move)  0 (fica parado) - movimento
        # userInputs[1] - 1 (vertical) 0 (horizontal)  - direção
        # userInputs[2] - 1 (positivo) 0 (negativo)    - sentido
        # userInputs[3] - 1 (bomba)    0 (nada)        - bomba
        for k in range(self.speed):
            if userInputs[0] == 1:
                if userInputs[1] == 1:
                    if userInputs[2] == 1:
                        self.Y_POS -= 1
                        if self.ARENA.hasBlockGlobal(self.X_POS, self.Y_POS):
                            self.Y_POS += 2
                        self.graph.update("K_UP", self.X_POS, self.Y_POS)
                    else:
                        self.Y_POS += 1
                        if self.ARENA.hasBlockGlobal(self.X_POS, self.Y_POS):
                            self.Y_POS -= 2
                        self.graph.update("K_DOWN", self.X_POS, self.Y_POS)
                else:
                    if userInputs[2] == 1:
                        self.X_POS += 1
                        if self.ARENA.hasBlockGlobal(self.X_POS, self.Y_POS):
                            self.X_POS -= 2
                        self.graph.update("K_RIGHT", self.X_POS, self.Y_POS)
                    else:
                        self.X_POS -= 1
                        if self.ARENA.hasBlockGlobal(self.X_POS, self.Y_POS):
                            self.X_POS += 2
                        self.graph.update("K_LEFT", self.X_POS, self.Y_POS)
        if userInputs[3] == 1:
            self.BOMBS.append(Bomb(self))
        for bomb in self.BOMBS:
            bomb.update()         

    def drawn(self):
        self.graph.draw(self.ARENA.WIDTH, self.ARENA.HEIGHT)

class Bomb:
    
    def __init__(self, owner):
        self.X_POS = owner.X_POS // BLOCK_SIZE + 1
        self.Y_POS = owner.Y_POS // BLOCK_SIZE + 1
        self.OWNER = owner
        self.bomb_power = owner.bomb_power
        self.step = 0
        self.time = pygame.time.get_ticks()
        self.boom = False

    def update(self):
        if not(self.boom):
            BombGraph.draw(self.X_POS,self.Y_POS,self.step,self.OWNER.ARENA.WIDTH, self.OWNER.ARENA.HEIGHT)
            self.step += 1
            if self.step > 15:
                self.step = 0
            if pygame.time.get_ticks() - self.time >= 3000 / TIME_SPEED:
                self.explode()
        else:
            self.boom = True
    
    def explode(self):
        self.boom = True


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

    def hasBlockGlobal(self, X_POS, Y_POS):
        left_x = (X_POS) // BLOCK_SIZE + 1
        right_x = (X_POS + PLAYER_SIZE) // BLOCK_SIZE + 1
        up_y = (Y_POS) // BLOCK_SIZE + 1
        down_y = (Y_POS + PLAYER_SIZE) // BLOCK_SIZE + 1

        if DEBUG:
            print([left_x, up_y, self.MATRIX[left_x][up_y]])

        if self.MATRIX[left_x][up_y] != '-' or self.MATRIX[right_x][up_y] != '-' or self.MATRIX[left_x][down_y] != '-' or self.MATRIX[right_x][down_y] != '-':
            return True
        return False
                    
    def update(self):
        print("arena update")

    def drawn(self):
        ArenaGraph.draw(self.MATRIX, self.WIDTH+2, self.HEIGHT+2)
