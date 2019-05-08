import pygame


class Bullet(pygame.sprite.Sprite):
    def __init__(self, image, player_x, player_y, damage, orientation):   
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
        self.vel = 20
        self.orientation = orientation
        self.damage = damage

    def bullet_update(self): 
        self.rect.x += self.vel * self.orientation

    def bullet_enemy_collision(self, bullet_container, enemy_container):
        for enemy in enemy_container:
            if pygame.sprite.spritecollide(enemy, bullet_container, 1, 0):
                enemy.health -= self.damage
                #print("ENEMY HEALTH =", enemy.health)

    def bullet_block_collision(self, bullet_container, block_container):
        if pygame.sprite.groupcollide(bullet_container, block_container, 1, 0):
            pass