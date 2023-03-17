import pygame
import os
import sys
from constants import IMAGES_DIRECTORY
from PIL import Image


def generate_new_enemy_image(source: str,
                             res: str,
                             key: callable = None,
                             rewrite: bool = False,
                             flip: bool = True) -> None:
    """Создаёт новое изображение с помощью замены цветов в source.
    Записывает результат как res. Замена определяется key.
    rewrite: перезаписывать ли файл, если такой уже есть
    flip: необходимо ли отразить по горизонтали"""
    fullname = os.path.join(IMAGES_DIRECTORY, source)
    try:
        im = Image.open(fullname)
    except IOError:
        print('Cannot load image:', name)
        raise SystemExit(message)
    pixels = im.load()
    x, y = im.size
    for i in range(x):
        for j in range(y):
            r, g, b = pixels[i, j][:3]
            if abs(sum(pixels[i, j]) - sum(pixels[0, 0])) > 10:
                if not key:
                    pixels[i, j] = b, g, r
                else:
                    pixels[i, j] = key(pixels[i, j])
    if flip:
        im = im.transpose(Image.FLIP_LEFT_RIGHT)
    fullname = os.path.join(IMAGES_DIRECTORY, res)
    if not os.path.isfile(fullname) or rewrite:
        im.save(os.path.join(IMAGES_DIRECTORY, res))
    else:
        print(f'Файл с именем {fullname} уже существует. Перезапись не разрешена')


def load_image(name: str, color_key: tuple = -1) -> pygame.Surface:
    """Загрузка изображения из файла. return pygame.Surface с данным изображением
    color_key - если изображение было непрозрачным, задаём цвет фона"""
    fullname = os.path.join(IMAGES_DIRECTORY, name)
    try:
        image = pygame.image.load(fullname)
    except pygame.error as message:
        print('Cannot load image:', name)
        raise SystemExit(message)
    if color_key is not None:
        image = image.convert()
        if color_key == -1:
            color_key = image.get_at((0, 0))
        image.set_colorkey(color_key)
    else:
        image = image.convert_alpha()
    return image


if __name__ == '__main__':
    """"Создание 2 вражеских самолётов, тестирование правильной работы и отрисовки"""
    pygame.init()
    size = 300, 300
    screen = pygame.display.set_mode(size)
    screen.fill(pygame.Color('black'))
    player = load_image('player_plane.png')
    generate_new_enemy_image('player_plane.png', 'enemy_plane.png', rewrite=True)
    generate_new_enemy_image('player_plane.png',
                             'enemy2_plane.png',
                             key=lambda x: (x[2], x[2], x[1]),
                             rewrite=True)
    enemy1 = load_image('enemy_plane.png')
    enemy2 = load_image('enemy2_plane.png')
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        pygame.display.update()
        screen.blit(player, (10, 10))
        screen.blit(enemy1, (100, 10))
        screen.blit(enemy2, (100, 150))

