import pygame
import os
import sys
import random
from image_processing import load_image
from entity_class import Entity
from plane_class import Plane, Player, TargetingPlane
from constants import BACKGROUND_COLOR, SCREEN_WIDTH, SCREEN_HEIGHT, LIFE_SIZE
from level_class import levels
from screens import draw_win, write_notification, draw_interface, draw_lost, draw_starting_screen


def create_enemy(all_sprites: pygame.sprite.Group,
                 player: pygame.sprite,
                 time: int,
                 black_propability: float) -> Plane:
    """Создаёт противника в случайном месте на экране. Противник атакует player
    time: время
    black_propability: вероятность появления чёрного самолёта, а не синего"""
    y = random.randrange(LIFE_SIZE, SCREEN_HEIGHT - 50)
    roll = random.random()
    if roll < black_propability:
        return TargetingPlane(all_sprites, alliance=-1, x=SCREEN_WIDTH, y=y, creation_time=time, target=player)
    return Plane(all_sprites, alliance=-1, x=SCREEN_WIDTH, y=y, creation_time=time)


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
    game_condition = 'starting_screen'
    level_number = 1
    spawn_rate = -1
    stronger_enemy_propability = 0.3  # Вероятность появления самолёта, стреляющего точно в игрока
    level_duration = 60
    while running:
        events = list(pygame.event.get())
        for event in events:
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_TAB:
                    player.hp += 5
        if game_condition == 'starting_screen':
            draw_starting_screen(screen)
            for event in events:
                if event.type == pygame.KEYDOWN  or event.type == pygame.MOUSEBUTTONDOWN:
                    game_condition = 'loading_level'
        if game_condition == 'loading_level':
            t = 0
            stronger_enemy_propability, spawn_rate, level_duration = levels[level_number].load()
            game_condition = 'level_active'
        elif game_condition == 'level_active':

            for event in events:
                if event.type == pygame.MOUSEMOTION and pygame.mouse.get_focused():
                    x, y = event.pos
                    dx, dy = player.image.get_size()
                    player.rect.topleft = x - dx // 2, max(LIFE_SIZE, y - dy // 2)
            if t % spawn_rate == 0:
                create_enemy(all_sprites, player, t, stronger_enemy_propability)
            screen.fill(pygame.Color(BACKGROUND_COLOR))
            all_sprites.draw(screen)
            draw_interface(player.hp, life_image, screen)
            all_sprites.update(t)
            clock.tick(60)
            t += 1
            if t < 90:
                write_notification(screen, f'Уровень {level_number}')
            pygame.display.flip()
            if t >= level_duration:
                game_condition = 'loading_level'
                level_number += 1
                if level_number > max(levels.keys()):
                    game_condition = 'win'
            if player.hp <= 0:
                game_condition = 'lost'
        elif game_condition == 'win':
            draw_win(screen, player)
        elif game_condition == 'lost':
            draw_lost(screen, player)

    pygame.quit()


if __name__ == '__main__':
    main()
