import pygame
import random
import asset
import functions

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)    
        self.jumpcount = 10
        self.walkcount = 0
        self.jump = False
        self.shootarrow = False
        self.mele_attack = False
        self.hit_loop = 0

    def update(self):
        functions.enemy_walk(self)
        functions.enemy_jump(self)
        

    def enemy_player_collision(self, player, enemy, damage):
        if pygame.sprite.collide_rect(player, enemy):
            if self.hit_loop == 0 and player.health > 0:
                player.health -= damage
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

        self.image = image
        self.rect = self.image.get_rect()
        self.x = x
        self.rect.x = self.x
        self.rect.y = 455
        self.y_cap = 455

        self.vel = 0
        self.jump_factor = 0
        self.walk_dynamics = 0
        self.jump_dynamics = 0

        self.damage = 0.5
        self.health = health
        self.health_cap = health

    def update(self):
        pass

    def draw(self, screen):
        screen.blit(asset.PORTAL[0], (self.rect.x, self.rect.y))
    
        #pygame.draw.rect(screen, (250,0,0), self.rect, 2)
    
class Imp(Enemy):
    def __init__(self, image, end, x, health):
        Enemy.__init__(self)

        self.image = image
        self.rect = self.image.get_rect()
        self.end = end
        self.path = [1, self.end - self.rect.width]
        self.x = x
        self.rect.x = self.x
        self.rect.y = 485
        self.y_cap = 485

        self.vel = 7
        self.jump_factor = 0.5
        self.walk_dynamics = 1
        self.jump_dynamics = 1.5

        self.damage = 1
        self.health = health
        self.health_cap = health
    
    def draw(self, screen):
        if self.walkcount + 1 == 27:
            self.walkcount = 0

        if self.vel > 1:
            screen.blit(asset.IMP_R[self.walkcount // 3], (self.rect.x, self.rect.y))
            self.walkcount += 1
        else:
            screen.blit(asset.IMP_L[self.walkcount // 3], (self.rect.x, self.rect.y))
            self.walkcount += 1
        #pygame.draw.rect(screen, (250,0,0), self.rect, 2)

class FatImp(Enemy):
    def __init__(self, image, end, x, health):
        Enemy.__init__(self)
    
        self.image = image
        self.rect = self.image.get_rect()
        self.end = end
        self.path = [1, self.end - self.rect.width]
        self.x = x
        self.rect.x = self.x
        self.rect.y = 470
        self.y_cap = 470

        self.vel = 3
        self.jump_factor = 0.1
        self.walk_dynamics = 0.5
        self.jump_dynamics = 1

        self.damage = 3
        self.health = health
        self.health_cap = health

    def draw(self, screen):
        if self.walkcount + 1 == 27:
            self.walkcount = 0

        if self.vel > 1:
            screen.blit(asset.FAT_IMP_R[self.walkcount // 3], (self.rect.x, self.rect.y))
            self.walkcount += 1
        else:
            screen.blit(asset.FAT_IMP_L[self.walkcount // 3], (self.rect.x, self.rect.y))
            self.walkcount += 1
        #pygame.draw.rect(screen, (250,0,0), self.rect, 2)
