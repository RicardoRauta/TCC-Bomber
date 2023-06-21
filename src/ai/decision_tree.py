from src.config import Config
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

    def get_input(self):
        if self.can_die():
            return self.escape_from_bomb()
        if self.opponent_in_area():
            return self.chase_opponent()
        if self.low_time():
            return self.go_to_center()
        return self.collect_items()
    
    def set_arena(self, arena):
        self.arena = arena

# Decision Tree Node

    def can_die(self):
        if self.find_object_in_line_limited(Config.ARENA_BOMB) or self.find_object_in_line_limited(Config.ARENA_EXPLOSION):
            return True
        return False

    def opponent_in_area(self):
        print("a")

    def low_time(self):
        print("a")

# Decision Tree Leaf
    def escape_from_bomb(self):
        state = "Escape from bomb"
        print("a")
    
    def chase_opponent(self):
        state = "Chase opponent"
        print("a")

    def go_to_center(self):
        state = "Go to center"
        print("a")

    def collect_items(self):
        state = "Collect Items"
        print("a")

    def find_object_in_vision(self, object):
        player = self.arena.PLAYERS[self.id]

        y_player = (int) (player.Y_ARENA_POS) - 1
        x_player = (int) (player.X_ARENA_POS) - 1

        if x_player == 0 : x_player = 1
        if x_player == self.arena.WIDTH - 1 : x_player = self.arena.WIDTH - 2
        if y_player == 0 : y_player = 1
        if y_player == self.arena.HEIGHT - 1 : y_player = self.arena.HEIGHT - 2

        for x in range(3):
            auxX = x_player - 1 + x
            for y in range(self.arena.HEIGHT):
                if self.arena.getObjectInPosition(auxX, y) == object:
                        return [True, auxX, y]
        for x in range(self.arena.WIDTH):
            if not(x == x_player - 1 or x == x_player or x == x_player + 1):
                for y in range(3):
                    auxY = y_player - 1 + y
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
                    return [True, x_player-x, y_player]
                elif objectInArena == Config.ARENA_BLOCK or objectInArena == Config.ARENA_WALL:
                    blockedLeft = True
            if not blockedRight:
                objectInArena = self.arena.getObjectInPosition(x_player+x, y_player)
                if objectInArena == object:
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
                    return [True, x_player, y_player+y]
                elif Config.ARENA_BLOCK or objectInArena == Config.ARENA_WALL:
                    blockedUp = True
            if not blockedDown:
                objectInArena = self.arena.getObjectInPosition(x_player, y_player-y)
                if objectInArena == object:
                    return [True, x_player, y_player-y]
                elif Config.ARENA_BLOCK or objectInArena == Config.ARENA_WALL:
                    blockedDown = True
            y += 1

        return [False, 0, 0]