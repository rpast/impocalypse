'''
A functions collection for Impocalypse game
'''

import pygame, os, random, asset
from bullet import Bullet
from gears import SpriteSheet, Block

#wrapper function
def run_game(size, fps, starting_scene):
    '''
    wrapper function that runs the whole game
    all global variables should be defined here
    '''
    os.environ['SDL_VIDEO_CENTERED'] = '1'

    pygame.init()
    clock = pygame.time.Clock()
    pygame.display.set_caption("IMPOCALYPSE")

    #initiate window and display surface

    #window = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    window = pygame.display.set_mode((size)) #initiate the window
    display = pygame.Surface(asset.DISPLAY_SIZE)
    stage_pos = 0
    
    #initiate scalable render space

    active_scene = starting_scene

    #GAME LOOP###
    while active_scene != None:
        key = pygame.key.get_pressed()
        
        # Event handler 
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

            #Movement mechanics
                for player in asset.PLAYER_GROUP:
                    if event.key == pygame.K_RIGHT:
                        player.right = True
                    if event.key == pygame.K_LEFT:
                        player.left = True
                    if event.key == pygame.K_UP:
                        if player.air_timer < asset.V_MOMENTUM_TRESHOLD:
                            player.vertical_momentum = asset.V_MOMENTUM_NEG_IMPACT

            elif event.type == pygame.KEYUP:
                for player in asset.PLAYER_GROUP:
                    if event.key == pygame.K_RIGHT:
                        player.right = False
                    if event.key == pygame.K_LEFT:
                        player.left = False
            ###

            if quit_attempt:
                active_scene.Terminate()
            else:
                filtered_events.append(event)
        
        #pass variables to scene methods
        active_scene.ProcessInput(filtered_events, key, asset.PLAYER_GROUP, display, stage_pos)
        active_scene.Update()
        active_scene.Render(display, asset.FONT_LIST)
        
        active_scene = active_scene.next

        #current_size = pygame.display.get_surface().get_size()
        window.blit(pygame.transform.scale(display, asset.WINDOW_SIZE),(0, 0))
        pygame.display.update()

        clock.tick(asset.FPS)

#functions passed to player methods
def animate_death(player, screen, orientation):
    if player.health <= 0:
        if orientation == 0:
            screen.blit(asset.NINJA_DEATH_L[player.deathblocker // 3], (player.rect.x, player.rect.y))
        else:
            screen.blit(asset.NINJA_DEATH_R[player.deathblocker // 3], (player.rect.x, player.rect.y)) 

        if player.deathblocker < 6:
            player.deathblocker += 1     

def animate_jump_attack(player, screen, orientation):
    if player.health > 0 and player.attack == True and player.shoot_bullet == False and player.jump == True:
        if orientation == 0:
            screen.blit(asset.NINJA_ATTACK_L[player.meleblocker // 3], (player.rect.x-40, player.rect.y))
        else:
            screen.blit(asset.NINJA_ATTACK_R[player.meleblocker // 3], (player.rect.x, player.rect.y))
        
        if player.jumpblocker < 6:
            player.jumpblocker += 1

def animate_jump_throw(player, screen, orientation):
    if player.health > 0 and player.attack == False and player.shoot_bullet == True and player.jump == True:
        if orientation == 0:
            screen.blit(asset.NINJA_SHOOT_L[player.throwblocker // 3], (player.rect.x, player.rect.y))
        else:
            screen.blit(asset.NINJA_SHOOT_R[player.throwblocker // 3], (player.rect.x, player.rect.y))
        
        if player.throwblocker < 6:
            player.throwblocker += 1

def animate_jump(player, screen, orientation):
    if player.health > 0 and player.attack == False and player.shoot_bullet == False and player.jump == True:
        if orientation == 0:
            screen.blit(asset.NINJA_JUMP_L[player.jumpblocker // 3], (player.rect.x, player.rect.y))
        else:
            screen.blit(asset.NINJA_JUMP_R[player.jumpblocker // 3], (player.rect.x, player.rect.y))

        if player.jumpblocker < 6:
            player.jumpblocker += 1

def animate_attack(player, screen, orientation):
    if player.health > 0 and player.attack == True and player.shoot_bullet == False and player.jump == False:
        if orientation == 0:
            screen.blit(asset.NINJA_ATTACK_L[player.meleblocker // 3], (player.rect.x-40, player.rect.y))
        else:
            screen.blit(asset.NINJA_ATTACK_R[player.meleblocker // 3], (player.rect.x, player.rect.y))
        
        if player.jumpblocker < 6:
            player.jumpblocker += 1

def animate_throw(player, screen, orientation):
    if player.health > 0 and player.attack == False and player.shoot_bullet == True and player.jump == False:
        if orientation == 0:
            screen.blit(asset.NINJA_SHOOT_L[player.throwblocker // 3], (player.rect.x, player.rect.y))
        else:
            screen.blit(asset.NINJA_SHOOT_R[player.meleblocker // 3], (player.rect.x, player.rect.y))
                
        if player.throwblocker < 6:
            player.throwblocker += 1

def animate_walk(player, screen, orientation):
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
def animate_enemy_walk(enemy):
    dice_roll_1 = (random.random()*100)

    if dice_roll_1 < enemy.walk_dynamics:
        enemy.vel *= -1

    if enemy.vel > 0:
        if enemy.rect.x + enemy.vel < enemy.path[1]:
            enemy.rect.x += enemy.vel
        else:
            enemy.vel *= -1
            enemy.walkblocker = 0
    else:
        if enemy.rect.x + enemy.vel > enemy.path[0]:
            enemy.rect.x += enemy.vel
        else:
            enemy.vel *= -1
            enemy.walkblocker = 0  

def animate_enemy_jump(enemy):
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

def animate_species(enemy, screen, orientation, catalog_no):
    if orientation < 1:
        if catalog_no == 0:
            screen.blit(asset.IMP_L[enemy.walkblocker // 3], (enemy.rect.x, enemy.rect.y))
        elif catalog_no == 1:
            screen.blit(asset.FAT_IMP_L[enemy.walkblocker // 3], (enemy.rect.x, enemy.rect.y))
        elif catalog_no == 2:
            screen.blit(asset.ACID_IMP_L[enemy.walkblocker // 3], (enemy.rect.x, enemy.rect.y))
        else:
            screen.blit(asset.MAMA_IMP_L[enemy.walkblocker // 3], (enemy.rect.x, enemy.rect.y))
    else:
        if catalog_no == 0:
            screen.blit(asset.IMP_R[enemy.walkblocker // 3], (enemy.rect.x, enemy.rect.y))
        elif catalog_no == 1:
            screen.blit(asset.FAT_IMP_R[enemy.walkblocker // 3], (enemy.rect.x, enemy.rect.y))
        elif catalog_no == 2:
            screen.blit(asset.ACID_IMP_R[enemy.walkblocker // 3], (enemy.rect.x, enemy.rect.y))
        else:
            screen.blit(asset.MAMA_IMP_R[enemy.walkblocker // 3], (enemy.rect.x, enemy.rect.y))

    enemy.walkblocker += 1
    if enemy.walkblocker + 1 == 27:
        enemy.walkblocker = 0


#functions passed to scene methods

def collision_test(rect, tiles):
    hit_list = []
    for tile in tiles:
        if rect.colliderect(tile):
            if tile not in hit_list:
                hit_list.append(tile)
    return hit_list
# ^ nested in:
def move(player, movement, tiles, display_width, screen, level, stage_position):
    collision_types = {'top':False, 'bottom':False, 'right':False, 'left':False}
    
    #scroller###
    background = asset.BACKGROUNDS[level-1]
    bg_width = background.get_rect().width
    stage_width = bg_width * 2
    scroll_start_pos = int(display_width / 2)
    
    player.rect.x += movement[0]
    player.scrolling_x += movement[0]
    #left collision
    if player.rect.x < 0:
        player.rect.x = 0
    #rolling background movement
    if player.rect.x < scroll_start_pos:
        player.scrolling_x = 0

    elif player.scrolling_x > stage_width - scroll_start_pos:
        player.rect.x = player.scrolling_x - stage_width + display_width

        if player.rect.x > stage_width - player.rect.width:
            player.rect.x = stage_width - player.rect.width

    else:
        player.rect.x = int(scroll_start_pos)
        stage_position += -player.scrolling_x
        
    #relative_x = stage_position % bgWidth
    relative_x = (stage_position % bg_width)
    screen.blit(background, (relative_x - bg_width, 0))
    if relative_x < display_width:
        screen.blit(background, (relative_x, 0))
        print("***\n")
        print(f"relative x:{relative_x}")
        print(f"stage position: {stage_position}")
        print(f"bg width: {bg_width}")
        print(f"stage width: {stage_width}")
    
    ###
    hit_list = collision_test(player.rect, tiles)
    for tile in hit_list:
        if movement[0] > 0:
            player.rect.right = tile.left
            collision_types['right'] = True
        elif movement[0] < 0:
            player.rect.left = tile.right
            collision_types['left'] = True

    player.rect.y += movement[1]
    hit_list = collision_test(player.rect,tiles)
    for tile in hit_list:
        if movement[1] > 0:
            player.rect.bottom = tile.top
            collision_types['bottom'] = True
        elif movement[1] < 0:
            player.rect.top = tile.bottom
            collision_types['top'] = True

    return player.rect, collision_types
# ^ nested in:
def movement_manager(player, tilelist, display_width, screen, level, stage_position):
    #player sprite movement mechanics
    player_movement = [0,0]

    if player.right == True:
        player_movement[0] += player.vel
    if player.left == True:
        player_movement[0] -= player.vel

    player_movement[1] += player.vertical_momentum
    player.vertical_momentum += asset.GRAVITY
    if player.vertical_momentum > asset.V_MOMENTUM_TRESHOLD:
        player.vertical_momentum = asset.V_MOMENTUM_IMPACT

    player.rect,collisions = move(player, player_movement, tilelist, display_width, screen, level, stage_position)

    if collisions['bottom'] == True:
        player.air_timer = 0
        player.vertical_momentum = 0
    else:
        player.air_timer += 1


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
    else:
        player.attack = False

def tile_drawer(screen, level, tilelist, tile1=0, tile2=0, tile3=0, tile4=0, tile5=0):
    y = 0
    for layer in asset.MAPS[level-1]:
        x = 0
        for tile in layer:
            if tile == 1:
                screen.blit(tile1,(x * asset.TILE_SIZE, y * asset.TILE_SIZE))
            if tile == 2:
                screen.blit(tile2,(x * asset.TILE_SIZE, y * asset.TILE_SIZE))
            if tile == 3:
                screen.blit(tile3,(x * asset.TILE_SIZE, y * asset.TILE_SIZE)) 
            if tile == 4:
                screen.blit(tile4,(x * asset.TILE_SIZE, y * asset.TILE_SIZE))
            if tile == 5:
                screen.blit(tile5,(x * asset.TILE_SIZE, y * asset.TILE_SIZE))
            if tile != 0:
                empty_tile = pygame.Rect(x*32,y*32,32,32)
                if empty_tile not in tilelist:
                    tilelist.append(empty_tile)
            x += 1
        y += 1
# ^ nested in:  
def redraw_manager(level, screen, display_width, tilelist, normal_font, player_container, bullet_container, enemy_container):
    #render and blit text
    text = normal_font.render("Assasin HP", 1, asset.WHITE, )
    screen.blit(text, (15, 35)) 
    #blit static health bar (foreground)
    screen.blit(asset.H_BAR_IMG, (10, 50))
    #draw health bar
    for player in player_container:
        if player.health > 0: #just to make sure no leftover green bar is blitted
            health_factor = 4 * (30 - player.health)
            pygame.draw.rect(screen, asset.GREEN, (12, 52, 120 - health_factor, 10))
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
        pygame.draw.rect(screen, asset.RED, (enemy.rect.x, enemy.rect.y - 30, 60, 8))
        pygame.draw.rect(screen, asset.GREEN, (enemy.rect.x, enemy.rect.y - 30, 60 - health_factor, 8))
    #draw player using sprite container
    for player in player_container:
        player.draw(screen) 
    #draw tiles
    tile_drawer(screen, level, tilelist, asset.T_BLACK, asset.T_GRASS, asset.T_DIRT)

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

def flush(enemy_container):
    enemy_container.empty()