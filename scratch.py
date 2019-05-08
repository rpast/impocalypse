import pygame, os
from player import Player

pygame.init()
os.environ['SDL_VIDEO_WINDOW_POS'] = "50,50"

WSIZE = (1280,720)
DSIZE = (640, 360)

WINDOW = pygame.display.set_mode((WSIZE))
DISPLAY = pygame.Surface((DSIZE))

BACKGROUND = pygame.image.load("img/backgrounds/background_1.png").convert()
GUYIMG = pygame.image.load("img/enemies/imp_sprite/walk_right1.png").convert()

RUN = True

GUY = Player(GUYIMG)



CLOCK = pygame.time.Clock()


while RUN:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUN = False
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                GUY.right = True
                print(GUY.right)
                print(GUY.rect.x)
                print(GUY.scrolling_x)
            if event.key == pygame.K_LEFT:
                GUY.left = True
                print(GUY.left)
                print(GUY.rect.x)
                print(GUY.scrolling_x)
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                GUY.right = False
                print(GUY.right)
            if event.key == pygame.K_LEFT:
                GUY.left = False
                print(GUY.left)


    if GUY.left == True:
        GUY.vel = GUY.vel * -1
    if GUY.right == True and GUY.vel < 0:
        GUY.vel = GUY.vel * -1

    bgWidth = BACKGROUND.get_rect().width
    HW = int(DSIZE[0] / 2)
    stageWidth = bgWidth * 2
    stagePosX = 0

    startScrollingPosX = HW

    if GUY.left == True or GUY.right == True:
        GUY.scrolling_x += GUY.vel
    
        if GUY.scrolling_x > stageWidth - GUY.rect.width: 
            GUY.scrolling_x = stageWidth - GUY.rect.width
    
        if GUY.scrolling_x < 1: 
            GUY.scrolling_x = 1
    
        if GUY.scrolling_x < startScrollingPosX: 
            GUY.rect.x = GUY.scrolling_x
        elif GUY.scrolling_x > stageWidth - startScrollingPosX:
            GUY.rect.x = GUY.scrolling_x - stageWidth + DSIZE[0]
        else:
            GUY.rect.x = int(startScrollingPosX)
            stagePosX += -GUY.vel
    
    rel_x = stagePosX % bgWidth
    DISPLAY.blit(BACKGROUND, (rel_x - bgWidth, 0))
    if rel_x < DSIZE[0]:
        DISPLAY.blit(BACKGROUND, (rel_x, 0))


    GUY.draw(DISPLAY)


    WINDOW.blit(pygame.transform.scale(DISPLAY, WSIZE),(0, 0))
    pygame.display.update()

    CLOCK.tick(100)

    