import pygame
from src.config import Config
from src.graph.bomb import BombGraph

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
        self.OWNER.ARENA.MATRIX[self.X_POS][self.Y_POS] = Config.ARENA_BOMB
        self.OWNER.ARENA.BOMBS[self.X_POS][self.Y_POS] = self

    def update(self):
        if not(self.boom):
            BombGraph.draw(self.X_POS,self.Y_POS,self.step,self.OWNER.ARENA.WIDTH, self.OWNER.ARENA.HEIGHT)
            self.step += 1
            if self.step > 15:
                self.step = 0
            if pygame.time.get_ticks() - self.time >= 3000:
                self.step = 0
                self.explode()
        elif self.exist:
            if self.OWNER.ARENA.checkBrickDestroy(self.X_POS, self.Y_POS,self.step==34):
                self.OWNER.SCORE += Config.SCORE_BRICK
            self.checkKill(self.X_POS,self.Y_POS)
            BombGraph.explosion_draw(self.X_POS,self.Y_POS,self.step, "start", 0,self.OWNER.ARENA.WIDTH, self.OWNER.ARENA.HEIGHT)
            self.explosionRec("x+", self.X_POS + 1, self.Y_POS, self.bomb_power)
            self.explosionRec("y-", self.X_POS, self.Y_POS - 1, self.bomb_power)
            self.explosionRec("x-", self.X_POS - 1, self.Y_POS, self.bomb_power)
            self.explosionRec("y+", self.X_POS, self.Y_POS + 1, self.bomb_power)
            self.step += 1
            if self.step >= 35:
                self.exist = False
                self.OWNER.ARENA.MATRIX[self.X_POS][self.Y_POS] = Config.ARENA_VOID
                self.OWNER.BOMBS.remove(self)

    def explosionRec(self, dir, x, y, left):
        if left == 0 or self.OWNER.ARENA.hasBlockPosition(x, y) == Config.ARENA_WALL:
            return
        self.checkKill(x,y)
        if self.OWNER.ARENA.checkBrickDestroy(x,y,self.step==34):
            self.OWNER.SCORE += Config.SCORE_BRICK
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
    
    def checkKill(self, x, y):
        for p in self.OWNER.ARENA.PLAYERS:
            if not p.death and int(p.X_ARENA_POS) == x and int(p.Y_ARENA_POS) == y:
                if p.ID == self.OWNER.ID:
                    self.OWNER.SCORE += Config.SCORE_SELF_KILL
                else:
                    self.OWNER.SCORE += Config.SCORE_KILL_PLAYER
                p.die()

    def explode(self):
        self.boom = True
        self.OWNER.ARENA.BOMBS[self.X_POS][self.Y_POS] = None