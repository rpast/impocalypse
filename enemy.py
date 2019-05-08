import pygame
import random
import asset
import functions

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)   
        #general enemy variables 
        self.jumpcount = 10
        self.walkblocker = 0
        self.jump = False
        self.shoot_bullet = False
        self.mele_attack = False
        self.hit_loop = 0

    def update(self):
        functions.animate_enemy_walk(self)
        functions.animate_enemy_jump(self)
        
    def enemy_player_collision(self, player, enemy, damage):
        if pygame.sprite.collide_rect(player, enemy):
            if self.hit_loop == 0 and player.health > 0:
                pass
                #player.health -= damage
                #print(f"*PLAYER HEALTH = {self.health}*")
            self.hit_loop += 1
            self.mele_attack = True
            
        if self.hit_loop > 0:
            self.hit_loop += 1
            if self.hit_loop > 30:
                self.hit_loop = 0
                self.mele_attack = False

class Portal(Enemy):
    def __init__(self, image, x, health):
        Enemy.__init__(self)
        #rect variables
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = 455
        self.y_cap = 455
        #movement variables
        self.vel = 0
        self.jump_factor = 0
        self.walk_dynamics = 0
        self.jump_dynamics = 0
        #attack variables
        self.damage = 0.5
        self.health = health
        self.health_cap = health

    def update(self):
        pass

    def draw(self, screen):
        screen.blit(asset.PORTAL[0], (self.rect.x, self.rect.y))
        pygame.draw.rect(screen, (250,0,0), self.rect, 2)
    
class Imp(Enemy):
    def __init__(self, image, end, x, health):
        Enemy.__init__(self)
        #rect variables
        self.image = image
        self.rect = self.image.get_rect()
        self.path = [1, end - self.rect.width]
        self.rect.x = x
        self.rect.y = 485
        self.y_cap = 485
        #movement variables
        self.vel = 7
        self.jump_factor = 0.5
        self.walk_dynamics = 1
        self.jump_dynamics = 1.5
        #attack variables
        self.damage = 1
        self.health = health
        self.health_cap = health
    
    def draw(self, screen):
        functions.animate_species(self, screen, self.vel, 0)
        pygame.draw.rect(screen, (250,0,0), self.rect, 2)

class FatImp(Enemy):
    def __init__(self, image, end, x, health):
        Enemy.__init__(self)
        #rect variables
        self.image = image
        self.rect = self.image.get_rect()
        self.path = [1, end - self.rect.width]
        self.rect.x = x
        self.rect.y = 470
        self.y_cap = 470
        #movement variables
        self.vel = 3
        self.jump_factor = 0.1
        self.walk_dynamics = 0.5
        self.jump_dynamics = 1
        #attack variables
        self.damage = 3
        self.health = health
        self.health_cap = health

    def draw(self, screen):
        functions.animate_species(self, screen, self.vel, 1)
        pygame.draw.rect(screen, (250,0,0), self.rect, 2)
