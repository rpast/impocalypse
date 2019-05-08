import pygame

class Wall(pygame.sprite.Sprite):
    def __init__(self, left, top, wall_x, wall_y):
        pygame.sprite.Sprite.__init__(self)
        self.wall_x = wall_x
        self.wall_y = wall_y
        self.left = left
        self.top = top
        self.rect = (self.left, self.top, self.wall_x, self.wall_y)

class Block(pygame.sprite.Sprite):
    def __init__(self, image, block_x, block_y,):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = block_x
        self.rect.y = block_y

#instantiate wall objects
WALL_LEFT = Wall(-1, 0, 1, 600)
WALL_RIGHT = Wall(800, 0, 1, 600)
# window dimension var
WINDOW_W = 800
WINDOW_H = 600
#set sprite groups containers
PLAYER_GROUP = pygame.sprite.Group()
BULLET_GROUP = pygame.sprite.Group()
ITEM_GROUP = pygame.sprite.Group()
ENEMY_GROUP = pygame.sprite.Group()
BOSS_GROUP = pygame.sprite.Group()
ENEMY_BULLET_GROUP = pygame.sprite.Group()
BLOCK_GROUP = pygame.sprite.Group()
#add block objects to group
BLOCK_GROUP.add(WALL_LEFT)
BLOCK_GROUP.add(WALL_RIGHT)

#image library
NINJA_R = [pygame.image.load("img/ninja_sprite/walk_r_1.png"), pygame.image.load("img/ninja_sprite/walk_r_2.png"),
            pygame.image.load("img/ninja_sprite/walk_r_3.png")]
NINJA_L = [pygame.image.load("img/ninja_sprite/walk_l_1.png"), pygame.image.load("img/ninja_sprite/walk_l_2.png"),
            pygame.image.load("img/ninja_sprite/walk_l_3.png")]

NINJA_JUMP_R = [pygame.image.load("img/ninja_sprite/jump_r_1.png"), pygame.image.load("img/ninja_sprite/jump_r_2.png"),
            pygame.image.load("img/ninja_sprite/jump_r_3.png")]
NINJA_JUMP_L = [pygame.image.load("img/ninja_sprite/jump_l_1.png"), pygame.image.load("img/ninja_sprite/jump_l_2.png"),
            pygame.image.load("img/ninja_sprite/jump_l_3.png")]

NINJA_ATTACK_R = [pygame.image.load("img/ninja_sprite/mele_r_1.png"), pygame.image.load("img/ninja_sprite/mele_r_2.png"),
            pygame.image.load("img/ninja_sprite/mele_r_3.png")]
NINJA_ATTACK_L = [pygame.image.load("img/ninja_sprite/mele_l_1.png"), pygame.image.load("img/ninja_sprite/mele_l_2.png"),
            pygame.image.load("img/ninja_sprite/mele_l_3.png")]

NINJA_SHOOT_R = [pygame.image.load("img/ninja_sprite/throw_r_2.png"), pygame.image.load("img/ninja_sprite/throw_r_3.png"),              pygame.image.load("img/ninja_sprite/throw_r_4.png"),]
NINJA_SHOOT_L = [pygame.image.load("img/ninja_sprite/throw_l_2.png"), pygame.image.load("img/ninja_sprite/throw_l_3.png"),              pygame.image.load("img/ninja_sprite/throw_l_4.png"),]

NINJA_DEATH_R = [pygame.image.load("img/ninja_sprite/death_r_2.png"), pygame.image.load("img/ninja_sprite/death_r_3.png"),              pygame.image.load("img/ninja_sprite/death_r_4.png"),]
NINJA_DEATH_L = [pygame.image.load("img/ninja_sprite/death_l_2.png"), pygame.image.load("img/ninja_sprite/death_l_3.png"),              pygame.image.load("img/ninja_sprite/death_l_4.png"),]


IMP_R = [pygame.image.load("img/imp_sprite/walk_right1.png"), pygame.image.load("img/imp_sprite/walk_right2.png"),
            pygame.image.load("img/imp_sprite/walk_right3.png"), pygame.image.load("img/imp_sprite/walk_right4.png"),
            pygame.image.load("img/imp_sprite/walk_right5.png"), pygame.image.load("img/imp_sprite/walk_right6.png"),
            pygame.image.load("img/imp_sprite/walk_right7.png"), pygame.image.load("img/imp_sprite/walk_right8.png"),
            pygame.image.load("img/imp_sprite/walk_right9.png")]
IMP_L = [pygame.image.load("img/imp_sprite/walk_left1.png"), pygame.image.load("img/imp_sprite/walk_left2.png"),
            pygame.image.load("img/imp_sprite/walk_left3.png"), pygame.image.load("img/imp_sprite/walk_left4.png"),
            pygame.image.load("img/imp_sprite/walk_left5.png"), pygame.image.load("img/imp_sprite/walk_left6.png"),
            pygame.image.load("img/imp_sprite/walk_left7.png"), pygame.image.load("img/imp_sprite/walk_left8.png"),
            pygame.image.load("img/imp_sprite/walk_left9.png")]

FAT_IMP_R = [pygame.image.load("img/fat_imp_sprite/walk_right1.png"), 
            pygame.image.load("img/fat_imp_sprite/walk_right2.png"),
            pygame.image.load("img/fat_imp_sprite/walk_right3.png"), 
            pygame.image.load("img/fat_imp_sprite/walk_right4.png"),
            pygame.image.load("img/fat_imp_sprite/walk_right5.png"), 
            pygame.image.load("img/fat_imp_sprite/walk_right6.png"),
            pygame.image.load("img/fat_imp_sprite/walk_right7.png"), 
            pygame.image.load("img/fat_imp_sprite/walk_right8.png"),
            pygame.image.load("img/fat_imp_sprite/walk_right9.png")]
FAT_IMP_L = [pygame.image.load("img/fat_imp_sprite/walk_left1.png"), 
            pygame.image.load("img/fat_imp_sprite/walk_left2.png"),
            pygame.image.load("img/fat_imp_sprite/walk_left3.png"), 
            pygame.image.load("img/fat_imp_sprite/walk_left4.png"),
            pygame.image.load("img/fat_imp_sprite/walk_left5.png"), 
            pygame.image.load("img/fat_imp_sprite/walk_left6.png"),
            pygame.image.load("img/fat_imp_sprite/walk_left7.png"), 
            pygame.image.load("img/fat_imp_sprite/walk_left8.png"),
            pygame.image.load("img/fat_imp_sprite/walk_left9.png")]

PORTAL = [pygame.image.load("img/portal1.png")]

BULLET_IMG = pygame.image.load("img/bullet1.png")
BG = [pygame.image.load("img/Background.png"), pygame.image.load("img/Background.png")]
H_BAR_IMG = pygame.image.load("img/easy_health_bar.png")