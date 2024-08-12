class Config:
    CPU_CORE = 32
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

    #NEURONS = [978, 489, 4] # 978 * 489 + 489 * 5 = 480.687
    #NEURONS = [369, 184, 4] # 369 * 184 + 184 * 5 = 68.816
    NEURONS = [190, 95, 5] # 190 * 95 + 95 * 5 = 18.525
    WEIGHTS_QTD = NEURONS[0] * NEURONS[1] + NEURONS[1] * NEURONS[2]
    WEIGHTS_RANGE = 1000

#comecou 16:10
#gen 666 em 21h53, 14:03
    ## MODE CONFIG

    ARENA_QTD = 256
    HUMAN_MODE = True
    LOAD = True
    SCREEN_ON = True
    SENSOR_TOTAL = False


    ## GAME CONFIG

    # Pontuação:
    # Colocou bomba
    SCORE_BOMB = 10
    # Destruiu bloco
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