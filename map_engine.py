import pygame, asset

class Map():
    def __init_(self, level):
        self.level = level
        self.tile_list = []

    def draw(self, screen, tile1=0, tile2=0, tile3=0, tile4=0, tile5=0):
        y = 0
        for layer in self.level:
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
                    self.tile_list.append(pygame.Rect(x*32,y*32,32,32))
                x += 1
            y += 1


