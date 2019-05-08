import pygame, os, random, asset, functions
from player import Player
from enemy import Portal, Imp, FatImp
from bullet import Bullet

# SCENE LOGIC ###
class SceneBase():
    '''
    Centralized Scene framework
    :ProcessInput: This method will receive all the events that happened since the last frame.
    :Update: Put your game logic in here for the scene.
    :Render: Put your render code here. It will receive the main screen Surface as input.
    '''

    def __init__(self):
        self.next = self
        self.shoot_loop = 0
        self.attack_loop = 0
        self.transition = False
        self.game_over = False
        
    def ProcessInput(self, events, key):
        print("uh-oh, you didn't override this in the child class")

    def Update(self):
        print("uh-oh, you didn't override this in the child class")

    def Render(self, screen, font):
        print("uh-oh, you didn't override this in the child class")

    def SwitchToScene(self, next_scene):
        self.next = next_scene
    
    def Terminate(self):
        self.SwitchToScene(None)

class TitleScene(SceneBase):
    def __init__(self):
        SceneBase.__init__(self)
    
    def ProcessInput(self, events, key, player_container, screen, stage_position):
        #define how to switch to the next scene 
        for event in events:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                # Move to the next scene when the user pressed Enter
                self.SwitchToScene(GameScene1(1))
        
    def Update(self):
        pass
    
    def Render(self, screen, font):
        #render welcome screen
        screen.fill(asset.BLACK)
        text1 = font[0].render("IMPOCALYPSE", 0, asset.WHITE, )
        screen.blit(text1, (210, 170))


class GameScene1(SceneBase):
    def __init__(self, level):
        #Inherit base scene, define enemy limit for each species
        SceneBase.__init__(self)
        self.imp_cap = 1
        self.fat_cap = 1
        self.acid_cap = 0
        self.mama_cap = 0
        self.full = False
        self.level = level
        self.tile_list = []
    
    def ProcessInput(self, events, key, player_container, screen, stage_position):
        #Define conditions for sene transition
        if self.transition == True:
            for event in events:
                if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                    # Move to the next scene when the user pressed Enter
                    self.SwitchToScene(GameScene2(2))
        #Define game over handler
        if self.game_over == True:
            for event in events:
                if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                    # Move to the first scene when the user pressed Enter
                    self.SwitchToScene(CreditsScene())
                    self.game_over = False
        #Populate the screen with enemies            
        #if self.full == False:
        #    functions.enemy_generator(1, 1, 0, 0, self.imp_cap, self.fat_cap, self.acid_cap, self.mama_cap)
        #    self.full = True

        for player in player_container:
            if player.health > 0:
                #Handle player movement
                functions.movement_manager(player, self.tile_list, asset.DISPLAY_W, screen, self.level, stage_position)

                #Handle player attacks delayed by counters
                if self.attack_loop == 0:
                    functions.attack_manager(player)
                self.attack_loop += 1
                if self.attack_loop == 3:
                    self.attack_loop = 0

                if self.shoot_loop == 0:
                    functions.shooting_manager(player)
                self.shoot_loop += 1
                if self.shoot_loop == 5:
                    self.shoot_loop = 0

    def Update(self):
        #Handle collisions and deaths
        functions.collision_manager(asset.PLAYER_GROUP, asset.BULLET_GROUP, asset.ENEMY_GROUP, asset.WALL_GROUP)
        functions.death_manager(asset.ENEMY_GROUP)        

    def Render(self, screen, font):
        # render the game scene
        functions.redraw_manager(self.level, screen, asset.WINDOW_W, self.tile_list, font[1], asset.PLAYER_GROUP, asset.BULLET_GROUP, asset.ENEMY_GROUP)

        for player in asset.PLAYER_GROUP:
            if player.health <= 0:
                functions.game_over_message(screen, font[1], font[2])
                self.game_over = True

        #if len(asset.ENEMY_GROUP) == 0:
        #    functions.transition_message(screen, normal_font, small_font)
        #    self.transition = True

class GameScene2(SceneBase):
    def __init__(self, level):
        #Inherit base scene, define enemy limit for each species
        SceneBase.__init__(self)
        self.imp_cap = 2
        self.fat_cap = 2
        self.acid_cap = 0
        self.mama_cap = 0
        self.full = False
        self.level = level
        self.tile_list = []
        
    def ProcessInput(self, events, key, player_container, screen, stage_position):
        #Define conditions for sene transition
        if self.transition == True:
            for event in events:
                if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                    # Move to the next scene when the user pressed Enter
                    self.SwitchToScene(CreditsScene())
        #Define game over handler
        if self.game_over == True:
            for event in events:
                if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                    # Move to the first scene when the user pressed Enter
                    self.SwitchToScene(CreditsScene())
                    self.game_over = False
        #Populate the screen with enemies  
        #if self.full == False:
        #    functions.enemy_generator(2, 1, 0, 0, self.imp_cap, self.fat_cap, self.acid_cap, self.mama_cap)
        #    self.full = True
        
        for player in player_container:
            if player.health > 0:

                #Handle player movement
                functions.movement_manager(player, self.tile_list, asset.DISPLAY_W, screen, self.level, stage_position)

                #Handle player attacks delayed by counters
                if self.attack_loop == 0:
                    functions.attack_manager(player)
                self.attack_loop += 1
                if self.attack_loop == 3:
                    self.attack_loop = 0
                    
                if self.shoot_loop == 0:
                    functions.shooting_manager(player)
                self.shoot_loop += 1
                if self.shoot_loop == 5:
                    self.shoot_loop = 0

    def Update(self):
        #Handle collisions and deaths
        functions.collision_manager(asset.PLAYER_GROUP, asset.BULLET_GROUP, asset.ENEMY_GROUP, asset.WALL_GROUP)
        functions.death_manager(asset.ENEMY_GROUP)
        
    def Render(self, screen, font):
        # The game scene is just a blank blue screen
        functions.redraw_manager(self.level, screen, asset.WINDOW_W, self.tile_list, font[1], asset.PLAYER_GROUP, asset.BULLET_GROUP, asset.ENEMY_GROUP)
        
        for player in asset.PLAYER_GROUP:
            if player.health <= 0:
                functions.game_over_message(screen, font[1], font[2])
                self.game_over = True

        #if len(asset.ENEMY_GROUP) == 0:
        #    functions.transition_message(screen, normal_font, small_font)
        #    self.transition = True

class CreditsScene(SceneBase):  
    def __init__(self):
        SceneBase.__init__(self)
    
    def ProcessInput(self, events, key):
        for event in events:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                # Move to the next scene when the user pressed Enter
                    self.SwitchToScene(GameScene1())
    
    def Update(self):
        #Reset player health
        for player in asset.PLAYER_GROUP:
            player.health = player.health_cap

        functions.flush(asset.ENEMY_GROUP)
    
    def Render(self, screen, font):
        #Draw end screen
        screen.fill(asset.BLACK)
        text1 = font[0].render("IMPOCALYPSE", 1, asset.WHITE)
        text2 = font[2].render("Assets used:", 1, asset.WHITE)
        text3 = font[2].render("Art: PixElthen, edermunizz, acewaydev", 1, asset.WHITE)
        screen.blit(text1, (210, 170))
        screen.blit(text2, (210, 200))
        screen.blit(text3, (210, 220))


#kazda scena bedzie roznic sie:
#iloscia i rodzajem potworów
#tłem
#blokalmi 
#przedmiotami

functions.run_game(asset.WINDOW_SIZE, 60, TitleScene())
