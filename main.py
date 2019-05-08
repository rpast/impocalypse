import pygame 
import os 
import random 
import asset 
import functions
from asset import Block
from player import Player
from enemy import Portal, Imp, FatImp
from bullet import Bullet

# SCENE LOGIC ###
class SceneBase:
    '''
    Centralized Scene framework
    ProcessInput - This method will receive all the events that happened since the last frame.
    Update - Put your game logic in here for the scene.
    Render - Put your render code here. It will receive the main screen Surface as input.
    '''

    def __init__(self):
        self.next = self
        self.shoot_loop = 0
        self.attack_loop = 0
    
    def ProcessInput(self, events, key, player):
        print("uh-oh, you didn't override this in the child class")

    def Update(self, player):
        #self.player = player
        print("uh-oh, you didn't override this in the child class")

    def Render(self, screen):
        print("uh-oh, you didn't override this in the child class")

    def SwitchToScene(self, next_scene):
        self.next = next_scene
    
    def Terminate(self):
        self.SwitchToScene(None)

class TitleScene(SceneBase):
    def __init__(self):
        SceneBase.__init__(self)
    
    def ProcessInput(self, events, key, player):
        for event in events:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                # Move to the next scene when the user pressed Enter
                self.SwitchToScene(GameScene1())
    
    def Update(self, player):
        pass
    
    def Render(self, screen, font, smallfont):
        screen.fill((0, 0, 0))
        text1 = font.render("IMPS & ASSASIN", 1, (250, 250, 250), )
        screen.blit(text1, (320, 250))

class GameScene1(SceneBase):
    def __init__(self):
        SceneBase.__init__(self)
        self.imp_cap = 1
        self.fat_cap = 1
        self.acid_cap = 0
        self.mama_cap = 0
        self.full = False
        self.transition = False
        self.game_over = False
        
    def ProcessInput(self, events, key, player):
        if self.transition == True:
            for event in events:
                if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                    # Move to the next scene when the user pressed Enter
                    self.SwitchToScene(GameScene2())

        if self.game_over == True:
            for event in events:
                if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                    # Move to the first scene when the user pressed Enter
                    self.SwitchToScene(TitleScene())
                    player.health = player.health_cap

        if self.full == False:
            functions.enemy_generator(2, 1, 0, 0, self.imp_cap, self.fat_cap, self.acid_cap, self.mama_cap)
            self.full = True

        if player.health > 0:
            functions.movement_manager(player)
            functions.jump_manager(player)
        
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

    def Update(self, player):
        functions.collision_manager(asset.PLAYER_GROUP, asset.BULLET_GROUP, asset.ENEMY_GROUP, asset.BLOCK_GROUP)
        functions.death_manager(asset.ENEMY_GROUP)        

    def Render(self, screen, font, smallfont):
        # The game scene is just a blank blue screen
        functions.redraw_manager(screen, asset.BG[0], font, asset.PLAYER_GROUP, asset.BULLET_GROUP, asset.ENEMY_GROUP)

        for player in asset.PLAYER_GROUP:
            if player.health <= 0:
                functions.game_over_message(screen, font, smallfont)
                self.game_over = True

        if len(asset.ENEMY_GROUP) == 0:
            functions.transition_message(screen, font, smallfont)
            self.transition = True

class GameScene2(SceneBase):
    def __init__(self):
        SceneBase.__init__(self)
        self.imp_cap = 2
        self.fat_cap = 2
        self.acid_cap = 0
        self.mama_cap = 0
        self.full = False
        self.transition = False
        self.game_over = False
        
    def ProcessInput(self, events, key, player):
        if self.transition == True:
            for event in events:
                if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                    # Move to the next scene when the user pressed Enter
                    self.SwitchToScene(CreditsScene())

        if self.game_over == True:
            for event in events:
                if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                    # Move to the first scene when the user pressed Enter
                    self.SwitchToScene(TitleScene())
                    player.health = player.health_cap

        if self.full == False:
            functions.enemy_generator(2, 1, 0, 0, self.imp_cap, self.fat_cap, self.acid_cap, self.mama_cap)
            self.full = True

        if player.health > 0:
            functions.movement_manager(player)
            functions.jump_manager(player)
        
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

    def Update(self, player):
        functions.collision_manager(asset.PLAYER_GROUP, asset.BULLET_GROUP, asset.ENEMY_GROUP, asset.BLOCK_GROUP)
        functions.death_manager(asset.ENEMY_GROUP)
        
    def Render(self, screen, font, smallfont):
        # The game scene is just a blank blue screen
        functions.redraw_manager(screen, asset.BG[1], font, asset.PLAYER_GROUP, asset.BULLET_GROUP, asset.ENEMY_GROUP)
        
        for player in asset.PLAYER_GROUP:
            if player.health <= 0:
                functions.game_over_message(screen, font, smallfont)
                self.game_over = True

        if len(asset.ENEMY_GROUP) == 0:
            functions.transition_message(screen, font, smallfont)
            self.transition = True

class CreditsScene(SceneBase):
    def __init__(self):
        SceneBase.__init__(self)
    
    def ProcessInput(self, events, key, player):
        for event in events:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                # Move to the next scene when the user pressed Enter
                self.SwitchToScene(GameScene1())
    
    def Update(self, player):
        player.health = player.health_cap
    
    def Render(self, screen, font, smallfont):
        screen.fill((0, 0, 0))
        text = font.render("IMPS & ASSASIN", 1, (250, 250, 250), )
        screen.blit(text, (320, 250))

functions.run_game(800, 600, 27, TitleScene())
