import pygame
#import asset


class Player(pygame.sprite.Sprite):
    def __init__(self, image):
        pygame.sprite.Sprite.__init__(self)
        #rect variables
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.y = 200
        self.rect_y_cap = 200
        self.rect.x = 1
        #movement variables
        self.vel = 3
        self.left = False
        self.right = False
        self.scrolling_x = 1
        self.y_momentum = 0
        self.air_timer = 0
        self.vertical_momentum = 0
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
        screen.blit(self.image, (self.rect.x, self.rect.y))
        #if self.left:
        #    functions.animate_death(self, screen, 0)
        #    functions.death_fall(self)
        #    functions.animate_jump_attack(self, screen, 0)
        #    functions.animate_jump_throw(self, screen, 0)
        #    functions.animate_jump(self, screen, 0)
        #    functions.animate_attack(self, screen, 0)
        #    functions.animate_throw(self, screen, 0)
        #    functions.animate_walk(self, screen, 0)
        #        
        #else:
        #    functions.animate_death(self, screen, 1)
        #    functions.death_fall(self)
        #    functions.animate_jump_attack(self, screen, 1)
        #    functions.animate_jump_throw(self, screen, 1)
        #    functions.animate_jump(self, screen, 1)
        #    functions.animate_attack(self, screen, 1)
        #    functions.animate_throw(self, screen, 1)
        #    functions.animate_walk(self, screen, 1)

        #pygame.draw.rect(screen, (250,0,0), (self.rect.x, self.rect.y, 32, 32), 2)
    
    def mele_enemy_collision(self, player, enemy_container):
        #for enemy in enemy_container:
        #    if self.rect.y > enemy.rect.y - self.rect.top:
        #        self.y_momentum = -self.y_momentum
        #    else:
        #        self.y_momentum += 0.2
        #    self.rect.y += self.y_momentum

        if self.attack == True:
            for enemy in enemy_container:
                if pygame.sprite.collide_rect(player, enemy):
                    enemy.health -= self.weapon_damage
