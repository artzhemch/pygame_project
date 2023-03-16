import pygame
import os
import sys
from entity_class import Entity
from plane_class import Plane
from constants import BACKGROUND_COLOR, WIDTH, HEIGHT


def main():
    pygame.init()
    size = WIDTH, HEIGHT
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode(size)
    all_sprites = pygame.sprite.Group()
    for i in range(3):
        # Entity(all_sprites)
        Plane(all_sprites, x=100, y=100 * i, v_x=0, v_y=-3 + 2 * i)
    Plane(all_sprites, x=100, y=100, v_x=0, v_y=5)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill(pygame.Color(BACKGROUND_COLOR))
        all_sprites.draw(screen)
        all_sprites.update()
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()


if __name__ == '__main__':
    main()