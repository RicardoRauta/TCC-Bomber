class Config:
    CPU_CORE = 16
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

    #NEURONS = [978, 489, 4] # 978 * 489 + 489 * 4 = 480.198
    #NEURONS = [369, 184, 4] # 369 * 184 + 184 * 4 = 68.632
    NEURONS = [190, 95, 4] # 190 * 95 + 95 * 4 = 18.430
    WEIGHTS_QTD = NEURONS[0] * NEURONS[1] + NEURONS[1] * NEURONS[2]
    WEIGHTS_RANGE = 1000

    ## MODE CONFIG

    ARENA_QTD = 64
    HUMAN_MODE = False
    LOAD = False
    SCREEN_ON = True
    SENSOR_TOTAL = False


    ## GAME CONFIG

    # Pontuação:
    # Colocou bomba    5
    SCORE_BOMB = 50
    # Destruiu bloco   5
    SCORE_BRICK = 200
    # Se explodiu
    SCORE_SELF_KILL = -500
    # Explodiu oponente
    SCORE_KILL_PLAYER = 500

    ## ARENA CONFIG
    ARENA_BLOCK = '*'
    ARENA_WALL = 'o'
    ARENA_BOMB = '0'
    ARENA_EXPLOSION = 'x'
    ARENA_VOID = '-'
    ARENA_UPGRADE_BOMB = 'b'
    ARENA_UPGRADE_POWER = 'p'
    ARENA_UPGRADE_SPEED = 's'