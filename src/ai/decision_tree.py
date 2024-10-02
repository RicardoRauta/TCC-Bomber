from src.config import Config
from src.ai.human import HumanMode
from src.ai.neural import Neural 
import random
# Esta na área de uma bomba
#   - Sim, fugir
#   - Não, algum oponente esta próximo?
#       - Sim, perseguir
#       - Não, tempo esta acabando?
#           - Sim, ir para o meio
#           - Não, coletar itens

class DecisionTree():
    arena = None
    state = "Idle"
    id = 0

    def get_input(self):
        if self.can_die():
            return self.escape_from_bomb()
        #if self.opponent_in_area()[0]:
        return self.chase_opponent()
        #return self.go_to_target(1+self.arena.WIDTH / 2, 1+self.arena.HEIGHT / 2)
    
    def set_arena(self, arena):
        self.arena = arena

# Decision Tree Node

    def can_die(self):
        here, x, y = self.find_object_in_vision(Config.ARENA_BOMB)
        
        if (not here):
            here, x, y = self.find_object_in_vision(Config.ARENA_EXPLOSION)

        return here

    def opponent_in_area(self):
        player = self.arena.PLAYERS[self.id]
        y_player = (int) (player.Y_ARENA_POS)
        x_player = (int) (player.X_ARENA_POS)

        #for target in self.arena.PLAYERS:
        target = None
        for p in self.arena.PLAYERS:
            if isinstance(p.MODE, Neural) or isinstance(p.MODE, HumanMode):
                target = p

        if target != None and target != player and not target.death:

            y_target = (int) (target.Y_ARENA_POS)
            x_target = (int) (target.X_ARENA_POS)

            if (x_target - x_player < 3 and x_target - x_player > -3):
                return [True, target.X_ARENA_POS, target.Y_ARENA_POS]
            if (y_target - y_player < 3 and y_target - y_player > -3):
                return [True, target.X_ARENA_POS, target.Y_ARENA_POS]
                
        return [False, 0, 0]

# Decision Tree Leaf
    def escape_from_bomb(self):
        state = "Escape from bomb"
        player = self.arena.PLAYERS[self.id]

        here, x, y = self.find_object_in_vision(Config.ARENA_BOMB)
        
        if (not here):
            _, x, y = self.find_object_in_vision(Config.ARENA_EXPLOSION)

        returnValue = [0,0,0,0,0]
        xP = int(player.X_ARENA_POS)
        yP = int(player.Y_ARENA_POS)


        if x > xP:
            returnValue[2] = 1
        elif x < xP:
            returnValue[3] = 1
        if x == xP:
            if x > self.arena.WIDTH / 2:
                returnValue[2] = 1
            elif x < self.arena.WIDTH / 2:
                returnValue[3] = 1

        if y > yP:
            returnValue[0] = 1
        elif y < yP:
            returnValue[1] = 1
        if y == yP:
            if y > self.arena.HEIGHT / 2:
                returnValue[0] = 1
            elif y < self.arena.HEIGHT / 2:
                returnValue[1] = 1
                    
        
        return returnValue
    
    def chase_opponent(self):
        state = "Chase opponent"
        player = self.arena.PLAYERS[self.id]
        xP = player.X_ARENA_POS
        yP = player.Y_ARENA_POS
        _, enemyX, enemyY = self.opponent_in_area()

        returnValue = [0,0,0,0,0]
        if random.random() < 0.05 and (xP - enemyX < 1 and xP - enemyX > -1 and yP - enemyY < 4 and yP - enemyY > -4):
            returnValue[4] = 1
        elif random.random() < 0.05 and (xP - enemyX < 4 and xP - enemyX > -4 and yP - enemyY < 1 and yP - enemyY > -1):
            returnValue[4] = 1
        if random.random() < 0.05 and (xP - enemyX < 1 and xP - enemyX > -1 and yP - enemyY < 3 and yP - enemyY > -3):
            returnValue[4] = 1
        elif random.random() < 0.05 and (xP - enemyX < 3 and xP - enemyX > -3 and yP - enemyY < 1 and yP - enemyY > -1):
            returnValue[4] = 1
        elif (xP - enemyX < 1 and xP - enemyX > -1 and yP - enemyY < 1 and yP - enemyY > -1):
            returnValue[4] = 1
        elif random.random() < 0.3:
            returnValue = self.go_to_target(enemyX + 1, enemyY + 1)
        elif random.random() < 0.3:
            returnValue = self.go_to_target(enemyX + 1, enemyY - 1)
        elif random.random() < 0.3:
            returnValue = self.go_to_target(enemyX - 1, enemyY + 1)
        elif random.random() < 0.3:
            returnValue = self.go_to_target(enemyX - 1, enemyY - 1)
        else:
            returnValue = self.go_to_target(enemyX, enemyY )
        
        return returnValue

    def go_to_target(self, x, y):
        player = self.arena.PLAYERS[self.id]
        xP = player.X_ARENA_POS
        yP = player.Y_ARENA_POS

        returnValue = [0,0,0,0,0]

        if (x > xP):
            returnValue[3] = 1
        if (x < xP):
            returnValue[2] = 1
        if (y > yP):
            returnValue[1] = 1
        if (y < yP):
            returnValue[0] = 1

        return returnValue

    def find_object_in_vision(self, object):
        player = self.arena.PLAYERS[self.id]

        y_player = (int) (player.Y_ARENA_POS)
        x_player = (int) (player.X_ARENA_POS)


        for x in range(3):
            auxX = x_player - 1 + x
            for y in range(self.arena.HEIGHT+2):
                if self.arena.getObjectInPosition(auxX, y) == object:
                        return [True, auxX, y]
        for y in range(3):
            auxY = y_player - 1 + y
            for x in range(self.arena.WIDTH+2):
                if self.arena.getObjectInPosition(x, auxY) == object:
                    return [True, x, auxY]
        return [False, 0, 0]

    def find_object_in_line_limited(self, object):
        player = self.arena.PLAYERS[self.id]

        y_player = (int) (player.Y_ARENA_POS) - 1
        x_player = (int) (player.X_ARENA_POS) - 1

        if x_player == 0 : x_player = 1
        if x_player == self.arena.WIDTH - 1 : x_player = self.arena.WIDTH - 2
        if y_player == 0 : y_player = 1
        if y_player == self.arena.HEIGHT - 1 : y_player = self.arena.HEIGHT - 2

        # Vision X
        blockedRight = False
        blockedLeft = False
        x = 0
        while not blockedLeft or not blockedRight:
            if not blockedLeft:
                objectInArena = self.arena.getObjectInPosition(x_player-x, y_player)
                if objectInArena == object:
                    print("entrou A com obj = " + str(object))
                    return [True, x_player-x, y_player]
                elif objectInArena == Config.ARENA_BLOCK or objectInArena == Config.ARENA_WALL:
                    blockedLeft = True
            if not blockedRight:
                objectInArena = self.arena.getObjectInPosition(x_player+x, y_player)
                if objectInArena == object:
                    print("entrou B com obj = " + str(object))
                    return [True, x_player+x, y_player]
                elif Config.ARENA_BLOCK or objectInArena == Config.ARENA_WALL:
                    blockedRight = True
            x += 1

        # Vision Y
        blockedUp = False
        blockedDown = False
        y = 0
        while not blockedUp or not blockedDown:
            if not blockedUp:
                objectInArena = self.arena.getObjectInPosition(x_player, y_player+y)
                if objectInArena == object:
                    print("entrou C com obj = " + str(object))
                    return [True, x_player, y_player+y]
                elif Config.ARENA_BLOCK or objectInArena == Config.ARENA_WALL:
                    blockedUp = True
            if not blockedDown:
                objectInArena = self.arena.getObjectInPosition(x_player, y_player-y)
                if objectInArena == object:
                    print("entrou D com obj = " + str(object))
                    return [True, x_player, y_player-y]
                elif Config.ARENA_BLOCK or objectInArena == Config.ARENA_WALL:
                    blockedDown = True
            y += 1

        return [False, 0, 0]