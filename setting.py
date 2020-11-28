''' Adjust screen width and height accordingly '''
WIDTH = 800
HEIGHT = 800

''' All game component positions and sizes depend on the screen width and height '''
MINI_WIDTH = int(HEIGHT/4)
MINI_HEIGHT = int(HEIGHT/4)

G_OFFSET_X = int(WIDTH/4)
G_OFFSET_Y = int(HEIGHT/8)
OFFSET = int(G_OFFSET_Y*1.2)
G_MINI_OFFSET = int(WIDTH/8) 

H_SIZE = int(HEIGHT/10)
V_SIZE = int(HEIGHT/10)
MINI_H_SIZE = int(MINI_WIDTH/10)
MINI_V_SIZE = int(MINI_HEIGHT/10)
MINI_Y = G_OFFSET_Y + 6 * V_SIZE 
MINI_OFFSET = 4*MINI_V_SIZE 

SHRINKER = int(V_SIZE * 2/10)
RADIUS = int((V_SIZE-2*SHRINKER)/2)
MINI_SHRINKER = int(MINI_V_SIZE * 2/10)
MINI_RADIUS = int((MINI_V_SIZE-2*MINI_SHRINKER)/2)

TEXT_SIZE = int(HEIGHT/45) 
TEXT_POS_X = int(HEIGHT/8)
TEXT_POS_Y = int(0.3*HEIGHT/8)

MESSAGE_POS = (WIDTH/3, 6*V_SIZE)
MESSAGE_DURATION = 3
TIME_POS = (WIDTH/3, V_SIZE/3)
ROUND_POS = (WIDTH - 2*H_SIZE, V_SIZE)
SCORE_POS = (WIDTH - 2*H_SIZE, 1.3*V_SIZE)
RESET_POS = (WIDTH - 2*H_SIZE, 2*V_SIZE)
NOSET_POS = (WIDTH - 2*H_SIZE, 3*V_SIZE)
EXIT_POS = (WIDTH - 2*H_SIZE, 4*V_SIZE)

RESET_NAME = "<SHUFFLE>" 
NOSET_NAME = "NO SET!" 
EXIT_NAME = "Good Bye" 

''' Color settings '''
RED    = (255, 0 ,0)
ORANGE = (255, 140, 0)
YELLOW = (255, 255, 0)
GREEN  = (0, 255, 0)
BLUE   = (0, 0, 255)
WHITE  = (255, 255, 255)
GRAY   = (120, 120, 120)
BROWN  = (139, 69, 19)
BLACK  = (0, 0, 0)

COLORS = ['red', 'blue', 'yellow']
BG_COLORS = ['white', 'brown', 'black']
SHAPES = ['rect', 'circle', 'triangle']
SELECT_COLOR = GREEN
CM = {
    'red': RED,
    'yellow': YELLOW,
    'green': GREEN,
    'blue': BLUE,
    'white': WHITE,
    'gray': GRAY,
    'brown': BROWN,
    'black': BLACK,
}