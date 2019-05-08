import pygame
import asset
import functions

class Player(pygame.sprite.Sprite):
    def __init__(self, image):
        pygame.sprite.Sprite.__init__(self)
        #rect variables
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.y = 460
        self.rect_y_cap = 460
        self.rect.x = 1
        #movement variables
        self.vel = 6
        self.jump = False
        self.jumpcount = 12
        self.jumpcount_cap = 12
        self.jumpblocker = 0
        self.left = False
        self.right = True
        self.walkblocker = 0
        #combat variables
        self.shoot_bullet = False
        self.throwblocker = 0
        self.attack = False
        self.meleblocker = 0
        self.weapon_damage = 1
        self.health = 30
        self.health_cap = 30
        self.deathblocker = 0
        self.hit_loop = 0


    def draw(self, screen):
        if self.left:
            functions.identify_death(self, screen, 0)
            functions.identify_jump_attack(self, screen, 0)
            functions.identify_jump_throw(self, screen, 0)
            functions.identify_jump(self, screen, 0)
            functions.identify_attack(self, screen, 0)
            functions.identify_throw(self, screen, 0)
            functions.identify_walk(self, screen, 0)
                
        else:
            functions.identify_death(self, screen, 1)
            functions.identify_jump_attack(self, screen, 1)
            functions.identify_jump_throw(self, screen, 1)
            functions.identify_jump(self, screen, 1)
            functions.identify_attack(self, screen, 1)
            functions.identify_throw(self, screen, 1)
            functions.identify_walk(self, screen, 1)

        #pygame.draw.rect(screen, (250,0,0), self.rect, 2)
    
    def mele_enemy_collision(self, player, enemy_container):
        if self.attack == True:
            for enemy in enemy_container:
                if pygame.sprite.collide_rect(player, enemy):
                    enemy.health -= self.weapon_damage
