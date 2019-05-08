'''
Settings file:
1st section - game settings
2nd section - game assets
'''

import pygame
from gears import SpriteSheet, Block
from player import Player


#Game settings section ###

#Window dimension var
WINDOW_SIZE = (1280, 720)
WINDOW_W = WINDOW_SIZE[0]
WINDOW_H = WINDOW_SIZE[1]

FPS = 60

#Pygame and video mode initialized to allow image conversion
pygame.init()
window = pygame.display.set_mode((WINDOW_SIZE)) #the same settings as in the game wrapper

#Display layer size
#note:
#1024 = 16 x 64 or 32 x 32 or 64 * 16
#768 = 16 x 48 or 32 x 24 or 64 x 12
DISPLAY_SIZE = (640 , 360)
DISPLAY_W, DISPLAY_H = DISPLAY_SIZE

TILE_SIZE = 32

#Font details
FACE = "calibri"
TITLE = 22
NORMAL = 19
SMALL = 16

FONT_TITLE = pygame.font.SysFont(FACE, TITLE)
FONT_NORMAL = pygame.font.SysFont(FACE, NORMAL)
FONT_SMALL = pygame.font.SysFont(FACE, SMALL)
FONT_LIST = [FONT_TITLE, FONT_NORMAL, FONT_SMALL]

#Colour palete
BLACK = (18,19,27)
WHITE = (250, 250, 250)
RED = (100, 0, 0)
GREEN = (20, 89, 12)

#Game physics
GRAVITY = 1
V_MOMENTUM_TRESHOLD = 6
V_MOMENTUM_IMPACT = 14 #How fast player falls
V_MOMENTUM_NEG_IMPACT = -16 #How high player jumps

#Game assets section ###

#instantiate wall objects
WALL_LEFT = Block(-1, 0, 1, WINDOW_H)
WALL_RIGHT = Block(WINDOW_W, 0, 1, WINDOW_H)

#set sprite groups containers
PLAYER_GROUP = pygame.sprite.Group()
BULLET_GROUP = pygame.sprite.Group()
ITEM_GROUP = pygame.sprite.Group()
ENEMY_GROUP = pygame.sprite.Group()
BOSS_GROUP = pygame.sprite.Group()
ENEMY_BULLET_GROUP = pygame.sprite.Group()
WALL_GROUP = pygame.sprite.Group()

#add block objects to group
WALL_GROUP.add(WALL_LEFT)
WALL_GROUP.add(WALL_RIGHT)

#define player instances and sprites
PLAYER_SS = SpriteSheet("img/ninja_sprite/idle_sheet.png")
LOADED_PLAYER_SS = PLAYER_SS.images_at(((0,0,32,32),(50,0,32,32),(104,0,32,32),(153,0,32,32)),(0, 0, 0))
#instantiate player sprite 
ASSASIN = Player(LOADED_PLAYER_SS[3])
#add sprite to player group
PLAYER_GROUP.add(ASSASIN)


#/// TEST TILE
game_map_1 = [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
              [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,3,3,3,2,2,2,2,3,3,3,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2],
              [3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3],
            ]

game_map_2 = [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
              [0,0,1,1,1,0,0,0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0,1,1,1,0,0,0,0],
              [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
              [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
            ]

MAPS = [game_map_1, game_map_2]
### image library ###

#player
#NINJA_R = [pygame.image.load("img/ninja_sprite/walk_r_1.png"), pygame.image.load("img/ninja_sprite/walk_r_2.png"),
#            pygame.image.load("img/ninja_sprite/walk_r_3.png")]
#NINJA_L = [pygame.image.load("img/ninja_sprite/walk_l_1.png"), pygame.image.load("img/ninja_sprite/walk_l_2.png"),
#            pygame.image.load("img/ninja_sprite/walk_l_3.png")]
#
#NINJA_JUMP_R = [pygame.image.load("img/ninja_sprite/jump_r_1.png"), pygame.image.load("img/ninja_sprite/jump_r_2.png"),
#            pygame.image.load("img/ninja_sprite/jump_r_3.png")]
#NINJA_JUMP_L = [pygame.image.load("img/ninja_sprite/jump_l_1.png"), pygame.image.load("img/ninja_sprite/jump_l_2.png"),
#            pygame.image.load("img/ninja_sprite/jump_l_3.png")]
#
#NINJA_ATTACK_R = [pygame.image.load("img/ninja_sprite/mele_r_1.png"), pygame.image.load("img/ninja_sprite/mele_r_2.png"),
#            pygame.image.load("img/ninja_sprite/mele_r_3.png")]
#NINJA_ATTACK_L = [pygame.image.load("img/ninja_sprite/mele_l_1.png"), pygame.image.load("img/ninja_sprite/mele_l_2.png"),
#            pygame.image.load("img/ninja_sprite/mele_l_3.png")]
#
#NINJA_SHOOT_R = [pygame.image.load("img/ninja_sprite/throw_r_2.png"), pygame.image.load("img/ninja_sprite/throw_r_3.png"),  #            pygame.image.load("img/ninja_sprite/throw_r_4.png"),]
#NINJA_SHOOT_L = [pygame.image.load("img/ninja_sprite/throw_l_2.png"), pygame.image.load("img/ninja_sprite/throw_l_3.png"),  #            pygame.image.load("img/ninja_sprite/throw_l_4.png"),]
#
#NINJA_DEATH_R = [pygame.image.load("img/ninja_sprite/death_r_2.png"), pygame.image.load("img/ninja_sprite/death_r_3.png"),  #            pygame.image.load("img/ninja_sprite/death_r_4.png"),]
#NINJA_DEATH_L = [pygame.image.load("img/ninja_sprite/death_l_2.png"), pygame.image.load("img/ninja_sprite/death_l_3.png"),  #            pygame.image.load("img/ninja_sprite/death_l_4.png"),]
#
#NINJA32 = [pygame.image.load("img/walk_32.png")]

#enemies
IMP_R = [pygame.image.load("img/enemies/imp_sprite/walk_right1.png"), pygame.image.load("img/enemies/imp_sprite/walk_right2.png"),
            pygame.image.load("img/enemies/imp_sprite/walk_right3.png"), pygame.image.load("img/enemies/imp_sprite/walk_right4.png"),
            pygame.image.load("img/enemies/imp_sprite/walk_right5.png"), pygame.image.load("img/enemies/imp_sprite/walk_right6.png"),
            pygame.image.load("img/enemies/imp_sprite/walk_right7.png"), pygame.image.load("img/enemies/imp_sprite/walk_right8.png"),
            pygame.image.load("img/enemies/imp_sprite/walk_right9.png")]
IMP_L = [pygame.image.load("img/enemies/imp_sprite/walk_left1.png"), pygame.image.load("img/enemies/imp_sprite/walk_left2.png"),
            pygame.image.load("img/enemies/imp_sprite/walk_left3.png"), pygame.image.load("img/enemies/imp_sprite/walk_left4.png"),
            pygame.image.load("img/enemies/imp_sprite/walk_left5.png"), pygame.image.load("img/enemies/imp_sprite/walk_left6.png"),
            pygame.image.load("img/enemies/imp_sprite/walk_left7.png"), pygame.image.load("img/enemies/imp_sprite/walk_left8.png"),
            pygame.image.load("img/enemies/imp_sprite/walk_left9.png")]



FAT_IMP_R = [pygame.image.load("img/enemies/fat_imp_sprite/walk_right1.png"), 
            pygame.image.load("img/enemies/fat_imp_sprite/walk_right2.png"),
            pygame.image.load("img/enemies/fat_imp_sprite/walk_right3.png"), 
            pygame.image.load("img/enemies/fat_imp_sprite/walk_right4.png"),
            pygame.image.load("img/enemies/fat_imp_sprite/walk_right5.png"), 
            pygame.image.load("img/enemies/fat_imp_sprite/walk_right6.png"),
            pygame.image.load("img/enemies/fat_imp_sprite/walk_right7.png"), 
            pygame.image.load("img/enemies/fat_imp_sprite/walk_right8.png"),
            pygame.image.load("img/enemies/fat_imp_sprite/walk_right9.png")]
FAT_IMP_L = [pygame.image.load("img/enemies/fat_imp_sprite/walk_left1.png"), 
            pygame.image.load("img/enemies/fat_imp_sprite/walk_left2.png"),
            pygame.image.load("img/enemies/fat_imp_sprite/walk_left3.png"), 
            pygame.image.load("img/enemies/fat_imp_sprite/walk_left4.png"),
            pygame.image.load("img/enemies/fat_imp_sprite/walk_left5.png"), 
            pygame.image.load("img/enemies/fat_imp_sprite/walk_left6.png"),
            pygame.image.load("img/enemies/fat_imp_sprite/walk_left7.png"), 
            pygame.image.load("img/enemies/fat_imp_sprite/walk_left8.png"),
            pygame.image.load("img/enemies/fat_imp_sprite/walk_left9.png")]

PORTAL = [pygame.image.load("img/enemies/portal1.png")]

#Tileset
T_GRASS = pygame.image.load("img/tiles/grass32.png").convert()
T_DIRT = pygame.image.load("img/tiles/dirt32.png").convert()
T_BLACK = pygame.image.load("img/tiles/blacktile32.png").convert()

#varia
BULLET_IMG = pygame.image.load("img/bullets/bullet_1.png")
BACKGROUNDS = [pygame.image.load("img/backgrounds/background_1.png").convert(), pygame.image.load("img/backgrounds/background_1.png").convert()]
H_BAR_IMG = pygame.image.load("img/GUI/health_bar.png").convert()