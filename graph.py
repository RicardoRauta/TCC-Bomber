import pygame
import os

SCREEN_HEIGHT = 800
SCREEN_WIDTH = 800

BLOCK_SIZE = 32
PLAYER_SIZE = 28
BOMB_SIZE = 30

SCREEN_ON = True

if SCREEN_ON:
    SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

BOMB = [pygame.image.load(os.path.join("Assets/Bomb", "Bomb1.png")),
        pygame.image.load(os.path.join("Assets/Bomb", "Bomb2.png")),
        pygame.image.load(os.path.join("Assets/Bomb", "Bomb3.png")),
        pygame.image.load(os.path.join("Assets/Bomb", "Bomb4.png"))]

BOMB = [pygame.transform.scale(BOMB[0], (BOMB_SIZE, BOMB_SIZE)),
        pygame.transform.scale(BOMB[1], (BOMB_SIZE, BOMB_SIZE)),
        pygame.transform.scale(BOMB[2], (BOMB_SIZE, BOMB_SIZE)),
        pygame.transform.scale(BOMB[3], (BOMB_SIZE, BOMB_SIZE))]

EXPLOSION_START = [pygame.image.load(os.path.join("Assets/Explosion", "ExplosionStart1.png")),
                   pygame.image.load(os.path.join("Assets/Explosion", "ExplosionStart2.png")),
                   pygame.image.load(os.path.join("Assets/Explosion", "ExplosionStart3.png")),
                   pygame.image.load(os.path.join("Assets/Explosion", "ExplosionStart4.png")),
                   pygame.image.load(os.path.join("Assets/Explosion", "ExplosionStart5.png")),
                   pygame.image.load(os.path.join("Assets/Explosion", "ExplosionStart6.png")),
                   pygame.image.load(os.path.join("Assets/Explosion", "ExplosionStart7.png")),
                   pygame.image.load(os.path.join("Assets/Explosion", "ExplosionStart8.png"))]

EXPLOSION_START = [pygame.transform.scale(EXPLOSION_START[0], (BLOCK_SIZE, BLOCK_SIZE)),
                   pygame.transform.scale(EXPLOSION_START[1], (BLOCK_SIZE, BLOCK_SIZE)),
                   pygame.transform.scale(EXPLOSION_START[2], (BLOCK_SIZE, BLOCK_SIZE)),
                   pygame.transform.scale(EXPLOSION_START[3], (BLOCK_SIZE, BLOCK_SIZE)),
                   pygame.transform.scale(EXPLOSION_START[4], (BLOCK_SIZE, BLOCK_SIZE)),
                   pygame.transform.scale(EXPLOSION_START[5], (BLOCK_SIZE, BLOCK_SIZE)),
                   pygame.transform.scale(EXPLOSION_START[6], (BLOCK_SIZE, BLOCK_SIZE)),
                   pygame.transform.scale(EXPLOSION_START[7], (BLOCK_SIZE, BLOCK_SIZE))]

EXPLOSION_MIDDLE = [pygame.image.load(os.path.join("Assets/Explosion", "ExplosionMiddle1.png")),
                    pygame.image.load(os.path.join("Assets/Explosion", "ExplosionMiddle2.png")),
                    pygame.image.load(os.path.join("Assets/Explosion", "ExplosionMiddle3.png")),
                    pygame.image.load(os.path.join("Assets/Explosion", "ExplosionMiddle4.png")),
                    pygame.image.load(os.path.join("Assets/Explosion", "ExplosionMiddle5.png")),
                    pygame.image.load(os.path.join("Assets/Explosion", "ExplosionMiddle6.png")),
                    pygame.image.load(os.path.join("Assets/Explosion", "ExplosionMiddle7.png")),
                    pygame.image.load(os.path.join("Assets/Explosion", "ExplosionMiddle8.png"))]

EXPLOSION_MIDDLE = [pygame.transform.scale(EXPLOSION_MIDDLE[0], (BLOCK_SIZE, BLOCK_SIZE)),
                    pygame.transform.scale(EXPLOSION_MIDDLE[1], (BLOCK_SIZE, BLOCK_SIZE)),
                    pygame.transform.scale(EXPLOSION_MIDDLE[2], (BLOCK_SIZE, BLOCK_SIZE)),
                    pygame.transform.scale(EXPLOSION_MIDDLE[3], (BLOCK_SIZE, BLOCK_SIZE)),
                    pygame.transform.scale(EXPLOSION_MIDDLE[4], (BLOCK_SIZE, BLOCK_SIZE)),
                    pygame.transform.scale(EXPLOSION_MIDDLE[5], (BLOCK_SIZE, BLOCK_SIZE)),
                    pygame.transform.scale(EXPLOSION_MIDDLE[6], (BLOCK_SIZE, BLOCK_SIZE)),
                    pygame.transform.scale(EXPLOSION_MIDDLE[7], (BLOCK_SIZE, BLOCK_SIZE))]

EXPLOSION_END = [pygame.image.load(os.path.join("Assets/Explosion", "ExplosionEnd1.png")),
                 pygame.image.load(os.path.join("Assets/Explosion", "ExplosionEnd2.png")),
                 pygame.image.load(os.path.join("Assets/Explosion", "ExplosionEnd3.png")),
                 pygame.image.load(os.path.join("Assets/Explosion", "ExplosionEnd4.png")),
                 pygame.image.load(os.path.join("Assets/Explosion", "ExplosionEnd5.png")),
                 pygame.image.load(os.path.join("Assets/Explosion", "ExplosionEnd6.png")),
                 pygame.image.load(os.path.join("Assets/Explosion", "ExplosionEnd7.png")),
                 pygame.image.load(os.path.join("Assets/Explosion", "ExplosionEnd8.png"))]

EXPLOSION_END = [pygame.transform.scale(EXPLOSION_END[0], (BLOCK_SIZE, BLOCK_SIZE)),
                 pygame.transform.scale(EXPLOSION_END[1], (BLOCK_SIZE, BLOCK_SIZE)),
                 pygame.transform.scale(EXPLOSION_END[2], (BLOCK_SIZE, BLOCK_SIZE)),
                 pygame.transform.scale(EXPLOSION_END[3], (BLOCK_SIZE, BLOCK_SIZE)),
                 pygame.transform.scale(EXPLOSION_END[4], (BLOCK_SIZE, BLOCK_SIZE)),
                 pygame.transform.scale(EXPLOSION_END[5], (BLOCK_SIZE, BLOCK_SIZE)),
                 pygame.transform.scale(EXPLOSION_END[6], (BLOCK_SIZE, BLOCK_SIZE)),
                 pygame.transform.scale(EXPLOSION_END[7], (BLOCK_SIZE, BLOCK_SIZE))]

ITEM_BLAST_RADIUS = [pygame.image.load(os.path.join("Assets/Item", "ItemBlastRadius.png"))]

ITEM_BLAST_RADIUS = [pygame.transform.scale(ITEM_BLAST_RADIUS[0], (BLOCK_SIZE, BLOCK_SIZE))]

ITEM_EXTRA_BOMB = [pygame.image.load(os.path.join("Assets/Item", "ItemExtraBomb.png"))]

ITEM_EXTRA_BOMB = [pygame.transform.scale(ITEM_EXTRA_BOMB[0], (BLOCK_SIZE, BLOCK_SIZE))]

ITEM_SPEED_INCREASE = [pygame.image.load(os.path.join("Assets/Item", "ItemSpeedIncrease.png"))]

ITEM_SPEED_INCREASE = [pygame.transform.scale(ITEM_SPEED_INCREASE[0], (BLOCK_SIZE, BLOCK_SIZE))]

PLAYER_BLACK_DEATH = [pygame.image.load(os.path.join("Assets/Player", "PlayerBlackDeath1.png")),
                      pygame.image.load(os.path.join("Assets/Player", "PlayerBlackDeath2.png")),
                      pygame.image.load(os.path.join("Assets/Player", "PlayerBlackDeath3.png")),
                      pygame.image.load(os.path.join("Assets/Player", "PlayerBlackDeath4.png")),
                      pygame.image.load(os.path.join("Assets/Player", "PlayerBlackDeath5.png")),
                      pygame.image.load(os.path.join("Assets/Player", "PlayerBlackDeath6.png"))]

PLAYER_BLACK_DEATH = [pygame.transform.scale(PLAYER_BLACK_DEATH[0], (PLAYER_SIZE, PLAYER_SIZE)),
                      pygame.transform.scale(PLAYER_BLACK_DEATH[1], (PLAYER_SIZE, PLAYER_SIZE)),
                      pygame.transform.scale(PLAYER_BLACK_DEATH[2], (PLAYER_SIZE, PLAYER_SIZE)),
                      pygame.transform.scale(PLAYER_BLACK_DEATH[3], (PLAYER_SIZE, PLAYER_SIZE)),
                      pygame.transform.scale(PLAYER_BLACK_DEATH[4], (PLAYER_SIZE, PLAYER_SIZE)),
                      pygame.transform.scale(PLAYER_BLACK_DEATH[5], (PLAYER_SIZE, PLAYER_SIZE))]

PLAYER_BLACK_WALK_UP = [pygame.image.load(os.path.join("Assets/Player", "PlayerBlackWalkUp1.png")),
                        pygame.image.load(os.path.join("Assets/Player", "PlayerBlackWalkUp2.png")),
                        pygame.image.load(os.path.join("Assets/Player", "PlayerBlackWalkUp3.png")),
                        pygame.image.load(os.path.join("Assets/Player", "PlayerBlackWalkUp4.png"))]

PLAYER_BLACK_WALK_UP = [pygame.transform.scale(PLAYER_BLACK_WALK_UP[0], (PLAYER_SIZE, PLAYER_SIZE)),
                        pygame.transform.scale(PLAYER_BLACK_WALK_UP[1], (PLAYER_SIZE, PLAYER_SIZE)),
                        pygame.transform.scale(PLAYER_BLACK_WALK_UP[2], (PLAYER_SIZE, PLAYER_SIZE)),
                        pygame.transform.scale(PLAYER_BLACK_WALK_UP[3], (PLAYER_SIZE, PLAYER_SIZE))]

PLAYER_BLACK_WALK_DOWN = [pygame.image.load(os.path.join("Assets/Player", "PlayerBlackWalkDown1.png")),
                          pygame.image.load(os.path.join("Assets/Player", "PlayerBlackWalkDown2.png")),
                          pygame.image.load(os.path.join("Assets/Player", "PlayerBlackWalkDown3.png")),
                          pygame.image.load(os.path.join("Assets/Player", "PlayerBlackWalkDown4.png"))]

PLAYER_BLACK_WALK_DOWN = [pygame.transform.scale(PLAYER_BLACK_WALK_DOWN[0], (PLAYER_SIZE, PLAYER_SIZE)),
                          pygame.transform.scale(PLAYER_BLACK_WALK_DOWN[1], (PLAYER_SIZE, PLAYER_SIZE)),
                          pygame.transform.scale(PLAYER_BLACK_WALK_DOWN[2], (PLAYER_SIZE, PLAYER_SIZE)),
                          pygame.transform.scale(PLAYER_BLACK_WALK_DOWN[3], (PLAYER_SIZE, PLAYER_SIZE))]

PLAYER_BLACK_WALK_LEFT = [pygame.image.load(os.path.join("Assets/Player", "PlayerBlackWalkLeft1.png")),
                          pygame.image.load(os.path.join("Assets/Player", "PlayerBlackWalkLeft2.png")),
                          pygame.image.load(os.path.join("Assets/Player", "PlayerBlackWalkLeft3.png")),
                          pygame.image.load(os.path.join("Assets/Player", "PlayerBlackWalkLeft4.png"))]

PLAYER_BLACK_WALK_LEFT = [pygame.transform.scale(PLAYER_BLACK_WALK_LEFT[0], (PLAYER_SIZE, PLAYER_SIZE)),
                          pygame.transform.scale(PLAYER_BLACK_WALK_LEFT[1], (PLAYER_SIZE, PLAYER_SIZE)),
                          pygame.transform.scale(PLAYER_BLACK_WALK_LEFT[2], (PLAYER_SIZE, PLAYER_SIZE)),
                          pygame.transform.scale(PLAYER_BLACK_WALK_LEFT[3], (PLAYER_SIZE, PLAYER_SIZE))]

PLAYER_BLACK_WALK_RIGHT = [pygame.image.load(os.path.join("Assets/Player", "PlayerBlackWalkRight1.png")),
                           pygame.image.load(os.path.join("Assets/Player", "PlayerBlackWalkRight2.png")),
                           pygame.image.load(os.path.join("Assets/Player", "PlayerBlackWalkRight3.png")),
                           pygame.image.load(os.path.join("Assets/Player", "PlayerBlackWalkRight4.png"))]

PLAYER_BLACK_WALK_RIGHT = [pygame.transform.scale(PLAYER_BLACK_WALK_RIGHT[0], (PLAYER_SIZE, PLAYER_SIZE)),
                           pygame.transform.scale(PLAYER_BLACK_WALK_RIGHT[1], (PLAYER_SIZE, PLAYER_SIZE)),
                           pygame.transform.scale(PLAYER_BLACK_WALK_RIGHT[2], (PLAYER_SIZE, PLAYER_SIZE)),
                           pygame.transform.scale(PLAYER_BLACK_WALK_RIGHT[3], (PLAYER_SIZE, PLAYER_SIZE))]

PLAYER_BLUE_DEATH = [pygame.image.load(os.path.join("Assets/Player", "PlayerBlueDeath1.png")),
                     pygame.image.load(os.path.join("Assets/Player", "PlayerBlueDeath2.png")),
                     pygame.image.load(os.path.join("Assets/Player", "PlayerBlueDeath3.png")),
                     pygame.image.load(os.path.join("Assets/Player", "PlayerBlueDeath4.png")),
                     pygame.image.load(os.path.join("Assets/Player", "PlayerBlueDeath5.png")),
                     pygame.image.load(os.path.join("Assets/Player", "PlayerBlueDeath6.png"))]

PLAYER_BLUE_DEATH = [pygame.transform.scale(PLAYER_BLUE_DEATH[0], (PLAYER_SIZE, PLAYER_SIZE)),
                     pygame.transform.scale(PLAYER_BLUE_DEATH[1], (PLAYER_SIZE, PLAYER_SIZE)),
                     pygame.transform.scale(PLAYER_BLUE_DEATH[2], (PLAYER_SIZE, PLAYER_SIZE)),
                     pygame.transform.scale(PLAYER_BLUE_DEATH[3], (PLAYER_SIZE, PLAYER_SIZE)),
                     pygame.transform.scale(PLAYER_BLUE_DEATH[4], (PLAYER_SIZE, PLAYER_SIZE)),
                     pygame.transform.scale(PLAYER_BLUE_DEATH[5], (PLAYER_SIZE, PLAYER_SIZE))]

PLAYER_BLUE_WALK_UP = [pygame.image.load(os.path.join("Assets/Player", "PlayerBlueWalkUp1.png")),
                       pygame.image.load(os.path.join("Assets/Player", "PlayerBlueWalkUp2.png")),
                       pygame.image.load(os.path.join("Assets/Player", "PlayerBlueWalkUp3.png")),
                       pygame.image.load(os.path.join("Assets/Player", "PlayerBlueWalkUp4.png"))]

PLAYER_BLUE_WALK_UP = [pygame.transform.scale(PLAYER_BLUE_WALK_UP[0], (PLAYER_SIZE, PLAYER_SIZE)),
                       pygame.transform.scale(PLAYER_BLUE_WALK_UP[1], (PLAYER_SIZE, PLAYER_SIZE)),
                       pygame.transform.scale(PLAYER_BLUE_WALK_UP[2], (PLAYER_SIZE, PLAYER_SIZE)),
                       pygame.transform.scale(PLAYER_BLUE_WALK_UP[3], (PLAYER_SIZE, PLAYER_SIZE))]

PLAYER_BLUE_WALK_DOWN = [pygame.image.load(os.path.join("Assets/Player", "PlayerBlueWalkDown1.png")),
                         pygame.image.load(os.path.join("Assets/Player", "PlayerBlueWalkDown2.png")),
                         pygame.image.load(os.path.join("Assets/Player", "PlayerBlueWalkDown3.png")),
                         pygame.image.load(os.path.join("Assets/Player", "PlayerBlueWalkDown4.png"))]

PLAYER_BLUE_WALK_DOWN = [pygame.transform.scale(PLAYER_BLUE_WALK_DOWN[0], (PLAYER_SIZE, PLAYER_SIZE)),
                         pygame.transform.scale(PLAYER_BLUE_WALK_DOWN[1], (PLAYER_SIZE, PLAYER_SIZE)),
                         pygame.transform.scale(PLAYER_BLUE_WALK_DOWN[2], (PLAYER_SIZE, PLAYER_SIZE)),
                         pygame.transform.scale(PLAYER_BLUE_WALK_DOWN[3], (PLAYER_SIZE, PLAYER_SIZE))]

PLAYER_BLUE_WALK_LEFT = [pygame.image.load(os.path.join("Assets/Player", "PlayerBlueWalkLeft1.png")),
                         pygame.image.load(os.path.join("Assets/Player", "PlayerBlueWalkLeft2.png")),
                         pygame.image.load(os.path.join("Assets/Player", "PlayerBlueWalkLeft3.png")),
                         pygame.image.load(os.path.join("Assets/Player", "PlayerBlueWalkLeft4.png"))]

PLAYER_BLUE_WALK_LEFT = [pygame.transform.scale(PLAYER_BLUE_WALK_LEFT[0], (PLAYER_SIZE, PLAYER_SIZE)),
                         pygame.transform.scale(PLAYER_BLUE_WALK_LEFT[1], (PLAYER_SIZE, PLAYER_SIZE)),
                         pygame.transform.scale(PLAYER_BLUE_WALK_LEFT[2], (PLAYER_SIZE, PLAYER_SIZE)),
                         pygame.transform.scale(PLAYER_BLUE_WALK_LEFT[3], (PLAYER_SIZE, PLAYER_SIZE))]

PLAYER_BLUE_WALK_RIGHT = [pygame.image.load(os.path.join("Assets/Player", "PlayerBlueWalkRight1.png")),
                          pygame.image.load(os.path.join("Assets/Player", "PlayerBlueWalkRight2.png")),
                          pygame.image.load(os.path.join("Assets/Player", "PlayerBlueWalkRight3.png")),
                          pygame.image.load(os.path.join("Assets/Player", "PlayerBlueWalkRight4.png"))]

PLAYER_BLUE_WALK_RIGHT = [pygame.transform.scale(PLAYER_BLUE_WALK_RIGHT[0], (PLAYER_SIZE, PLAYER_SIZE)),
                          pygame.transform.scale(PLAYER_BLUE_WALK_RIGHT[1], (PLAYER_SIZE, PLAYER_SIZE)),
                          pygame.transform.scale(PLAYER_BLUE_WALK_RIGHT[2], (PLAYER_SIZE, PLAYER_SIZE)),
                          pygame.transform.scale(PLAYER_BLUE_WALK_RIGHT[3], (PLAYER_SIZE, PLAYER_SIZE))]

PLAYER_RED_DEATH = [pygame.image.load(os.path.join("Assets/Player", "PlayerRedDeath1.png")),
                    pygame.image.load(os.path.join("Assets/Player", "PlayerRedDeath2.png")),
                    pygame.image.load(os.path.join("Assets/Player", "PlayerRedDeath3.png")),
                    pygame.image.load(os.path.join("Assets/Player", "PlayerRedDeath4.png")),
                    pygame.image.load(os.path.join("Assets/Player", "PlayerRedDeath5.png")),
                    pygame.image.load(os.path.join("Assets/Player", "PlayerRedDeath6.png"))]

PLAYER_RED_DEATH = [pygame.transform.scale(PLAYER_RED_DEATH[0], (PLAYER_SIZE, PLAYER_SIZE)),
                    pygame.transform.scale(PLAYER_RED_DEATH[1], (PLAYER_SIZE, PLAYER_SIZE)),
                    pygame.transform.scale(PLAYER_RED_DEATH[2], (PLAYER_SIZE, PLAYER_SIZE)),
                    pygame.transform.scale(PLAYER_RED_DEATH[3], (PLAYER_SIZE, PLAYER_SIZE)),
                    pygame.transform.scale(PLAYER_RED_DEATH[4], (PLAYER_SIZE, PLAYER_SIZE)),
                    pygame.transform.scale(PLAYER_RED_DEATH[5], (PLAYER_SIZE, PLAYER_SIZE))]

PLAYER_RED_WALK_UP = [pygame.image.load(os.path.join("Assets/Player", "PlayerRedWalkUp1.png")),
                      pygame.image.load(os.path.join("Assets/Player", "PlayerRedWalkUp2.png")),
                      pygame.image.load(os.path.join("Assets/Player", "PlayerRedWalkUp3.png")),
                      pygame.image.load(os.path.join("Assets/Player", "PlayerRedWalkUp4.png"))]

PLAYER_RED_WALK_UP = [pygame.transform.scale(PLAYER_RED_WALK_UP[0], (PLAYER_SIZE, PLAYER_SIZE)),
                      pygame.transform.scale(PLAYER_RED_WALK_UP[1], (PLAYER_SIZE, PLAYER_SIZE)),
                      pygame.transform.scale(PLAYER_RED_WALK_UP[2], (PLAYER_SIZE, PLAYER_SIZE)),
                      pygame.transform.scale(PLAYER_RED_WALK_UP[3], (PLAYER_SIZE, PLAYER_SIZE))]

PLAYER_RED_WALK_DOWN = [pygame.image.load(os.path.join("Assets/Player", "PlayerRedWalkDown1.png")),
                        pygame.image.load(os.path.join("Assets/Player", "PlayerRedWalkDown2.png")),
                        pygame.image.load(os.path.join("Assets/Player", "PlayerRedWalkDown3.png")),
                        pygame.image.load(os.path.join("Assets/Player", "PlayerRedWalkDown4.png"))]

PLAYER_RED_WALK_DOWN = [pygame.transform.scale(PLAYER_RED_WALK_DOWN[0], (PLAYER_SIZE, PLAYER_SIZE)),
                        pygame.transform.scale(PLAYER_RED_WALK_DOWN[1], (PLAYER_SIZE, PLAYER_SIZE)),
                        pygame.transform.scale(PLAYER_RED_WALK_DOWN[2], (PLAYER_SIZE, PLAYER_SIZE)),
                        pygame.transform.scale(PLAYER_RED_WALK_DOWN[3], (PLAYER_SIZE, PLAYER_SIZE))]

PLAYER_RED_WALK_LEFT = [pygame.image.load(os.path.join("Assets/Player", "PlayerRedWalkLeft1.png")),
                        pygame.image.load(os.path.join("Assets/Player", "PlayerRedWalkLeft2.png")),
                        pygame.image.load(os.path.join("Assets/Player", "PlayerRedWalkLeft3.png")),
                        pygame.image.load(os.path.join("Assets/Player", "PlayerRedWalkLeft4.png"))]

PLAYER_RED_WALK_LEFT = [pygame.transform.scale(PLAYER_RED_WALK_LEFT[0], (PLAYER_SIZE, PLAYER_SIZE)),
                        pygame.transform.scale(PLAYER_RED_WALK_LEFT[1], (PLAYER_SIZE, PLAYER_SIZE)),
                        pygame.transform.scale(PLAYER_RED_WALK_LEFT[2], (PLAYER_SIZE, PLAYER_SIZE)),
                        pygame.transform.scale(PLAYER_RED_WALK_LEFT[3], (PLAYER_SIZE, PLAYER_SIZE))]

PLAYER_RED_WALK_RIGHT = [pygame.image.load(os.path.join("Assets/Player", "PlayerRedWalkRight1.png")),
                         pygame.image.load(os.path.join("Assets/Player", "PlayerRedWalkRight2.png")),
                         pygame.image.load(os.path.join("Assets/Player", "PlayerRedWalkRight3.png")),
                         pygame.image.load(os.path.join("Assets/Player", "PlayerRedWalkRight4.png"))]

PLAYER_RED_WALK_RIGHT = [pygame.transform.scale(PLAYER_RED_WALK_RIGHT[0], (PLAYER_SIZE, PLAYER_SIZE)),
                         pygame.transform.scale(PLAYER_RED_WALK_RIGHT[1], (PLAYER_SIZE, PLAYER_SIZE)),
                         pygame.transform.scale(PLAYER_RED_WALK_RIGHT[2], (PLAYER_SIZE, PLAYER_SIZE)),
                         pygame.transform.scale(PLAYER_RED_WALK_RIGHT[3], (PLAYER_SIZE, PLAYER_SIZE))]

PLAYER_WHITE_DEATH = [pygame.image.load(os.path.join("Assets/Player", "PlayerWhiteDeath1.png")),
                      pygame.image.load(os.path.join("Assets/Player", "PlayerWhiteDeath2.png")),
                      pygame.image.load(os.path.join("Assets/Player", "PlayerWhiteDeath3.png")),
                      pygame.image.load(os.path.join("Assets/Player", "PlayerWhiteDeath4.png")),
                      pygame.image.load(os.path.join("Assets/Player", "PlayerWhiteDeath5.png")),
                      pygame.image.load(os.path.join("Assets/Player", "PlayerWhiteDeath6.png"))]

PLAYER_WHITE_DEATH = [pygame.transform.scale(PLAYER_WHITE_DEATH[0], (PLAYER_SIZE, PLAYER_SIZE)),
                      pygame.transform.scale(PLAYER_WHITE_DEATH[1], (PLAYER_SIZE, PLAYER_SIZE)),
                      pygame.transform.scale(PLAYER_WHITE_DEATH[2], (PLAYER_SIZE, PLAYER_SIZE)),
                      pygame.transform.scale(PLAYER_WHITE_DEATH[3], (PLAYER_SIZE, PLAYER_SIZE)),
                      pygame.transform.scale(PLAYER_WHITE_DEATH[4], (PLAYER_SIZE, PLAYER_SIZE)),
                      pygame.transform.scale(PLAYER_WHITE_DEATH[5], (PLAYER_SIZE, PLAYER_SIZE))]

PLAYER_WHITE_WALK_UP = [pygame.image.load(os.path.join("Assets/Player", "PlayerWhiteWalkUp1.png")),
                        pygame.image.load(os.path.join("Assets/Player", "PlayerWhiteWalkUp2.png")),
                        pygame.image.load(os.path.join("Assets/Player", "PlayerWhiteWalkUp3.png")),
                        pygame.image.load(os.path.join("Assets/Player", "PlayerWhiteWalkUp4.png"))]

PLAYER_WHITE_WALK_UP = [pygame.transform.scale(PLAYER_WHITE_WALK_UP[0], (PLAYER_SIZE, PLAYER_SIZE)),
                        pygame.transform.scale(PLAYER_WHITE_WALK_UP[1], (PLAYER_SIZE, PLAYER_SIZE)),
                        pygame.transform.scale(PLAYER_WHITE_WALK_UP[2], (PLAYER_SIZE, PLAYER_SIZE)),
                        pygame.transform.scale(PLAYER_WHITE_WALK_UP[3], (PLAYER_SIZE, PLAYER_SIZE))]

PLAYER_WHITE_WALK_DOWN = [pygame.image.load(os.path.join("Assets/Player", "PlayerWhiteWalkDown1.png")),
                          pygame.image.load(os.path.join("Assets/Player", "PlayerWhiteWalkDown2.png")),
                          pygame.image.load(os.path.join("Assets/Player", "PlayerWhiteWalkDown3.png")),
                          pygame.image.load(os.path.join("Assets/Player", "PlayerWhiteWalkDown4.png"))]

PLAYER_WHITE_WALK_DOWN = [pygame.transform.scale(PLAYER_WHITE_WALK_DOWN[0], (PLAYER_SIZE, PLAYER_SIZE)),
                          pygame.transform.scale(PLAYER_WHITE_WALK_DOWN[1], (PLAYER_SIZE, PLAYER_SIZE)),
                          pygame.transform.scale(PLAYER_WHITE_WALK_DOWN[2], (PLAYER_SIZE, PLAYER_SIZE)),
                          pygame.transform.scale(PLAYER_WHITE_WALK_DOWN[3], (PLAYER_SIZE, PLAYER_SIZE))]

PLAYER_WHITE_WALK_LEFT = [pygame.image.load(os.path.join("Assets/Player", "PlayerWhiteWalkLeft1.png")),
                          pygame.image.load(os.path.join("Assets/Player", "PlayerWhiteWalkLeft2.png")),
                          pygame.image.load(os.path.join("Assets/Player", "PlayerWhiteWalkLeft3.png")),
                          pygame.image.load(os.path.join("Assets/Player", "PlayerWhiteWalkLeft4.png"))]

PLAYER_WHITE_WALK_LEFT = [pygame.transform.scale(PLAYER_WHITE_WALK_LEFT[0], (PLAYER_SIZE, PLAYER_SIZE)),
                          pygame.transform.scale(PLAYER_WHITE_WALK_LEFT[1], (PLAYER_SIZE, PLAYER_SIZE)),
                          pygame.transform.scale(PLAYER_WHITE_WALK_LEFT[2], (PLAYER_SIZE, PLAYER_SIZE)),
                          pygame.transform.scale(PLAYER_WHITE_WALK_LEFT[3], (PLAYER_SIZE, PLAYER_SIZE))]

PLAYER_WHITE_WALK_RIGHT = [pygame.image.load(os.path.join("Assets/Player", "PlayerWhiteWalkRight1.png")),
                           pygame.image.load(os.path.join("Assets/Player", "PlayerWhiteWalkRight2.png")),
                           pygame.image.load(os.path.join("Assets/Player", "PlayerWhiteWalkRight3.png")),
                           pygame.image.load(os.path.join("Assets/Player", "PlayerWhiteWalkRight4.png"))]

PLAYER_WHITE_WALK_RIGHT = [pygame.transform.scale(PLAYER_WHITE_WALK_RIGHT[0], (PLAYER_SIZE, PLAYER_SIZE)),
                           pygame.transform.scale(PLAYER_WHITE_WALK_RIGHT[1], (PLAYER_SIZE, PLAYER_SIZE)),
                           pygame.transform.scale(PLAYER_WHITE_WALK_RIGHT[2], (PLAYER_SIZE, PLAYER_SIZE)),
                           pygame.transform.scale(PLAYER_WHITE_WALK_RIGHT[3], (PLAYER_SIZE, PLAYER_SIZE))]

BLOCK = [pygame.image.load(os.path.join("Assets/Terrain", "Block.png"))]

BLOCK = [pygame.transform.scale(BLOCK[0], (BLOCK_SIZE, BLOCK_SIZE))]

BRICK = [pygame.image.load(os.path.join("Assets/Terrain", "Brick.png"))]

BRICK = [pygame.transform.scale(BRICK[0], (BLOCK_SIZE, BLOCK_SIZE))]

BRICK_DESTROY = [pygame.image.load(os.path.join("Assets/Terrain", "BrickDestroy1.png")),
                 pygame.image.load(os.path.join("Assets/Terrain", "BrickDestroy2.png")),
                 pygame.image.load(os.path.join("Assets/Terrain", "BrickDestroy3.png")),
                 pygame.image.load(os.path.join("Assets/Terrain", "BrickDestroy4.png")),
                 pygame.image.load(os.path.join("Assets/Terrain", "BrickDestroy5.png")),
                 pygame.image.load(os.path.join("Assets/Terrain", "BrickDestroy6.png"))]

BRICK_DESTROY = [pygame.transform.scale(BRICK_DESTROY[0], (BLOCK_SIZE, BLOCK_SIZE)),
                 pygame.transform.scale(BRICK_DESTROY[1], (BLOCK_SIZE, BLOCK_SIZE)),
                 pygame.transform.scale(BRICK_DESTROY[2], (BLOCK_SIZE, BLOCK_SIZE)),
                 pygame.transform.scale(BRICK_DESTROY[3], (BLOCK_SIZE, BLOCK_SIZE)),
                 pygame.transform.scale(BRICK_DESTROY[4], (BLOCK_SIZE, BLOCK_SIZE)),
                 pygame.transform.scale(BRICK_DESTROY[5], (BLOCK_SIZE, BLOCK_SIZE))]

GROUND = [pygame.image.load(os.path.join("Assets/Terrain", "Ground.png"))]

GROUND = [pygame.transform.scale(GROUND[0], (BLOCK_SIZE, BLOCK_SIZE))]

GROUND_SHADOW = [pygame.image.load(os.path.join("Assets/Terrain", "GroundShadow.png"))]

GROUND_SHADOW = [pygame.transform.scale(GROUND_SHADOW[0], (BLOCK_SIZE, BLOCK_SIZE))]

def init_graph():
    SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    return SCREEN

class PlayerGraph:
    X_POS = 0
    Y_POS = 0
    
    def __init__(self, id, x, y):
        if id == 0:
            self.walk_up_img = PLAYER_WHITE_WALK_UP
            self.walk_down_img = PLAYER_WHITE_WALK_DOWN
            self.walk_left_img = PLAYER_WHITE_WALK_LEFT
            self.walk_right_img = PLAYER_WHITE_WALK_RIGHT
            self.death_img = PLAYER_WHITE_DEATH
        elif id == 1:
            self.walk_up_img = PLAYER_BLACK_WALK_UP
            self.walk_down_img = PLAYER_BLACK_WALK_DOWN
            self.walk_left_img = PLAYER_BLACK_WALK_LEFT
            self.walk_right_img = PLAYER_BLACK_WALK_RIGHT
            self.death_img = PLAYER_BLACK_DEATH
        elif id == 2:
            self.walk_up_img = PLAYER_BLUE_WALK_UP
            self.walk_down_img = PLAYER_BLUE_WALK_DOWN
            self.walk_left_img = PLAYER_BLUE_WALK_LEFT
            self.walk_right_img = PLAYER_BLUE_WALK_RIGHT
            self.death_img = PLAYER_BLUE_DEATH
        elif id == 3:
            self.walk_up_img = PLAYER_RED_WALK_UP
            self.walk_down_img = PLAYER_RED_WALK_DOWN
            self.walk_left_img = PLAYER_RED_WALK_LEFT
            self.walk_right_img = PLAYER_RED_WALK_RIGHT
            self.death_img = PLAYER_RED_DEATH

        self.is_death = False
        self.death_step = 0

        self.step_index = 0
        self.image = self.walk_down_img[0]
        self.player_rect = self.image.get_rect()
        self.X_POS = x
        self.Y_POS = y

    def update(self, userInput, X_POS, Y_POS):
        if self.is_death:
            if self.death_step < 36:
                self.death()
            return
        
        if self.step_index >= 16:
            self.step_index = 0

        if userInput == "K_UP":
            self.image = self.walk_up_img
        elif userInput == "K_DOWN":
            self.image = self.walk_down_img
        elif userInput == "K_LEFT":
            self.image = self.walk_left_img
        elif userInput == "K_RIGHT":
            self.image = self.walk_right_img
        
        if not(self.X_POS == X_POS) or not(self.Y_POS == Y_POS):
            self.walk()

        self.X_POS = X_POS
        self.Y_POS = Y_POS

    def walk(self):
        self.image = self.image[self.step_index // 4]
        self.player_rect = self.image.get_rect()
        self.player_rect.x = self.X_POS
        self.player_rect.y = self.Y_POS
        self.step_index += 1

    def death(self):
        self.image = self.image[self.death_step // 6]
        self.player_rect = self.image.get_rect()
        self.player_rect.x = self.X_POS
        self.player_rect.y = self.Y_POS
        self.death_step += 1

    def draw(self, width, height):
        offsetX = (SCREEN_WIDTH - BLOCK_SIZE * width) / 2
        offsetY = (SCREEN_HEIGHT - BLOCK_SIZE * height) / 2
        SCREEN.blit(self.image, (offsetX+self.X_POS, offsetY+self.Y_POS))

    def getXY(self):
        return (self.player_rect.x, self.player_rect.y)
        

class ArenaGraph:
    
    def draw(matrix, width, height):
        offsetX = (SCREEN_WIDTH - BLOCK_SIZE * width) / 2
        offsetY = (SCREEN_HEIGHT - BLOCK_SIZE * height) / 2
        for i in range(width):
            for j in range(height):
                image = BRICK_DESTROY[5]
                if matrix[i][j] == 'o':
                    image = BLOCK[0]
                elif matrix[i][j] == '*':
                    image = BRICK[0]
                elif matrix[i][j] == '-' or matrix[i][j] == '0':
                    if matrix[i][j-1] == 'o':
                        image = GROUND_SHADOW[0]
                    else:
                        image = GROUND[0]
                SCREEN.blit(image, (offsetX+BLOCK_SIZE*i,offsetY+BLOCK_SIZE*j))

class BombGraph:
    def draw(x, y, step, arena_width, arena_height):
        offsetX = (SCREEN_WIDTH - BLOCK_SIZE * arena_width) / 2
        offsetY = (SCREEN_HEIGHT - BLOCK_SIZE * arena_height) / 2

        bomb_x = BOMB[step//4].get_rect().x
        bomb_y = BOMB[step//4].get_rect().y

        SCREEN.blit(BOMB[step//4], [(x-1) * BLOCK_SIZE + offsetX + bomb_x, (y-1) * BLOCK_SIZE + offsetY + bomb_y])

    def explosion_draw(x, y, step, state, rotate, arena_width, arena_height):
        offsetX = (SCREEN_WIDTH - BLOCK_SIZE * arena_width) / 2
        offsetY = (SCREEN_HEIGHT - BLOCK_SIZE * arena_height) / 2

        if state == "start":
            explosion_x = EXPLOSION_START[step//8].get_rect().x
            explosion_y = EXPLOSION_START[step//8].get_rect().y
            SCREEN.blit(EXPLOSION_START[step//8], [(x-1) * BLOCK_SIZE + offsetX + explosion_x, (y-1) * BLOCK_SIZE + offsetY + explosion_y])
        elif state == "middle":
            exlosion = pygame.transform.rotate(EXPLOSION_MIDDLE[step//8], rotate)
            explosion_x = exlosion.get_rect().x
            explosion_y = exlosion.get_rect().y
            SCREEN.blit(exlosion, [(x-1) * BLOCK_SIZE + offsetX + explosion_x, (y-1) * BLOCK_SIZE + offsetY + explosion_y])
        elif state == "end":
            exlosion = pygame.transform.rotate(EXPLOSION_END[step//8], rotate)
            explosion_x = exlosion.get_rect().x
            explosion_y = exlosion.get_rect().y
            SCREEN.blit(exlosion, [(x-1) * BLOCK_SIZE + offsetX + explosion_x, (y-1) * BLOCK_SIZE + offsetY + explosion_y])
        elif state == "block":
            exlosion = pygame.transform.rotate(BRICK_DESTROY[step//8], rotate)
            explosion_x = exlosion.get_rect().x
            explosion_y = exlosion.get_rect().y
            SCREEN.blit(exlosion, [(x-1) * BLOCK_SIZE + offsetX + explosion_x, (y-1) * BLOCK_SIZE + offsetY + explosion_y])

        
