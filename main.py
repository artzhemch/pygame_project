import pygame
import os
import sys
import random
from image_processing import load_image
from entity_class import Entity
from plane_class import Plane, Player, TargetingPlane
from constants import BACKGROUND_COLOR, SCREEN_WIDTH, SCREEN_HEIGHT, LIFE_SIZE


def draw_interface(life: int, life_image: pygame.Surface, screen: pygame.display, score: int):
    pygame.draw.rect(screen, (255, 255, 255, 120), (0, 0, SCREEN_WIDTH, LIFE_SIZE))
    for i in range(life):
        screen.blit(life_image, (i * LIFE_SIZE, 0))
    myfont = pygame.font.SysFont("monospace", 20)
    label = myfont.render(f"Score: {score}", True, (0, 0, 0))
    screen.blit(label, (SCREEN_WIDTH - label.get_size()[0] - 10, 10))


def create_enemy(all_sprites: pygame.sprite.Group, player: pygame.sprite, time: int) -> Plane:
    """Создаёт противника в случайном месте на экране. Противник атакует player"""
    y = random.randrange(50, SCREEN_HEIGHT - 50)
    return TargetingPlane(all_sprites, alliance=-1, x=SCREEN_WIDTH, y=y, creation_time=time, target=player)


def main():
    pygame.init()
    size = SCREEN_WIDTH, SCREEN_HEIGHT
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode(size)
    all_sprites = pygame.sprite.Group()
    Entity.all_sprites = all_sprites
    life_image = pygame.transform.scale(load_image('heart.png'), (LIFE_SIZE, LIFE_SIZE))

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
                player.rect.topleft = x - dx // 2, max(LIFE_SIZE, y - dy // 2)
        if t % 10 == 0:
            x = create_enemy(all_sprites, player, t)
            x.fire()
        screen.fill(pygame.Color(BACKGROUND_COLOR))
        all_sprites.draw(screen)
        draw_interface(player.hp, life_image, screen, 0)
        all_sprites.update(t)
        pygame.display.flip()
        clock.tick(60)
        t += 1

    pygame.quit()


if __name__ == '__main__':
    main()
