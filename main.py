import pygame
import os
import sys
import random
from entity_class import Entity
from plane_class import Plane, Player
from constants import BACKGROUND_COLOR, SCREEN_WIDTH, SCREEN_HEIGHT


def create_enemy(all_sprites: pygame.sprite.Group) -> Plane:
    """Создаёт противника в случайном месте на экране"""
    y = random.randrange(50, SCREEN_HEIGHT - 50)
    return Plane(all_sprites, alliance=-1, x=SCREEN_WIDTH, y=y)


def main():
    pygame.init()
    size = SCREEN_WIDTH, SCREEN_HEIGHT
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode(size)
    all_sprites = pygame.sprite.Group()
    Entity.all_sprites = all_sprites
    player = Player(all_sprites, alliance=1, x=0, y=0)
    running = True
    t = 0
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEMOTION and pygame.mouse.get_focused():
                x, y = event.pos
                dx, dy = player.image.get_size()
                player.rect.topleft = x - dx // 2, y - dy // 2
        if t % 10 == 0:
            x = create_enemy(all_sprites)
            x.fire()
        screen.fill(pygame.Color(BACKGROUND_COLOR))
        all_sprites.draw(screen)
        all_sprites.update(t)
        pygame.display.flip()
        clock.tick(60)
        print(len(all_sprites))
        t += 1

    pygame.quit()


if __name__ == '__main__':
    main()