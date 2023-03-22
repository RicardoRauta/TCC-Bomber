import pygame, os, paths
from src.config import Config
from src.global_state import GlobalState

ITEM_BLAST_RADIUS = [pygame.image.load(os.path.join(paths.ASSETS_DIR, "Item\ItemBlastRadius.png"))]

ITEM_BLAST_RADIUS = [pygame.transform.scale(ITEM_BLAST_RADIUS[0], (Config.BLOCK_SIZE, Config.BLOCK_SIZE))]

ITEM_EXTRA_BOMB = [pygame.image.load(os.path.join(paths.ASSETS_DIR, "Item\ItemExtraBomb.png"))]

ITEM_EXTRA_BOMB = [pygame.transform.scale(ITEM_EXTRA_BOMB[0], (Config.BLOCK_SIZE, Config.BLOCK_SIZE))]

ITEM_SPEED_INCREASE = [pygame.image.load(os.path.join(paths.ASSETS_DIR, "Item\ItemSpeedIncrease.png"))]

ITEM_SPEED_INCREASE = [pygame.transform.scale(ITEM_SPEED_INCREASE[0], (Config.BLOCK_SIZE, Config.BLOCK_SIZE))]

BLOCK = [pygame.image.load(os.path.join(paths.ASSETS_DIR, "Terrain\Block.png"))]

BLOCK = [pygame.transform.scale(BLOCK[0], (Config.BLOCK_SIZE, Config.BLOCK_SIZE))]

BRICK = [pygame.image.load(os.path.join(paths.ASSETS_DIR, "Terrain\Brick.png"))]

BRICK = [pygame.transform.scale(BRICK[0], (Config.BLOCK_SIZE, Config.BLOCK_SIZE))]

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

GROUND = [pygame.image.load(os.path.join(paths.ASSETS_DIR, "Terrain\Ground.png"))]

GROUND = [pygame.transform.scale(GROUND[0], (Config.BLOCK_SIZE, Config.BLOCK_SIZE))]

GROUND_SHADOW = [pygame.image.load(os.path.join(paths.ASSETS_DIR, "Terrain\GroundShadow.png"))]

GROUND_SHADOW = [pygame.transform.scale(GROUND_SHADOW[0], (Config.BLOCK_SIZE, Config.BLOCK_SIZE))]

class ArenaGraph:
    
    def draw(matrix, width, height):
        if not Config.SCREEN_ON:
            return
        offsetX = (Config.SCREEN_WIDTH - Config.BLOCK_SIZE * width) / 2
        offsetY = (Config.SCREEN_HEIGHT - Config.BLOCK_SIZE * height) / 2
        for i in range(width):
            for j in range(height):
                image = BRICK_DESTROY[5]
                if matrix[i][j] == 'o':
                    image = BLOCK[0]
                elif matrix[i][j] == '*':
                    image = BRICK[0]
                elif matrix[i][j] == '-' or matrix[i][j] == '0' or matrix[i][j] == 'x':
                    if matrix[i][j-1] == 'o':
                        image = GROUND_SHADOW[0]
                    else:
                        image = GROUND[0]
                elif matrix[i][j] == 'b':
                    image = ITEM_EXTRA_BOMB[0]
                elif matrix[i][j] == 's':
                    image = ITEM_SPEED_INCREASE[0]
                elif matrix[i][j] == 'p':
                    image = ITEM_BLAST_RADIUS[0]
                GlobalState.SCREEN.blit(image, (offsetX+Config.BLOCK_SIZE*i,offsetY+Config.BLOCK_SIZE*j))