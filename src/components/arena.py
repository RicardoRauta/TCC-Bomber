import pygame, random
from src.config import Config
from src.graph.arena import ArenaGraph
from src.global_state import GlobalState

class Arena:
    WIDTH = 9
    HEIGHT = 9
    MATRIX = []
    BOMBS = []
    PLAYERS = []
    END_PHASE = False
    END_TIMER = 0
    END_COUNTER = 1
    END = False

    def __init__(self, WIDTH, HEIGHT):
        self.WIDTH = WIDTH
        self.MATRIX = HEIGHT
        self.createMatrix()
        self.time = pygame.time.get_ticks()

    def onEdge(self, positionX, positionY):
        if positionX == 0 or positionX == self.WIDTH+1:
            return True
        if positionY == 0 or positionY == self.HEIGHT+1:
            return True
        return False

    def getObjectInPosition(self, positionX, positionY):
        if positionX < 0 or positionX > self.WIDTH+1 or positionY < 0 or positionY > self.HEIGHT+1:
            return None
        else:
            return self.MATRIX[positionX][positionY]

    def createMatrix(self):
        self.MATRIX = []
        for i in range(self.WIDTH+2):
            col = []
            colBomb = []
            for j in range(self.HEIGHT+2):
                #col.append(Config.ARENA_BLOCK)
                col.append(Config.ARENA_VOID)
                colBomb.append(None)
            self.MATRIX.append(col)
            self.BOMBS.append(colBomb)

        for i in range(self.WIDTH+2):
            for j in range(self.HEIGHT+2):
                if self.onEdge(i,j):
                    self.MATRIX[i][j] = Config.ARENA_WALL
                elif (i == 1 or i == self.WIDTH) and (j <= 2 or j >= self.HEIGHT-1):
                    self.MATRIX[i][j] = Config.ARENA_VOID
                elif (j == 1 or j == self.HEIGHT) and (i <= 2 or i >= self.WIDTH-1):
                    self.MATRIX[i][j] = Config.ARENA_VOID
                elif (i % 2 == 0) and (j % 2 == 0):
                    self.MATRIX[i][j] = Config.ARENA_WALL

    def checkDeath(self, X_POS, Y_POS):
        if self.MATRIX[X_POS][Y_POS] == Config.ARENA_WALL or self.MATRIX[X_POS][Y_POS] == Config.ARENA_EXPLOSION:
            return True
        return False

    def canGoIn(self, X_POS, Y_POS, OBJECT_SIZE, X_POS_A, Y_POS_A):
        MOVE_THROUGH_BOMB = True#int(X_POS) == int(X_POS_A) and int(Y_POS) == int(Y_POS_A)
        left_x = (X_POS) // Config.BLOCK_SIZE + 1
        right_x = (X_POS + OBJECT_SIZE) // Config.BLOCK_SIZE + 1
        up_y = (Y_POS) // Config.BLOCK_SIZE + 1
        down_y = (Y_POS + OBJECT_SIZE) // Config.BLOCK_SIZE + 1

        if self.MATRIX[left_x][up_y] == Config.ARENA_BOMB or self.MATRIX[left_x][up_y] == Config.ARENA_BLOCK or self.MATRIX[left_x][up_y] == Config.ARENA_WALL:
            if not(MOVE_THROUGH_BOMB and self.MATRIX[left_x][up_y] == Config.ARENA_BOMB):
                return False
        if self.MATRIX[right_x][up_y] == Config.ARENA_BOMB  or self.MATRIX[right_x][up_y] == Config.ARENA_BLOCK or self.MATRIX[right_x][up_y] == Config.ARENA_WALL:
            if not(MOVE_THROUGH_BOMB and self.MATRIX[right_x][up_y] == Config.ARENA_BOMB):
                return False
        if self.MATRIX[left_x][down_y] == Config.ARENA_BOMB  or self.MATRIX[left_x][down_y] == Config.ARENA_BLOCK or self.MATRIX[left_x][down_y] == Config.ARENA_WALL:
            if not(MOVE_THROUGH_BOMB and self.MATRIX[left_x][down_y] == Config.ARENA_BOMB):
                return False
        if self.MATRIX[right_x][down_y] == Config.ARENA_BOMB  or self.MATRIX[right_x][down_y] == Config.ARENA_BLOCK or self.MATRIX[right_x][down_y] == Config.ARENA_WALL:
            if not(MOVE_THROUGH_BOMB and self.MATRIX[right_x][down_y] == Config.ARENA_BOMB):
                return False
        return True

    def hasBlockGlobal(self, X_POS, Y_POS):
        left_x = (X_POS) // Config.BLOCK_SIZE + 1
        right_x = (X_POS + Config.PLAYER_SIZE) // Config.BLOCK_SIZE + 1
        up_y = (Y_POS) // Config.BLOCK_SIZE + 1
        down_y = (Y_POS + Config.PLAYER_SIZE) // Config.BLOCK_SIZE + 1

        #if DEBUG and DEBUG_PLAYER == PLAYER:
        #    print([left_x, up_y, self.MATRIX[left_x][up_y]])

        if self.MATRIX[left_x][up_y] != Config.ARENA_VOID:
            return self.MATRIX[left_x][up_y]
        elif self.MATRIX[right_x][up_y] != Config.ARENA_VOID:
            return self.MATRIX[right_x][up_y]
        elif self.MATRIX[left_x][down_y] != Config.ARENA_VOID:
            return self.MATRIX[left_x][down_y]
        elif self.MATRIX[right_x][down_y] != Config.ARENA_VOID:
            return self.MATRIX[right_x][down_y]
        return Config.ARENA_VOID
    
    def hasItem(self, X_POS, Y_POS):
        if self.MATRIX[X_POS][Y_POS] == Config.ARENA_UPGRADE_BOMB or self.MATRIX[X_POS][Y_POS] == Config.ARENA_UPGRADE_SPEED or self.MATRIX[X_POS][Y_POS] == Config.ARENA_UPGRADE_POWER:
            item = self.MATRIX[X_POS][Y_POS]
            self.MATRIX[X_POS][Y_POS] = Config.ARENA_VOID
            return item
        return None

    def hasBlockGlobalDir(self, X_POS, Y_POS, DIR):
        left_x = (X_POS) // Config.BLOCK_SIZE + 1
        right_x = (X_POS + Config.PLAYER_SIZE) // Config.BLOCK_SIZE + 1
        up_y = (Y_POS) // Config.BLOCK_SIZE + 1
        down_y = (Y_POS + Config.PLAYER_SIZE) // Config.BLOCK_SIZE + 1

        if self.MATRIX[left_x][up_y] != Config.ARENA_VOID and ('L' in DIR or 'U' in DIR):
            return self.MATRIX[left_x][up_y]
        elif self.MATRIX[right_x][up_y] != Config.ARENA_VOID and ('R' in DIR or 'U' in DIR):
            return self.MATRIX[right_x][up_y]
        elif self.MATRIX[left_x][down_y] != Config.ARENA_VOID and ('L' in DIR or 'D' in DIR):
            return self.MATRIX[left_x][down_y]
        elif self.MATRIX[right_x][down_y] != Config.ARENA_VOID and ('R' in DIR or 'D' in DIR):
            return self.MATRIX[right_x][down_y]
        return Config.ARENA_VOID

    def hasBlockPosition(self, X_POS, Y_POS):
        X_POS = int(X_POS)
        Y_POS = int(Y_POS)

        if self.MATRIX[X_POS][Y_POS] != Config.ARENA_VOID:
            return  self.MATRIX[X_POS][Y_POS]
        return Config.ARENA_VOID

    def checkBrickDestroy(self, X_POS, Y_POS, bool_destroy):
        if self.MATRIX[X_POS][Y_POS] == Config.ARENA_BLOCK:
            if bool_destroy:
                rand = random.randint(0, 100)
                if rand < 10:
                    self.MATRIX[X_POS][Y_POS] = Config.ARENA_UPGRADE_BOMB
                elif rand < 20:
                    self.MATRIX[X_POS][Y_POS] = Config.ARENA_UPGRADE_POWER
                elif rand < 30:
                    self.MATRIX[X_POS][Y_POS] = Config.ARENA_UPGRADE_SPEED
                else:
                    self.MATRIX[X_POS][Y_POS] = Config.ARENA_VOID                
            return True
        elif self.MATRIX[X_POS][Y_POS] == Config.ARENA_BOMB and self.BOMBS[X_POS][Y_POS] != None:
            self.BOMBS[X_POS][Y_POS].explode()
        else:
            if bool_destroy:
                self.MATRIX[X_POS][Y_POS] = Config.ARENA_VOID
            else:
                self.MATRIX[X_POS][Y_POS] = Config.ARENA_EXPLOSION
        return False
                    
    def check_end(self):
        alive = 4
        for p in self.PLAYERS:
            if p.death:
                alive -= 1
        if alive <= 1 or self.PLAYERS[0].death:
            self.END = True
        if self.END == True:
            for p in self.PLAYERS:
                p.SCORE += self.arena_time()
        if not(self.END_PHASE) and pygame.time.get_ticks() - self.time >= 120000:
            self.END_PHASE = True
            self.END_TIMER = pygame.time.get_ticks()
        if self.END_PHASE and self.END_COUNTER <= self.HEIGHT - 1:
            if pygame.time.get_ticks() - self.END_TIMER >= 5000:
                self.END_TIMER = pygame.time.get_ticks()

                for vector in self.MATRIX:
                    vector[self.END_COUNTER] = Config.ARENA_WALL
                    vector[self.HEIGHT - self.END_COUNTER + 1] = Config.ARENA_WALL
                self.END_COUNTER += 1

    def arena_time(self):
        return (pygame.time.get_ticks() - self.time) / 1000


    def drawn(self):
        ArenaGraph.draw(self.MATRIX, self.WIDTH+2, self.HEIGHT+2)
