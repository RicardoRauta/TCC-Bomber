import pygame, os, paths
from src.config import Config
from src.global_state import GlobalState

BOMB = [pygame.image.load(os.path.join(paths.ASSETS_DIR, "Bomb\Bomb1.png")),
        pygame.image.load(os.path.join(paths.ASSETS_DIR, "Bomb\Bomb2.png")),
        pygame.image.load(os.path.join(paths.ASSETS_DIR, "Bomb\Bomb3.png")),
        pygame.image.load(os.path.join(paths.ASSETS_DIR, "Bomb\Bomb4.png"))]

BOMB = [pygame.transform.scale(BOMB[0], (Config.BOMB_SIZE, Config.BOMB_SIZE)),
        pygame.transform.scale(BOMB[1], (Config.BOMB_SIZE, Config.BOMB_SIZE)),
        pygame.transform.scale(BOMB[2], (Config.BOMB_SIZE, Config.BOMB_SIZE)),
        pygame.transform.scale(BOMB[3], (Config.BOMB_SIZE, Config.BOMB_SIZE))]

EXPLOSION_START = [pygame.image.load(os.path.join(paths.ASSETS_DIR, "Explosion\ExplosionStart1.png")),
                   pygame.image.load(os.path.join(paths.ASSETS_DIR, "Explosion\ExplosionStart2.png")),
                   pygame.image.load(os.path.join(paths.ASSETS_DIR, "Explosion\ExplosionStart3.png")),
                   pygame.image.load(os.path.join(paths.ASSETS_DIR, "Explosion\ExplosionStart4.png")),
                   pygame.image.load(os.path.join(paths.ASSETS_DIR, "Explosion\ExplosionStart5.png")),
                   pygame.image.load(os.path.join(paths.ASSETS_DIR, "Explosion\ExplosionStart6.png")),
                   pygame.image.load(os.path.join(paths.ASSETS_DIR, "Explosion\ExplosionStart7.png")),
                   pygame.image.load(os.path.join(paths.ASSETS_DIR, "Explosion\ExplosionStart8.png"))]

EXPLOSION_START = [pygame.transform.scale(EXPLOSION_START[0], (Config.BLOCK_SIZE, Config.BLOCK_SIZE)),
                   pygame.transform.scale(EXPLOSION_START[1], (Config.BLOCK_SIZE, Config.BLOCK_SIZE)),
                   pygame.transform.scale(EXPLOSION_START[2], (Config.BLOCK_SIZE, Config.BLOCK_SIZE)),
                   pygame.transform.scale(EXPLOSION_START[3], (Config.BLOCK_SIZE, Config.BLOCK_SIZE)),
                   pygame.transform.scale(EXPLOSION_START[4], (Config.BLOCK_SIZE, Config.BLOCK_SIZE)),
                   pygame.transform.scale(EXPLOSION_START[5], (Config.BLOCK_SIZE, Config.BLOCK_SIZE)),
                   pygame.transform.scale(EXPLOSION_START[6], (Config.BLOCK_SIZE, Config.BLOCK_SIZE)),
                   pygame.transform.scale(EXPLOSION_START[7], (Config.BLOCK_SIZE, Config.BLOCK_SIZE))]

EXPLOSION_MIDDLE = [pygame.image.load(os.path.join(paths.ASSETS_DIR, "Explosion\ExplosionMiddle1.png")),
                    pygame.image.load(os.path.join(paths.ASSETS_DIR, "Explosion\ExplosionMiddle2.png")),
                    pygame.image.load(os.path.join(paths.ASSETS_DIR, "Explosion\ExplosionMiddle3.png")),
                    pygame.image.load(os.path.join(paths.ASSETS_DIR, "Explosion\ExplosionMiddle4.png")),
                    pygame.image.load(os.path.join(paths.ASSETS_DIR, "Explosion\ExplosionMiddle5.png")),
                    pygame.image.load(os.path.join(paths.ASSETS_DIR, "Explosion\ExplosionMiddle6.png")),
                    pygame.image.load(os.path.join(paths.ASSETS_DIR, "Explosion\ExplosionMiddle7.png")),
                    pygame.image.load(os.path.join(paths.ASSETS_DIR, "Explosion\ExplosionMiddle8.png"))]

EXPLOSION_MIDDLE = [pygame.transform.scale(EXPLOSION_MIDDLE[0], (Config.BLOCK_SIZE, Config.BLOCK_SIZE)),
                    pygame.transform.scale(EXPLOSION_MIDDLE[1], (Config.BLOCK_SIZE, Config.BLOCK_SIZE)),
                    pygame.transform.scale(EXPLOSION_MIDDLE[2], (Config.BLOCK_SIZE, Config.BLOCK_SIZE)),
                    pygame.transform.scale(EXPLOSION_MIDDLE[3], (Config.BLOCK_SIZE, Config.BLOCK_SIZE)),
                    pygame.transform.scale(EXPLOSION_MIDDLE[4], (Config.BLOCK_SIZE, Config.BLOCK_SIZE)),
                    pygame.transform.scale(EXPLOSION_MIDDLE[5], (Config.BLOCK_SIZE, Config.BLOCK_SIZE)),
                    pygame.transform.scale(EXPLOSION_MIDDLE[6], (Config.BLOCK_SIZE, Config.BLOCK_SIZE)),
                    pygame.transform.scale(EXPLOSION_MIDDLE[7], (Config.BLOCK_SIZE, Config.BLOCK_SIZE))]

EXPLOSION_END = [pygame.image.load(os.path.join(paths.ASSETS_DIR, "Explosion\ExplosionEnd1.png")),
                 pygame.image.load(os.path.join(paths.ASSETS_DIR, "Explosion\ExplosionEnd2.png")),
                 pygame.image.load(os.path.join(paths.ASSETS_DIR, "Explosion\ExplosionEnd3.png")),
                 pygame.image.load(os.path.join(paths.ASSETS_DIR, "Explosion\ExplosionEnd4.png")),
                 pygame.image.load(os.path.join(paths.ASSETS_DIR, "Explosion\ExplosionEnd5.png")),
                 pygame.image.load(os.path.join(paths.ASSETS_DIR, "Explosion\ExplosionEnd6.png")),
                 pygame.image.load(os.path.join(paths.ASSETS_DIR, "Explosion\ExplosionEnd7.png")),
                 pygame.image.load(os.path.join(paths.ASSETS_DIR, "Explosion\ExplosionEnd8.png"))]

EXPLOSION_END = [pygame.transform.scale(EXPLOSION_END[0], (Config.BLOCK_SIZE, Config.BLOCK_SIZE)),
                 pygame.transform.scale(EXPLOSION_END[1], (Config.BLOCK_SIZE, Config.BLOCK_SIZE)),
                 pygame.transform.scale(EXPLOSION_END[2], (Config.BLOCK_SIZE, Config.BLOCK_SIZE)),
                 pygame.transform.scale(EXPLOSION_END[3], (Config.BLOCK_SIZE, Config.BLOCK_SIZE)),
                 pygame.transform.scale(EXPLOSION_END[4], (Config.BLOCK_SIZE, Config.BLOCK_SIZE)),
                 pygame.transform.scale(EXPLOSION_END[5], (Config.BLOCK_SIZE, Config.BLOCK_SIZE)),
                 pygame.transform.scale(EXPLOSION_END[6], (Config.BLOCK_SIZE, Config.BLOCK_SIZE)),
                 pygame.transform.scale(EXPLOSION_END[7], (Config.BLOCK_SIZE, Config.BLOCK_SIZE))]

BRICK_DESTROY = [pygame.image.load(os.path.join(paths.ASSETS_DIR, "Terrain\BrickDestroy1.png")),
                 pygame.image.load(os.path.join(paths.ASSETS_DIR, "Terrain\BrickDestroy2.png")),
                 pygame.image.load(os.path.join(paths.ASSETS_DIR, "Terrain\BrickDestroy3.png")),
                 pygame.image.load(os.path.join(paths.ASSETS_DIR, "Terrain\BrickDestroy4.png")),
                 pygame.image.load(os.path.join(paths.ASSETS_DIR, "Terrain\BrickDestroy5.png")),
                 pygame.image.load(os.path.join(paths.ASSETS_DIR, "Terrain\BrickDestroy6.png"))]

BRICK_DESTROY = [pygame.transform.scale(BRICK_DESTROY[0], (Config.BLOCK_SIZE, Config.BLOCK_SIZE)),
                 pygame.transform.scale(BRICK_DESTROY[1], (Config.BLOCK_SIZE, Config.BLOCK_SIZE)),
                 pygame.transform.scale(BRICK_DESTROY[2], (Config.BLOCK_SIZE, Config.BLOCK_SIZE)),
                 pygame.transform.scale(BRICK_DESTROY[3], (Config.BLOCK_SIZE, Config.BLOCK_SIZE)),
                 pygame.transform.scale(BRICK_DESTROY[4], (Config.BLOCK_SIZE, Config.BLOCK_SIZE)),
                 pygame.transform.scale(BRICK_DESTROY[5], (Config.BLOCK_SIZE, Config.BLOCK_SIZE))]

class BombGraph:
    def draw(x, y, step, arena_width, arena_height):
        if not Config.SCREEN_ON:
            return
        offsetX = (Config.SCREEN_WIDTH - Config.BLOCK_SIZE * arena_width) / 2
        offsetY = (Config.SCREEN_HEIGHT - Config.BLOCK_SIZE * arena_height) / 2

        bomb_x = BOMB[step//4].get_rect().x
        bomb_y = BOMB[step//4].get_rect().y

        GlobalState.SCREEN.blit(BOMB[step//4], [(x-1) * Config.BLOCK_SIZE + offsetX + bomb_x, (y-1) * Config.BLOCK_SIZE + offsetY + bomb_y])

    def explosion_draw(x, y, step, state, rotate, arena_width, arena_height):
        if not Config.SCREEN_ON:
            return
        offsetX = (Config.SCREEN_WIDTH - Config.BLOCK_SIZE * arena_width) / 2
        offsetY = (Config.SCREEN_HEIGHT - Config.BLOCK_SIZE * arena_height) / 2

        if state == "start":
            explosion_x = EXPLOSION_START[step//8].get_rect().x
            explosion_y = EXPLOSION_START[step//8].get_rect().y
            GlobalState.SCREEN.blit(EXPLOSION_START[step//8], [(x-1) * Config.BLOCK_SIZE + offsetX + explosion_x, (y-1) * Config.BLOCK_SIZE + offsetY + explosion_y])
        elif state == "middle":
            exlosion = pygame.transform.rotate(EXPLOSION_MIDDLE[step//8], rotate)
            explosion_x = exlosion.get_rect().x
            explosion_y = exlosion.get_rect().y
            GlobalState.SCREEN.blit(exlosion, [(x-1) * Config.BLOCK_SIZE + offsetX + explosion_x, (y-1) * Config.BLOCK_SIZE + offsetY + explosion_y])
        elif state == "end":
            exlosion = pygame.transform.rotate(EXPLOSION_END[step//8], rotate)
            explosion_x = exlosion.get_rect().x
            explosion_y = exlosion.get_rect().y
            GlobalState.SCREEN.blit(exlosion, [(x-1) * Config.BLOCK_SIZE + offsetX + explosion_x, (y-1) * Config.BLOCK_SIZE + offsetY + explosion_y])
        elif state == "block":
            exlosion = pygame.transform.rotate(BRICK_DESTROY[step//8], rotate)
            explosion_x = exlosion.get_rect().x
            explosion_y = exlosion.get_rect().y
            GlobalState.SCREEN.blit(exlosion, [(x-1) * Config.BLOCK_SIZE + offsetX + explosion_x, (y-1) * Config.BLOCK_SIZE + offsetY + explosion_y])

        
