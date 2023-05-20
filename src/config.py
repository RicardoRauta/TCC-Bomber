class Config:
    CPU_CORE = 4
    FPS = 30

    ## Screen Information
    #SCREEN_HEIGHT = 800
    #SCREEN_WIDTH = 800
    SCREEN_HEIGHT = 400
    SCREEN_WIDTH = 400

    BLOCK_SIZE = 32
    PLAYER_SIZE = 28
    BOMB_SIZE = 30

    ## IA CONFIG

    #NEURONS = [978, 489, 4] # 978 * 489 + 489 * 4 = 480198
    NEURONS = [369, 184, 4] # 369 * 184 + 184 * 4 = 68632
    WEIGHTS_QTD = NEURONS[0] * NEURONS[1] + NEURONS[1] * NEURONS[2]
    WEIGHTS_RANGE = 1000

    ## MODE CONFIG

    ARENA_QTD = 16
    HUMAN_MODE = False
    LOAD = False
    SCREEN_ON = True
    SENSOR_TOTAL = False


    ## GAME CONFIG

    # Pontuação:
    # Colocou bomba    5
    SCORE_BOMB = 5
    # Destruiu bloco   1
    SCORE_BRICK = 5
    # Se explodiu
    SCORE_SELF_KILL = -20
    # Explodiu oponente
    SCORE_KILL_PLAYER = 20