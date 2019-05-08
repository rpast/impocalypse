'''
A function module
'''

import pygame 
import os 
import random 
import asset 
from asset import Block
from player import Player
from enemy import Portal, Imp, FatImp
from bullet import Bullet

#wrapper function
def run_game(width, height, fps, starting_scene):
    '''
    wrapper function that runs the whole game
    all global variables should be defined here
    '''
    os.environ['SDL_VIDEO_CENTERED'] = '1'
    pygame.init()
    window = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Imps & Assasin")
    clock = pygame.time.Clock()
    font = pygame.font.SysFont("calibri", 30)
    font_small = pygame.font.SysFont("calibri", 25)
    
    #instantiate sprite objects 
    assasin = Player(asset.NINJA_R[0])
    #add sprites to groups
    asset.PLAYER_GROUP.add(assasin)

    active_scene = starting_scene

    #GAME LOOP###
    while active_scene != None:
        key = pygame.key.get_pressed()
        
        # Event filtering
        filtered_events = []
        for event in pygame.event.get():
            quit_attempt = False
            if event.type == pygame.QUIT:
                quit_attempt = True
            elif event.type == pygame.KEYDOWN:
                alt_pressed = key[pygame.K_LALT] or \
                              key[pygame.K_RALT]
                if event.key == pygame.K_ESCAPE:
                    quit_attempt = True
                elif event.key == pygame.K_F4 and alt_pressed:
                    quit_attempt = True
            
            if quit_attempt:
                active_scene.Terminate()
            else:
                filtered_events.append(event)
        
        #pass variables to scene methods
        active_scene.ProcessInput(filtered_events, key, assasin)
        active_scene.Update(assasin)
        active_scene.Render(window, font, font_small)
        
        active_scene = active_scene.next
        
        pygame.display.flip()

        clock.tick(fps)


#functions passed to player methods
def identify_death(player, screen, orientation):
    if player.health <= 0:
        if orientation == 0:
            screen.blit(asset.NINJA_DEATH_L[player.deathblocker // 3], (player.rect.x, player.rect.y))
        else:
            screen.blit(asset.NINJA_DEATH_R[player.deathblocker // 3], (player.rect.x, player.rect.y)) 

        if player.deathblocker < 6:
            player.deathblocker += 1     

def identify_jump_attack(player, screen, orientation):
    if player.health > 0 and player.attack == True and player.shoot_bullet == False and player.jump == True:
        if orientation == 0:
            screen.blit(asset.NINJA_ATTACK_L[player.meleblocker // 3], (player.rect.x-40, player.rect.y))
        else:
            screen.blit(asset.NINJA_ATTACK_R[player.meleblocker // 3], (player.rect.x, player.rect.y))
        
        if player.jumpblocker < 6:
            player.jumpblocker += 1

def identify_jump_throw(player, screen, orientation):
    if player.health > 0 and player.attack == False and player.shoot_bullet == True and player.jump == True:
        if orientation == 0:
            screen.blit(asset.NINJA_SHOOT_L[player.throwblocker // 3], (player.rect.x, player.rect.y))
        else:
            screen.blit(asset.NINJA_SHOOT_R[player.throwblocker // 3], (player.rect.x, player.rect.y))
        
        if player.throwblocker < 6:
            player.throwblocker += 1

def identify_jump(player, screen, orientation):
    if player.health > 0 and player.attack == False and player.shoot_bullet == False and player.jump == True:
        if orientation == 0:
            screen.blit(asset.NINJA_JUMP_L[player.jumpblocker // 3], (player.rect.x, player.rect.y))
        else:
            screen.blit(asset.NINJA_JUMP_R[player.jumpblocker // 3], (player.rect.x, player.rect.y))

        if player.jumpblocker < 6:
            player.jumpblocker += 1

def identify_attack(player, screen, orientation):
    if player.health > 0 and player.attack == True and player.shoot_bullet == False and player.jump == False:
        if orientation == 0:
            screen.blit(asset.NINJA_ATTACK_L[player.meleblocker // 3], (player.rect.x-40, player.rect.y))
        else:
            screen.blit(asset.NINJA_ATTACK_R[player.meleblocker // 3], (player.rect.x, player.rect.y))
        
        if player.jumpblocker < 6:
            player.jumpblocker += 1

def identify_throw(player, screen, orientation):
    if player.health > 0 and player.attack == False and player.shoot_bullet == True and player.jump == False:
        if orientation == 0:
            screen.blit(asset.NINJA_SHOOT_L[player.throwblocker // 3], (player.rect.x, player.rect.y))
        else:
            screen.blit(asset.NINJA_SHOOT_R[player.meleblocker // 3], (player.rect.x, player.rect.y))
                
        if player.throwblocker < 6:
            player.throwblocker += 1

def identify_walk(player, screen, orientation):
    if player.health > 0 and player.attack == False and player.shoot_bullet == False and player.jump == False:
        if orientation == 0:
            screen.blit(asset.NINJA_L[player.walkblocker // 3], (player.rect.x, player.rect.y))
        else:
            screen.blit(asset.NINJA_R[player.walkblocker // 3], (player.rect.x, player.rect.y))

    if player.walkblocker + 1 < 9:
        player.walkblocker += 1
    else:
        player.walkblocker = 0

#functions passed to enemy methods
def enemy_walk(enemy):
    dice_roll_1 = (random.random()*100)

    if dice_roll_1 < enemy.walk_dynamics:
        enemy.vel *= -1

    if enemy.vel > 0:
        if enemy.rect.x + enemy.vel < enemy.path[1]:
            enemy.rect.x += enemy.vel
        else:
            enemy.vel *= -1
            enemy.walkcount = 0
    else:
        if enemy.rect.x + enemy.vel > enemy.path[0]:
            enemy.rect.x += enemy.vel
        else:
            enemy.vel *= -1
            enemy.walkcount = 0  

def enemy_jump(enemy):
    dice_roll_2 = (random.random()*100)

    if enemy.jump == False:
        if dice_roll_2 < enemy.jump_dynamics:
            enemy.jump = True
    else:
        if enemy.jumpcount >= -10:
            neg = 1
            if enemy.jumpcount < 0:
                neg = -1
            enemy.rect.y -= (enemy.jumpcount ** 2) * enemy.jump_factor * neg
            enemy.jumpcount -= 1
        else:
            enemy.rect.y = enemy.y_cap
            enemy.jump = False
            enemy.jumpcount = 10

#functions passed to scene methods
def movement_manager(player):
    #player sprite movement mechanics
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and player.rect.x > 0:
        player.rect.x -= player.vel
        player.right = False
        player.left = True
    elif keys[pygame.K_RIGHT] and player.rect.x < asset.WINDOW_W - player.rect.width:
        player.rect.x += player.vel
        player.right = True
        player.left = False
    else:
        player.walkblocker = 0
    #jumping mechanics
    
def jump_manager(player):
    keys = pygame.key.get_pressed()
    if player.jump == False:
        if keys[pygame.K_UP]:
            player.jump = True
    else:
        if player.jumpcount >= -12:
            neg = 1  
            if player.jumpcount < 0:
                neg = -1
            player.rect.y -= (player.jumpcount ** 2) * 0.35 * neg
            player.jumpcount -= 1

        else:
            player.jump = False
            player.jumpcount = player.jumpcount_cap
            player.rect.y = player.rect_y_cap

def shooting_manager(player):
    #player sprite attack controls mechanics
    keys = pygame.key.get_pressed()

    #shooting bullets mechanics
    if player.shoot_bullet == False:
        if keys[pygame.K_x]:
            player.shoot_bullet = True
    else:
        if player.left == True:
            shuriken = Bullet(asset.BULLET_IMG,
                              player.rect.x, player.rect.y+45, 3, -1)
            asset.BULLET_GROUP.add(shuriken)
            player.shoot_bullet = False

        else:
            shuriken = Bullet(asset.BULLET_IMG,
                              player.rect.x+25, player.rect.y+45, 3, 1)
            asset.BULLET_GROUP.add(shuriken)
            player.shoot_bullet = False

def attack_manager(player):
    #player sprite attack controls mechanics
    keys = pygame.key.get_pressed()

    #mele attack switch
    if player.attack == False:
        if keys[pygame.K_SPACE]:
            player.attack = True
            print(player.attack)
    else:
        player.attack = False
  
def redraw_manager(screen, bg, font, player_container, bullet_container, enemy_container):
    #blit background image
    screen.blit(bg, (0, -190))
    #render and blit text
    text = font.render("Assasin HP", 1, (250, 250, 250), )
    screen.blit(text, (13, 25))
    #blit static health bar (foreground)
    screen.blit(asset.H_BAR_IMG, (10, 50))

    #draw health bar
    for player in player_container:
        if player.health > 0: #just to make sure no leftover green bar is blitted
            health_factor = 8 * (30 - player.health)
            pygame.draw.rect(screen, (20, 89, 12), (15, 55, 240 - health_factor, 20))
    #update projectile data and draw
    for bullet in bullet_container:
        bullet.bullet_update()
        asset.BULLET_GROUP.draw(screen)
    #update enemy data and draw
    for enemy in enemy_container:
        enemy.update()
        enemy.draw(screen)
        #draw health bars for enemies
        health_factor = (60/enemy.health_cap) * (enemy.health_cap - enemy.health)
        pygame.draw.rect(screen, (100, 0, 0), (enemy.rect.x, enemy.rect.y - 30, 60, 8))
        pygame.draw.rect(screen, (35, 89, 12), (enemy.rect.x, enemy.rect.y - 30, 60 - health_factor, 8))
    #draw player using sprite container
    for player in player_container:
        player.draw(screen) 
    
    pygame.display.flip()

def collision_manager(player_container, bullet_container, enemy_container, block_container):
    '''
    this function gathers all collision methods from instantiated objects
    and executes them
    '''
    #player mele attack
    for player in player_container:
        player.mele_enemy_collision(player, enemy_container)
    #bullet collisions
    for elem in bullet_container:
        elem.bullet_enemy_collision(bullet_container, enemy_container)
        elem.bullet_block_collision(bullet_container, block_container)
    #enemy mele attack
    for enemy in enemy_container:
        for player in player_container:
            enemy.enemy_player_collision(player, enemy, enemy.damage)

def death_manager(*args):
    for arg in args:
        for elem in arg:
            if elem.health <= 0:
                arg.remove(elem)
                print("Sprite killed")

def enemy_generator(impno, fatno, acidno, mamano, impcap, fatcap, acidcap, mamacap):
    seed_x = random.randint(200,700)
    portal = Portal(asset.PORTAL[0], seed_x, 25)
    asset.ENEMY_GROUP.add(portal)

    if impno > impcap:
        for n in range(0, impcap):
            imp = Imp(asset.IMP_R[0], asset.WINDOW_W, seed_x, 5)
            asset.ENEMY_GROUP.add(imp)
    else:
        for n in range(0, impno):
            imp = Imp(asset.IMP_R[0], asset.WINDOW_W, seed_x, 5)
            asset.ENEMY_GROUP.add(imp)
        
    if fatno > fatcap:
        for n in range(0, fatcap):
            fat_imp = FatImp(asset.IMP_R[0], asset.WINDOW_W, seed_x, 15)
            asset.ENEMY_GROUP.add(fat_imp)
    else:
        for n in range(0, fatno):
            fat_imp = FatImp(asset.FAT_IMP_R[0], asset.WINDOW_W, seed_x, 15)
            asset.ENEMY_GROUP.add(fat_imp)
            
    #add acid imp and mama imp

def transition_message(screen, font, smallfont):
    text1 = font.render("You banished all imps from this land!", 1, (250, 250, 250), )
    text2 = font.render("Hit enter when you are ready to move to next map", 
    1, (250, 250, 250))
    screen.blit(text1, (200, 250))
    screen.blit(text2, (130, 285))

def game_over_message(screen, font, smallfont):
    text3 = font.render("YOU DIED", 1, (250, 250, 250))
    text4 = smallfont.render("Hit enter to restart", 1, (250, 250, 250))
    screen.blit(text3, (350, 250))
    screen.blit(text4, (320, 290))