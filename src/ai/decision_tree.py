# Esta na área de uma bomba
#   - Sim, fugir
#   - Não, algum oponente esta próximo?
#       - Sim, perseguir
#       - Não, tempo esta acabando?
#           - Sim, ir para o meio
#           - Não, coletar itens

class DecisionTree():
    arena = None

    def get_input(self):
        input = [0,0,0,0]


        return input
    
    def set_arena(self, arena):
        self.arena = arena

# Decision Tree Node

    def can_die(self):
        print("a")

    def opponent_in_area(self):
        print("a")

    def low_time(self):
        print("a")

# Decision Tree Leaf
    def escape_from_bomb(self):
        print("a")
    
    def chase_opponent(self):
        print("a")

    def go_to_center(self):
        print("a")

    def collect_items(self):
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