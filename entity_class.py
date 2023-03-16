import pygame
from image_processing import load_image
import random


class Entity(pygame.sprite.Sprite):
    """Класс для всех сущностей"""
    image = None  # Изображение для всех экземпляров класса
    image_name = 'player_plane.png'

    def __init__(self, *group, alliance: int = 0, x: int, y: int, v_x: int = 0, v_y: int = 0):
        """alliance: какой команде принадлежит объект
        x, y: координаты исходной точки
        v_x, v_y: скорости"""
        super().__init__(*group)
        print(self.__class__)
        if not self.__class__.image:
            self.__class__.image = load_image(self.__class__.image_name)
        self.image = self.__class__.image
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = x, y
        self.v_x = v_x
        self.v_y = v_y

    def update(self):
        self.rect.x -= self.v_x
        self.rect.y -= self.v_y



