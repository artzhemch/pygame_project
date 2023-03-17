import pygame
import os
import sys
from entity_class import Entity
from plane_class import Plane, Player
from constants import BACKGROUND_COLOR, WIDTH, HEIGHT


def main():
    pygame.init()
    size = WIDTH, HEIGHT
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode(size)
    all_sprites = pygame.sprite.Group()
    Entity.all_sprites = all_sprites

    Plane(all_sprites, x=100, y=400)
    Plane(all_sprites, alliance=-1, x=100, y=100, v_x=0, v_y=5)
    player = Player(all_sprites, x=0, y=0)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEMOTION:
                x, y = event.pos
                player.rect.topleft = x - 50, y - 50
        screen.fill(pygame.Color(BACKGROUND_COLOR))
        all_sprites.draw(screen)
        all_sprites.update()
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()


if __name__ == '__main__':
    main()