import numpy as np
from graph import ArenaGraph, PlayerGraph, BombGraph, BLOCK_SIZE, PLAYER_SIZE
import pygame

TIME_SPEED = 1
DEBUG = False
DEBUG_PLAYER = 0

class Player:
    X_POS = 0
    Y_POS = 0
    ID = 0

    def __init__(self, ID, ARENA):
        self.ID = ID
        self.ARENA = ARENA
        self.BOMBS = []
        self.speed = 1
        self.max_bomb = 1
        self.bomb_power = 1
        self.place_bomb = False

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
        self.X_ARENA_POS = self.X_POS // BLOCK_SIZE + 1
        self.Y_ARENA_POS = self.Y_POS // BLOCK_SIZE + 1
        
    def update(self, userInputs):
        # userInputs[0] - 1 (se move)  0 (fica parado) - movimento
        # userInputs[1] - 1 (vertical) 0 (horizontal)  - direção
        # userInputs[2] - 1 (positivo) 0 (negativo)    - sentido
        # userInputs[3] - 1 (bomba)    0 (nada)        - bomba
        self.X_ARENA_POS = (self.X_POS + PLAYER_SIZE/2) / BLOCK_SIZE + 1
        self.Y_ARENA_POS = (self.Y_POS + PLAYER_SIZE/2) / BLOCK_SIZE + 1
        if DEBUG and self.ID == DEBUG_PLAYER:
            print([self.X_ARENA_POS, self.Y_ARENA_POS])

        for k in range(self.speed):
            if userInputs[0] == 1:
                if userInputs[1] == 1:
                    if userInputs[2] == 1:
                        self.Y_POS -= 1
                        if self.place_bomb:
                            if not self.ARENA.canGoIn(self.X_POS, self.Y_POS, PLAYER_SIZE, True):
                                self.Y_POS += 2
                        elif not self.ARENA.canGoIn(self.X_POS, self.Y_POS, PLAYER_SIZE):
                                self.Y_POS += 2
                        self.graph.update("K_UP", self.X_POS, self.Y_POS)
                    else:
                        self.Y_POS += 1
                        if self.place_bomb:
                            if not self.ARENA.canGoIn(self.X_POS, self.Y_POS, PLAYER_SIZE, True):
                                self.Y_POS -= 2
                        elif not self.ARENA.canGoIn(self.X_POS, self.Y_POS, PLAYER_SIZE):
                            self.Y_POS -= 2
                        self.graph.update("K_DOWN", self.X_POS, self.Y_POS)
                else:
                    if userInputs[2] == 1:
                        self.X_POS += 1
                        if self.place_bomb:
                            if not self.ARENA.canGoIn(self.X_POS, self.Y_POS, PLAYER_SIZE, True):
                                self.X_POS -= 2
                        elif not self.ARENA.canGoIn(self.X_POS, self.Y_POS, PLAYER_SIZE):
                            self.X_POS -= 2
                        self.graph.update("K_RIGHT", self.X_POS, self.Y_POS)
                    else:
                        self.X_POS -= 1
                        if self.place_bomb:
                            if not self.ARENA.canGoIn(self.X_POS, self.Y_POS, PLAYER_SIZE, True):
                                self.X_POS += 2
                        elif not self.ARENA.canGoIn(self.X_POS, self.Y_POS, PLAYER_SIZE):
                            self.X_POS += 2
                        self.graph.update("K_LEFT", self.X_POS, self.Y_POS)
        if userInputs[3] == 1 and len(self.BOMBS) < self.max_bomb:
            if self.ARENA.hasBlockPosition(self.X_ARENA_POS, self.Y_ARENA_POS) == '-':
                self.BOMBS.append(Bomb(self))
                self.place_bomb = True
        if self.ARENA.hasBlockGlobal(self.X_POS, self.Y_POS) == '-':
            self.place_bomb = False
        for bomb in self.BOMBS:
            bomb.update()

    def drawn(self):
        self.graph.draw(self.ARENA.WIDTH, self.ARENA.HEIGHT)

class Bomb:
    exist = True
    
    def __init__(self, owner):
        self.X_POS = int(owner.X_ARENA_POS)
        self.Y_POS = int(owner.Y_ARENA_POS)
        self.OWNER = owner
        self.bomb_power = owner.bomb_power
        self.step = 0
        self.time = pygame.time.get_ticks()
        self.boom = False
        self.OWNER.ARENA.MATRIX[self.X_POS][self.Y_POS] = '0'

    def update(self):
        if not(self.boom):
            BombGraph.draw(self.X_POS,self.Y_POS,self.step,self.OWNER.ARENA.WIDTH, self.OWNER.ARENA.HEIGHT)
            self.step += 1
            if self.step > 15:
                self.step = 0
            if pygame.time.get_ticks() - self.time >= 3000 / TIME_SPEED:
                self.step = 0
                self.explode()
        elif self.exist:
            BombGraph.explosion_draw(self.X_POS,self.Y_POS,self.step, "start", 0,self.OWNER.ARENA.WIDTH, self.OWNER.ARENA.HEIGHT)
            self.explosionRec("x+", self.X_POS + 1, self.Y_POS, self.bomb_power)
            self.explosionRec("y-", self.X_POS, self.Y_POS - 1, self.bomb_power)
            self.explosionRec("x-", self.X_POS - 1, self.Y_POS, self.bomb_power)
            self.explosionRec("y+", self.X_POS, self.Y_POS + 1, self.bomb_power)
            self.step += 1
            if self.step >= 35:
                self.exist = False
                self.OWNER.ARENA.MATRIX[self.X_POS][self.Y_POS] = '-'
                self.OWNER.BOMBS.remove(self)

    def explosionRec(self, dir, x, y, left):
        if left == 0 or self.OWNER.ARENA.hasBlockPosition(x, y) == 'o':
            return
        if self.OWNER.ARENA.checkBrickDestroy(x,y,self.step==34):
            BombGraph.explosion_draw(x ,y,self.step, "block", 0,self.OWNER.ARENA.WIDTH, self.OWNER.ARENA.HEIGHT)
            return

        if 'x' in dir:
            if '+' in dir:
                rot = 0
                self.explosionRec(dir, x+1, y, left-1)
            elif '-' in dir:
                rot = 180
                self.explosionRec(dir, x-1, y, left-1)
        else:
            if '+' in dir:
                rot = 270
                self.explosionRec(dir, x, y+1, left-1) 
            else:
                rot = 90
                self.explosionRec(dir, x, y-1, left-1)
        
        if left == 1: 
            BombGraph.explosion_draw(x,y,self.step, "end", rot,self.OWNER.ARENA.WIDTH, self.OWNER.ARENA.HEIGHT)
        else:
            BombGraph.explosion_draw(x,y,self.step, "middle", rot,self.OWNER.ARENA.WIDTH, self.OWNER.ARENA.HEIGHT)
    
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

    def canGoIn(self, X_POS, Y_POS, OBJECT_SIZE, MOVE_THROUGH_BOMB = False):
        left_x = (X_POS) // BLOCK_SIZE + 1
        right_x = (X_POS + OBJECT_SIZE) // BLOCK_SIZE + 1
        up_y = (Y_POS) // BLOCK_SIZE + 1
        down_y = (Y_POS + OBJECT_SIZE) // BLOCK_SIZE + 1

        if self.MATRIX[left_x][up_y] != '-':
            if not(MOVE_THROUGH_BOMB and self.MATRIX[left_x][up_y] == '0'):
                return False
        if self.MATRIX[right_x][up_y] != '-':
            if not(MOVE_THROUGH_BOMB and self.MATRIX[right_x][up_y] == '0'):
                return False
        if self.MATRIX[left_x][down_y] != '-':
            if not(MOVE_THROUGH_BOMB and self.MATRIX[left_x][down_y] == '0'):
                return False
        if self.MATRIX[right_x][down_y] != '-':
            if not(MOVE_THROUGH_BOMB and self.MATRIX[right_x][down_y] == '0'):
                return False
        return True

    def hasBlockGlobal(self, X_POS, Y_POS):
        left_x = (X_POS) // BLOCK_SIZE + 1
        right_x = (X_POS + PLAYER_SIZE) // BLOCK_SIZE + 1
        up_y = (Y_POS) // BLOCK_SIZE + 1
        down_y = (Y_POS + PLAYER_SIZE) // BLOCK_SIZE + 1

        #if DEBUG and DEBUG_PLAYER == PLAYER:
        #    print([left_x, up_y, self.MATRIX[left_x][up_y]])

        if self.MATRIX[left_x][up_y] != '-':
            return self.MATRIX[left_x][up_y]
        elif self.MATRIX[right_x][up_y] != '-':
            return self.MATRIX[right_x][up_y]
        elif self.MATRIX[left_x][down_y] != '-':
            return self.MATRIX[left_x][down_y]
        elif self.MATRIX[right_x][down_y] != '-':
            return self.MATRIX[right_x][down_y]
        return '-'

    def hasBlockGlobalDir(self, X_POS, Y_POS, DIR):
        left_x = (X_POS) // BLOCK_SIZE + 1
        right_x = (X_POS + PLAYER_SIZE) // BLOCK_SIZE + 1
        up_y = (Y_POS) // BLOCK_SIZE + 1
        down_y = (Y_POS + PLAYER_SIZE) // BLOCK_SIZE + 1

        if self.MATRIX[left_x][up_y] != '-' and ('L' in DIR or 'U' in DIR):
            return self.MATRIX[left_x][up_y]
        elif self.MATRIX[right_x][up_y] != '-' and ('R' in DIR or 'U' in DIR):
            return self.MATRIX[right_x][up_y]
        elif self.MATRIX[left_x][down_y] != '-' and ('L' in DIR or 'D' in DIR):
            return self.MATRIX[left_x][down_y]
        elif self.MATRIX[right_x][down_y] != '-' and ('R' in DIR or 'D' in DIR):
            return self.MATRIX[right_x][down_y]
        return '-'

    def hasBlockPosition(self, X_POS, Y_POS):
        X_POS = int(X_POS)
        Y_POS = int(Y_POS)

        if self.MATRIX[X_POS][Y_POS] != '-':
            return  self.MATRIX[X_POS][Y_POS]
        return '-'

    def checkBrickDestroy(self, X_POS, Y_POS, bool_destroy):
        if self.MATRIX[X_POS][Y_POS] == '*':
            if bool_destroy:
                # TODO: Drop ITEM
                self.MATRIX[X_POS][Y_POS] = '-'
            return True
        return False
                    
    def update(self):
        print("arena update")

    def drawn(self):
        ArenaGraph.draw(self.MATRIX, self.WIDTH+2, self.HEIGHT+2)
