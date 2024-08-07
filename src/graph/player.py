import pygame, os, paths
from src.config import Config
from src.global_state import GlobalState

PLAYER_BLACK_DEATH = [pygame.image.load(os.path.join(paths.ASSETS_DIR, "Player\PlayerBlackDeath1.png")),
                      pygame.image.load(os.path.join(paths.ASSETS_DIR, "Player\PlayerBlackDeath2.png")),
                      pygame.image.load(os.path.join(paths.ASSETS_DIR, "Player\PlayerBlackDeath3.png")),
                      pygame.image.load(os.path.join(paths.ASSETS_DIR, "Player\PlayerBlackDeath4.png")),
                      pygame.image.load(os.path.join(paths.ASSETS_DIR, "Player\PlayerBlackDeath5.png")),
                      pygame.image.load(os.path.join(paths.ASSETS_DIR, "Player\PlayerBlackDeath6.png"))]

PLAYER_BLACK_DEATH = [pygame.transform.scale(PLAYER_BLACK_DEATH[0], (Config.PLAYER_SIZE, Config.PLAYER_SIZE)),
                      pygame.transform.scale(PLAYER_BLACK_DEATH[1], (Config.PLAYER_SIZE, Config.PLAYER_SIZE)),
                      pygame.transform.scale(PLAYER_BLACK_DEATH[2], (Config.PLAYER_SIZE, Config.PLAYER_SIZE)),
                      pygame.transform.scale(PLAYER_BLACK_DEATH[3], (Config.PLAYER_SIZE, Config.PLAYER_SIZE)),
                      pygame.transform.scale(PLAYER_BLACK_DEATH[4], (Config.PLAYER_SIZE, Config.PLAYER_SIZE)),
                      pygame.transform.scale(PLAYER_BLACK_DEATH[5], (Config.PLAYER_SIZE, Config.PLAYER_SIZE))]

PLAYER_BLACK_WALK_UP = [pygame.image.load(os.path.join(paths.ASSETS_DIR, "Player\PlayerBlackWalkUp1.png")),
                        pygame.image.load(os.path.join(paths.ASSETS_DIR, "Player\PlayerBlackWalkUp2.png")),
                        pygame.image.load(os.path.join(paths.ASSETS_DIR, "Player\PlayerBlackWalkUp3.png")),
                        pygame.image.load(os.path.join(paths.ASSETS_DIR, "Player\PlayerBlackWalkUp4.png"))]

PLAYER_BLACK_WALK_UP = [pygame.transform.scale(PLAYER_BLACK_WALK_UP[0], (Config.PLAYER_SIZE, Config.PLAYER_SIZE)),
                        pygame.transform.scale(PLAYER_BLACK_WALK_UP[1], (Config.PLAYER_SIZE, Config.PLAYER_SIZE)),
                        pygame.transform.scale(PLAYER_BLACK_WALK_UP[2], (Config.PLAYER_SIZE, Config.PLAYER_SIZE)),
                        pygame.transform.scale(PLAYER_BLACK_WALK_UP[3], (Config.PLAYER_SIZE, Config.PLAYER_SIZE))]

PLAYER_BLACK_WALK_DOWN = [pygame.image.load(os.path.join(paths.ASSETS_DIR, "Player\PlayerBlackWalkDown1.png")),
                          pygame.image.load(os.path.join(paths.ASSETS_DIR, "Player\PlayerBlackWalkDown2.png")),
                          pygame.image.load(os.path.join(paths.ASSETS_DIR, "Player\PlayerBlackWalkDown3.png")),
                          pygame.image.load(os.path.join(paths.ASSETS_DIR, "Player\PlayerBlackWalkDown4.png"))]

PLAYER_BLACK_WALK_DOWN = [pygame.transform.scale(PLAYER_BLACK_WALK_DOWN[0], (Config.PLAYER_SIZE, Config.PLAYER_SIZE)),
                          pygame.transform.scale(PLAYER_BLACK_WALK_DOWN[1], (Config.PLAYER_SIZE, Config.PLAYER_SIZE)),
                          pygame.transform.scale(PLAYER_BLACK_WALK_DOWN[2], (Config.PLAYER_SIZE, Config.PLAYER_SIZE)),
                          pygame.transform.scale(PLAYER_BLACK_WALK_DOWN[3], (Config.PLAYER_SIZE, Config.PLAYER_SIZE))]

PLAYER_BLACK_WALK_LEFT = [pygame.image.load(os.path.join(paths.ASSETS_DIR, "Player\PlayerBlackWalkLeft1.png")),
                          pygame.image.load(os.path.join(paths.ASSETS_DIR, "Player\PlayerBlackWalkLeft2.png")),
                          pygame.image.load(os.path.join(paths.ASSETS_DIR, "Player\PlayerBlackWalkLeft3.png")),
                          pygame.image.load(os.path.join(paths.ASSETS_DIR, "Player\PlayerBlackWalkLeft4.png"))]

PLAYER_BLACK_WALK_LEFT = [pygame.transform.scale(PLAYER_BLACK_WALK_LEFT[0], (Config.PLAYER_SIZE, Config.PLAYER_SIZE)),
                          pygame.transform.scale(PLAYER_BLACK_WALK_LEFT[1], (Config.PLAYER_SIZE, Config.PLAYER_SIZE)),
                          pygame.transform.scale(PLAYER_BLACK_WALK_LEFT[2], (Config.PLAYER_SIZE, Config.PLAYER_SIZE)),
                          pygame.transform.scale(PLAYER_BLACK_WALK_LEFT[3], (Config.PLAYER_SIZE, Config.PLAYER_SIZE))]

PLAYER_BLACK_WALK_RIGHT = [pygame.image.load(os.path.join(paths.ASSETS_DIR, "Player\PlayerBlackWalkRight1.png")),
                           pygame.image.load(os.path.join(paths.ASSETS_DIR, "Player\PlayerBlackWalkRight2.png")),
                           pygame.image.load(os.path.join(paths.ASSETS_DIR, "Player\PlayerBlackWalkRight3.png")),
                           pygame.image.load(os.path.join(paths.ASSETS_DIR, "Player\PlayerBlackWalkRight4.png"))]

PLAYER_BLACK_WALK_RIGHT = [pygame.transform.scale(PLAYER_BLACK_WALK_RIGHT[0], (Config.PLAYER_SIZE, Config.PLAYER_SIZE)),
                           pygame.transform.scale(PLAYER_BLACK_WALK_RIGHT[1], (Config.PLAYER_SIZE, Config.PLAYER_SIZE)),
                           pygame.transform.scale(PLAYER_BLACK_WALK_RIGHT[2], (Config.PLAYER_SIZE, Config.PLAYER_SIZE)),
                           pygame.transform.scale(PLAYER_BLACK_WALK_RIGHT[3], (Config.PLAYER_SIZE, Config.PLAYER_SIZE))]

PLAYER_BLUE_DEATH = [pygame.image.load(os.path.join(paths.ASSETS_DIR, "Player\PlayerBlueDeath1.png")),
                     pygame.image.load(os.path.join(paths.ASSETS_DIR, "Player\PlayerBlueDeath2.png")),
                     pygame.image.load(os.path.join(paths.ASSETS_DIR, "Player\PlayerBlueDeath3.png")),
                     pygame.image.load(os.path.join(paths.ASSETS_DIR, "Player\PlayerBlueDeath4.png")),
                     pygame.image.load(os.path.join(paths.ASSETS_DIR, "Player\PlayerBlueDeath5.png")),
                     pygame.image.load(os.path.join(paths.ASSETS_DIR, "Player\PlayerBlueDeath6.png"))]

PLAYER_BLUE_DEATH = [pygame.transform.scale(PLAYER_BLUE_DEATH[0], (Config.PLAYER_SIZE, Config.PLAYER_SIZE)),
                     pygame.transform.scale(PLAYER_BLUE_DEATH[1], (Config.PLAYER_SIZE, Config.PLAYER_SIZE)),
                     pygame.transform.scale(PLAYER_BLUE_DEATH[2], (Config.PLAYER_SIZE, Config.PLAYER_SIZE)),
                     pygame.transform.scale(PLAYER_BLUE_DEATH[3], (Config.PLAYER_SIZE, Config.PLAYER_SIZE)),
                     pygame.transform.scale(PLAYER_BLUE_DEATH[4], (Config.PLAYER_SIZE, Config.PLAYER_SIZE)),
                     pygame.transform.scale(PLAYER_BLUE_DEATH[5], (Config.PLAYER_SIZE, Config.PLAYER_SIZE))]

PLAYER_BLUE_WALK_UP = [pygame.image.load(os.path.join(paths.ASSETS_DIR, "Player\PlayerBlueWalkUp1.png")),
                       pygame.image.load(os.path.join(paths.ASSETS_DIR, "Player\PlayerBlueWalkUp2.png")),
                       pygame.image.load(os.path.join(paths.ASSETS_DIR, "Player\PlayerBlueWalkUp3.png")),
                       pygame.image.load(os.path.join(paths.ASSETS_DIR, "Player\PlayerBlueWalkUp4.png"))]

PLAYER_BLUE_WALK_UP = [pygame.transform.scale(PLAYER_BLUE_WALK_UP[0], (Config.PLAYER_SIZE, Config.PLAYER_SIZE)),
                       pygame.transform.scale(PLAYER_BLUE_WALK_UP[1], (Config.PLAYER_SIZE, Config.PLAYER_SIZE)),
                       pygame.transform.scale(PLAYER_BLUE_WALK_UP[2], (Config.PLAYER_SIZE, Config.PLAYER_SIZE)),
                       pygame.transform.scale(PLAYER_BLUE_WALK_UP[3], (Config.PLAYER_SIZE, Config.PLAYER_SIZE))]

PLAYER_BLUE_WALK_DOWN = [pygame.image.load(os.path.join(paths.ASSETS_DIR, "Player\PlayerBlueWalkDown1.png")),
                         pygame.image.load(os.path.join(paths.ASSETS_DIR, "Player\PlayerBlueWalkDown2.png")),
                         pygame.image.load(os.path.join(paths.ASSETS_DIR, "Player\PlayerBlueWalkDown3.png")),
                         pygame.image.load(os.path.join(paths.ASSETS_DIR, "Player\PlayerBlueWalkDown4.png"))]

PLAYER_BLUE_WALK_DOWN = [pygame.transform.scale(PLAYER_BLUE_WALK_DOWN[0], (Config.PLAYER_SIZE, Config.PLAYER_SIZE)),
                         pygame.transform.scale(PLAYER_BLUE_WALK_DOWN[1], (Config.PLAYER_SIZE, Config.PLAYER_SIZE)),
                         pygame.transform.scale(PLAYER_BLUE_WALK_DOWN[2], (Config.PLAYER_SIZE, Config.PLAYER_SIZE)),
                         pygame.transform.scale(PLAYER_BLUE_WALK_DOWN[3], (Config.PLAYER_SIZE, Config.PLAYER_SIZE))]

PLAYER_BLUE_WALK_LEFT = [pygame.image.load(os.path.join(paths.ASSETS_DIR, "Player\PlayerBlueWalkLeft1.png")),
                         pygame.image.load(os.path.join(paths.ASSETS_DIR, "Player\PlayerBlueWalkLeft2.png")),
                         pygame.image.load(os.path.join(paths.ASSETS_DIR, "Player\PlayerBlueWalkLeft3.png")),
                         pygame.image.load(os.path.join(paths.ASSETS_DIR, "Player\PlayerBlueWalkLeft4.png"))]

PLAYER_BLUE_WALK_LEFT = [pygame.transform.scale(PLAYER_BLUE_WALK_LEFT[0], (Config.PLAYER_SIZE, Config.PLAYER_SIZE)),
                         pygame.transform.scale(PLAYER_BLUE_WALK_LEFT[1], (Config.PLAYER_SIZE, Config.PLAYER_SIZE)),
                         pygame.transform.scale(PLAYER_BLUE_WALK_LEFT[2], (Config.PLAYER_SIZE, Config.PLAYER_SIZE)),
                         pygame.transform.scale(PLAYER_BLUE_WALK_LEFT[3], (Config.PLAYER_SIZE, Config.PLAYER_SIZE))]

PLAYER_BLUE_WALK_RIGHT = [pygame.image.load(os.path.join(paths.ASSETS_DIR, "Player\PlayerBlueWalkRight1.png")),
                          pygame.image.load(os.path.join(paths.ASSETS_DIR, "Player\PlayerBlueWalkRight2.png")),
                          pygame.image.load(os.path.join(paths.ASSETS_DIR, "Player\PlayerBlueWalkRight3.png")),
                          pygame.image.load(os.path.join(paths.ASSETS_DIR, "Player\PlayerBlueWalkRight4.png"))]

PLAYER_BLUE_WALK_RIGHT = [pygame.transform.scale(PLAYER_BLUE_WALK_RIGHT[0], (Config.PLAYER_SIZE, Config.PLAYER_SIZE)),
                          pygame.transform.scale(PLAYER_BLUE_WALK_RIGHT[1], (Config.PLAYER_SIZE, Config.PLAYER_SIZE)),
                          pygame.transform.scale(PLAYER_BLUE_WALK_RIGHT[2], (Config.PLAYER_SIZE, Config.PLAYER_SIZE)),
                          pygame.transform.scale(PLAYER_BLUE_WALK_RIGHT[3], (Config.PLAYER_SIZE, Config.PLAYER_SIZE))]

PLAYER_RED_DEATH = [pygame.image.load(os.path.join(paths.ASSETS_DIR, "Player\PlayerRedDeath1.png")),
                    pygame.image.load(os.path.join(paths.ASSETS_DIR, "Player\PlayerRedDeath2.png")),
                    pygame.image.load(os.path.join(paths.ASSETS_DIR, "Player\PlayerRedDeath3.png")),
                    pygame.image.load(os.path.join(paths.ASSETS_DIR, "Player\PlayerRedDeath4.png")),
                    pygame.image.load(os.path.join(paths.ASSETS_DIR, "Player\PlayerRedDeath5.png")),
                    pygame.image.load(os.path.join(paths.ASSETS_DIR, "Player\PlayerRedDeath6.png"))]

PLAYER_RED_DEATH = [pygame.transform.scale(PLAYER_RED_DEATH[0], (Config.PLAYER_SIZE, Config.PLAYER_SIZE)),
                    pygame.transform.scale(PLAYER_RED_DEATH[1], (Config.PLAYER_SIZE, Config.PLAYER_SIZE)),
                    pygame.transform.scale(PLAYER_RED_DEATH[2], (Config.PLAYER_SIZE, Config.PLAYER_SIZE)),
                    pygame.transform.scale(PLAYER_RED_DEATH[3], (Config.PLAYER_SIZE, Config.PLAYER_SIZE)),
                    pygame.transform.scale(PLAYER_RED_DEATH[4], (Config.PLAYER_SIZE, Config.PLAYER_SIZE)),
                    pygame.transform.scale(PLAYER_RED_DEATH[5], (Config.PLAYER_SIZE, Config.PLAYER_SIZE))]

PLAYER_RED_WALK_UP = [pygame.image.load(os.path.join(paths.ASSETS_DIR, "Player\PlayerRedWalkUp1.png")),
                      pygame.image.load(os.path.join(paths.ASSETS_DIR, "Player\PlayerRedWalkUp2.png")),
                      pygame.image.load(os.path.join(paths.ASSETS_DIR, "Player\PlayerRedWalkUp3.png")),
                      pygame.image.load(os.path.join(paths.ASSETS_DIR, "Player\PlayerRedWalkUp4.png"))]

PLAYER_RED_WALK_UP = [pygame.transform.scale(PLAYER_RED_WALK_UP[0], (Config.PLAYER_SIZE, Config.PLAYER_SIZE)),
                      pygame.transform.scale(PLAYER_RED_WALK_UP[1], (Config.PLAYER_SIZE, Config.PLAYER_SIZE)),
                      pygame.transform.scale(PLAYER_RED_WALK_UP[2], (Config.PLAYER_SIZE, Config.PLAYER_SIZE)),
                      pygame.transform.scale(PLAYER_RED_WALK_UP[3], (Config.PLAYER_SIZE, Config.PLAYER_SIZE))]

PLAYER_RED_WALK_DOWN = [pygame.image.load(os.path.join(paths.ASSETS_DIR, "Player\PlayerRedWalkDown1.png")),
                        pygame.image.load(os.path.join(paths.ASSETS_DIR, "Player\PlayerRedWalkDown2.png")),
                        pygame.image.load(os.path.join(paths.ASSETS_DIR, "Player\PlayerRedWalkDown3.png")),
                        pygame.image.load(os.path.join(paths.ASSETS_DIR, "Player\PlayerRedWalkDown4.png"))]

PLAYER_RED_WALK_DOWN = [pygame.transform.scale(PLAYER_RED_WALK_DOWN[0], (Config.PLAYER_SIZE, Config.PLAYER_SIZE)),
                        pygame.transform.scale(PLAYER_RED_WALK_DOWN[1], (Config.PLAYER_SIZE, Config.PLAYER_SIZE)),
                        pygame.transform.scale(PLAYER_RED_WALK_DOWN[2], (Config.PLAYER_SIZE, Config.PLAYER_SIZE)),
                        pygame.transform.scale(PLAYER_RED_WALK_DOWN[3], (Config.PLAYER_SIZE, Config.PLAYER_SIZE))]

PLAYER_RED_WALK_LEFT = [pygame.image.load(os.path.join(paths.ASSETS_DIR, "Player\PlayerRedWalkLeft1.png")),
                        pygame.image.load(os.path.join(paths.ASSETS_DIR, "Player\PlayerRedWalkLeft2.png")),
                        pygame.image.load(os.path.join(paths.ASSETS_DIR, "Player\PlayerRedWalkLeft3.png")),
                        pygame.image.load(os.path.join(paths.ASSETS_DIR, "Player\PlayerRedWalkLeft4.png"))]

PLAYER_RED_WALK_LEFT = [pygame.transform.scale(PLAYER_RED_WALK_LEFT[0], (Config.PLAYER_SIZE, Config.PLAYER_SIZE)),
                        pygame.transform.scale(PLAYER_RED_WALK_LEFT[1], (Config.PLAYER_SIZE, Config.PLAYER_SIZE)),
                        pygame.transform.scale(PLAYER_RED_WALK_LEFT[2], (Config.PLAYER_SIZE, Config.PLAYER_SIZE)),
                        pygame.transform.scale(PLAYER_RED_WALK_LEFT[3], (Config.PLAYER_SIZE, Config.PLAYER_SIZE))]

PLAYER_RED_WALK_RIGHT = [pygame.image.load(os.path.join(paths.ASSETS_DIR, "Player\PlayerRedWalkRight1.png")),
                         pygame.image.load(os.path.join(paths.ASSETS_DIR, "Player\PlayerRedWalkRight2.png")),
                         pygame.image.load(os.path.join(paths.ASSETS_DIR, "Player\PlayerRedWalkRight3.png")),
                         pygame.image.load(os.path.join(paths.ASSETS_DIR, "Player\PlayerRedWalkRight4.png"))]

PLAYER_RED_WALK_RIGHT = [pygame.transform.scale(PLAYER_RED_WALK_RIGHT[0], (Config.PLAYER_SIZE, Config.PLAYER_SIZE)),
                         pygame.transform.scale(PLAYER_RED_WALK_RIGHT[1], (Config.PLAYER_SIZE, Config.PLAYER_SIZE)),
                         pygame.transform.scale(PLAYER_RED_WALK_RIGHT[2], (Config.PLAYER_SIZE, Config.PLAYER_SIZE)),
                         pygame.transform.scale(PLAYER_RED_WALK_RIGHT[3], (Config.PLAYER_SIZE, Config.PLAYER_SIZE))]

PLAYER_WHITE_DEATH = [pygame.image.load(os.path.join(paths.ASSETS_DIR, "Player\PlayerWhiteDeath1.png")),
                      pygame.image.load(os.path.join(paths.ASSETS_DIR, "Player\PlayerWhiteDeath2.png")),
                      pygame.image.load(os.path.join(paths.ASSETS_DIR, "Player\PlayerWhiteDeath3.png")),
                      pygame.image.load(os.path.join(paths.ASSETS_DIR, "Player\PlayerWhiteDeath4.png")),
                      pygame.image.load(os.path.join(paths.ASSETS_DIR, "Player\PlayerWhiteDeath5.png")),
                      pygame.image.load(os.path.join(paths.ASSETS_DIR, "Player\PlayerWhiteDeath6.png"))]

PLAYER_WHITE_DEATH = [pygame.transform.scale(PLAYER_WHITE_DEATH[0], (Config.PLAYER_SIZE, Config.PLAYER_SIZE)),
                      pygame.transform.scale(PLAYER_WHITE_DEATH[1], (Config.PLAYER_SIZE, Config.PLAYER_SIZE)),
                      pygame.transform.scale(PLAYER_WHITE_DEATH[2], (Config.PLAYER_SIZE, Config.PLAYER_SIZE)),
                      pygame.transform.scale(PLAYER_WHITE_DEATH[3], (Config.PLAYER_SIZE, Config.PLAYER_SIZE)),
                      pygame.transform.scale(PLAYER_WHITE_DEATH[4], (Config.PLAYER_SIZE, Config.PLAYER_SIZE)),
                      pygame.transform.scale(PLAYER_WHITE_DEATH[5], (Config.PLAYER_SIZE, Config.PLAYER_SIZE))]

PLAYER_WHITE_WALK_UP = [pygame.image.load(os.path.join(paths.ASSETS_DIR, "Player\PlayerWhiteWalkUp1.png")),
                        pygame.image.load(os.path.join(paths.ASSETS_DIR, "Player\PlayerWhiteWalkUp2.png")),
                        pygame.image.load(os.path.join(paths.ASSETS_DIR, "Player\PlayerWhiteWalkUp3.png")),
                        pygame.image.load(os.path.join(paths.ASSETS_DIR, "Player\PlayerWhiteWalkUp4.png"))]

PLAYER_WHITE_WALK_UP = [pygame.transform.scale(PLAYER_WHITE_WALK_UP[0], (Config.PLAYER_SIZE, Config.PLAYER_SIZE)),
                        pygame.transform.scale(PLAYER_WHITE_WALK_UP[1], (Config.PLAYER_SIZE, Config.PLAYER_SIZE)),
                        pygame.transform.scale(PLAYER_WHITE_WALK_UP[2], (Config.PLAYER_SIZE, Config.PLAYER_SIZE)),
                        pygame.transform.scale(PLAYER_WHITE_WALK_UP[3], (Config.PLAYER_SIZE, Config.PLAYER_SIZE))]

PLAYER_WHITE_WALK_DOWN = [pygame.image.load(os.path.join(paths.ASSETS_DIR, "Player\PlayerWhiteWalkDown1.png")),
                          pygame.image.load(os.path.join(paths.ASSETS_DIR, "Player\PlayerWhiteWalkDown2.png")),
                          pygame.image.load(os.path.join(paths.ASSETS_DIR, "Player\PlayerWhiteWalkDown3.png")),
                          pygame.image.load(os.path.join(paths.ASSETS_DIR, "Player\PlayerWhiteWalkDown4.png"))]

PLAYER_WHITE_WALK_DOWN = [pygame.transform.scale(PLAYER_WHITE_WALK_DOWN[0], (Config.PLAYER_SIZE, Config.PLAYER_SIZE)),
                          pygame.transform.scale(PLAYER_WHITE_WALK_DOWN[1], (Config.PLAYER_SIZE, Config.PLAYER_SIZE)),
                          pygame.transform.scale(PLAYER_WHITE_WALK_DOWN[2], (Config.PLAYER_SIZE, Config.PLAYER_SIZE)),
                          pygame.transform.scale(PLAYER_WHITE_WALK_DOWN[3], (Config.PLAYER_SIZE, Config.PLAYER_SIZE))]

PLAYER_WHITE_WALK_LEFT = [pygame.image.load(os.path.join(paths.ASSETS_DIR, "Player\PlayerWhiteWalkLeft1.png")),
                          pygame.image.load(os.path.join(paths.ASSETS_DIR, "Player\PlayerWhiteWalkLeft2.png")),
                          pygame.image.load(os.path.join(paths.ASSETS_DIR, "Player\PlayerWhiteWalkLeft3.png")),
                          pygame.image.load(os.path.join(paths.ASSETS_DIR, "Player\PlayerWhiteWalkLeft4.png"))]

PLAYER_WHITE_WALK_LEFT = [pygame.transform.scale(PLAYER_WHITE_WALK_LEFT[0], (Config.PLAYER_SIZE, Config.PLAYER_SIZE)),
                          pygame.transform.scale(PLAYER_WHITE_WALK_LEFT[1], (Config.PLAYER_SIZE, Config.PLAYER_SIZE)),
                          pygame.transform.scale(PLAYER_WHITE_WALK_LEFT[2], (Config.PLAYER_SIZE, Config.PLAYER_SIZE)),
                          pygame.transform.scale(PLAYER_WHITE_WALK_LEFT[3], (Config.PLAYER_SIZE, Config.PLAYER_SIZE))]

PLAYER_WHITE_WALK_RIGHT = [pygame.image.load(os.path.join(paths.ASSETS_DIR, "Player\PlayerWhiteWalkRight1.png")),
                           pygame.image.load(os.path.join(paths.ASSETS_DIR, "Player\PlayerWhiteWalkRight2.png")),
                           pygame.image.load(os.path.join(paths.ASSETS_DIR, "Player\PlayerWhiteWalkRight3.png")),
                           pygame.image.load(os.path.join(paths.ASSETS_DIR, "Player\PlayerWhiteWalkRight4.png"))]

PLAYER_WHITE_WALK_RIGHT = [pygame.transform.scale(PLAYER_WHITE_WALK_RIGHT[0], (Config.PLAYER_SIZE, Config.PLAYER_SIZE)),
                           pygame.transform.scale(PLAYER_WHITE_WALK_RIGHT[1], (Config.PLAYER_SIZE, Config.PLAYER_SIZE)),
                           pygame.transform.scale(PLAYER_WHITE_WALK_RIGHT[2], (Config.PLAYER_SIZE, Config.PLAYER_SIZE)),
                           pygame.transform.scale(PLAYER_WHITE_WALK_RIGHT[3], (Config.PLAYER_SIZE, Config.PLAYER_SIZE))]

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
        else:
            self.image = self.image[self.step_index // 4]

        self.X_POS = X_POS
        self.Y_POS = Y_POS

    def walk(self):
        self.image = self.image[self.step_index // 4]
        self.player_rect = self.image.get_rect()
        self.player_rect.x = self.X_POS
        self.player_rect.y = self.Y_POS
        self.step_index += 1

    def death(self):
        self.image = self.death_img[self.death_step // 6]
        self.player_rect = self.image.get_rect()
        self.player_rect.x = self.X_POS
        self.player_rect.y = self.Y_POS
        self.death_step += 1

    def draw(self, width, height):
        if not Config.SCREEN_ON:
            return

        if self.is_death:
            if self.death_step < 35:
                self.death()
            else:
                return
        
        offsetX = (Config.SCREEN_WIDTH - Config.BLOCK_SIZE * width) / 2
        offsetY = (Config.SCREEN_HEIGHT - Config.BLOCK_SIZE * height) / 2
        GlobalState.SCREEN.blit(self.image, (offsetX+self.X_POS, offsetY+self.Y_POS))

    def getXY(self):
        return (self.player_rect.x, self.player_rect.y)