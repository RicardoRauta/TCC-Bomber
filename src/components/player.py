from src.config import Config
from src.graph.player import PlayerGraph
from src.components.bomb import Bomb

class Player:
    SCORE = 500
    X_POS = 0
    Y_POS = 0
    ID = 0
    MODE = None

    def __init__(self, ID, ARENA, MODE):
        self.ID = ID
        
        self.BOMBS = []
        self.speed = 1
        self.max_bomb = 2
        self.bomb_power = 4
        self.place_bomb = False
        self.death = False
        self.MODE = MODE
        self.ARENA = ARENA
        self.MODE.arena = ARENA
        self.MODE.id = ID

        if ID == 0:
            self.X_POS = 0
            self.Y_POS = 0
        elif ID == 1:
            self.X_POS = Config.BLOCK_SIZE*ARENA.WIDTH - Config.BLOCK_SIZE
            self.Y_POS = 0
        elif ID == 2:
            self.X_POS = 0
            self.Y_POS = Config.BLOCK_SIZE*ARENA.HEIGHT - Config.BLOCK_SIZE
        elif ID == 3:
            self.X_POS = Config.BLOCK_SIZE*ARENA.WIDTH - Config.BLOCK_SIZE
            self.Y_POS = Config.BLOCK_SIZE*ARENA.HEIGHT - Config.BLOCK_SIZE
        self.graph = PlayerGraph(ID, self.X_POS, self.Y_POS)

        self.X_ARENA_POS = self.X_POS // Config.BLOCK_SIZE + 1
        self.Y_ARENA_POS = self.Y_POS // Config.BLOCK_SIZE + 1

    def set_arena(self, ARENA):
        self.ARENA = ARENA
        self.MODE.arena = ARENA

        
    def update(self, dt):
        # inputs[0] - 1 (se move)  0 (fica parado) - movimento
        # inputs[1] - 1 (vertical) 0 (horizontal)  - direção
        # inputs[2] - 1 (positivo) 0 (negativo)    - sentido
        # inputs[3] - 1 (bomba)    0 (nada)        - bomba


        # inputs[0] - 1 mover para cima
        # inputs[1] - 1 mover para baixo
        # inputs[2] - 1 mover para esquerda
        # inputs[3] - 1 mover para direita
        # inputs[4] - 1 soltar bomba

        if self.ARENA.checkDeath(int(self.X_ARENA_POS), int(self.Y_ARENA_POS)):
            self.die()
        
        mov = max(int((dt / 30) / 2), 1)
        #print(mov)

        if not self.death:
            inputs = self.MODE.get_input()
            move = [inputs[3] - inputs[2], inputs[1] - inputs[0]]

            self.X_ARENA_POS = (self.X_POS + Config.PLAYER_SIZE/2) / Config.BLOCK_SIZE + 1
            self.Y_ARENA_POS = (self.Y_POS + Config.PLAYER_SIZE/2) / Config.BLOCK_SIZE + 1

            for k in range(self.speed + mov):

                if self.ARENA.canGoIn(self.X_POS, self.Y_POS + move[1], Config.PLAYER_SIZE, self.X_POS, self.Y_POS):
                        self.Y_POS += move[1]
                if self.ARENA.canGoIn(self.X_POS + move[0], self.Y_POS, Config.PLAYER_SIZE, self.X_POS, self.Y_POS):
                        self.X_POS += move[0]
                
                if move[0] > 0:
                    self.graph.update("K_RIGHT", self.X_POS, self.Y_POS)
                elif move[0] < 0:
                    self.graph.update("K_LEFT", self.X_POS, self.Y_POS)
                elif move[1] < 0:
                    self.graph.update("K_UP", self.X_POS, self.Y_POS)
                elif move[1] > 0:
                    self.graph.update("K_DOWN", self.X_POS, self.Y_POS)

            if inputs[4] == 1 and len(self.BOMBS) < self.max_bomb:
                if self.ARENA.hasBlockPosition(self.X_ARENA_POS, self.Y_ARENA_POS) == Config.ARENA_VOID:
                    self.SCORE += Config.SCORE_BOMB
                    self.BOMBS.append(Bomb(self))
                    self.place_bomb = True
        if self.ARENA.hasBlockGlobal(self.X_POS, self.Y_POS) == Config.ARENA_VOID:
            self.place_bomb = False
        item = self.ARENA.hasItem(int(self.X_ARENA_POS), int(self.Y_ARENA_POS))
        if item != None:
            if item == Config.ARENA_UPGRADE_BOMB:
                self.max_bomb += 1
            elif item == Config.ARENA_UPGRADE_POWER:
                self.bomb_power += 1
            elif item == Config.ARENA_UPGRADE_SPEED:
                self.speed += 1
        for bomb in self.BOMBS:
            bomb.update()
        self.drawn()
    
    def die(self):
        self.graph.is_death = True
        self.death = True
        self.X_ARENA_POS = -1
        self.Y_ARENA_POS = -1

    def drawn(self):
        self.graph.draw(self.ARENA.WIDTH, self.ARENA.HEIGHT)