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
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    im = Image.open(fullname)
    pixels = im.load()
    x, y = im.size
    for i in range(x):
        for j in range(y):
            r, g, b = pixels[i, j]
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


def load_image(name: str) -> pygame.Surface:
    """Загрузка изображения из файла. return pygame.Surface с данным изображением"""
    fullname = os.path.join(IMAGES_DIRECTORY, name)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    image = image.convert_alpha()
    return image


if __name__ == '__main__':
    pygame.init()
    size = 300, 300
    screen = pygame.display.set_mode(size)
    screen.fill(pygame.Color('black'))
    load_image('player_plane.png')
    generate_new_enemy_image('player_plane.png', 'enemy2_plane.png', rewrite=True)
    generate_new_enemy_image('player_plane.png',
                             'enemy3_plane.png',
                             key=lambda x: (x[0], x[2], x[1]),
                             rewrite=True)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        pygame.display.update()
