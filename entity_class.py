import pygame
from image_processing import load_image
import random
from collections import defaultdict

class Entity(pygame.sprite.Sprite):
    """Класс для всех сущностей"""
    image = None  # Изображение для всех экземпляров класса
    image_name = 'player_plane.png'  # Имя изображения
    all_sprites = None  # Все спрайты
    sprite_groups = defaultdict(pygame.sprite.Group)  # Группы спрайтов по alliance

    def __init__(self, *group, alliance: int = 0, x: int, y: int, v_x: int = 0, v_y: int = 0):
        """alliance: какой команде принадлежит объект
        x, y: координаты исходной точки
        v_x, v_y: скорости"""
        super().__init__(*group)
        print(self.__class__)
        if not self.__class__.image:
            self.__class__.image = load_image(self.__class__.image_name)
        self.add(Entity.sprite_groups[alliance])
        if not Entity.all_sprites:
            Entity.all_sprites = group
        self.image = self.__class__.image
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = x, y
        self.v_x = v_x
        self.v_y = v_y
        self.alliance = alliance

    def update(self):
        self.rect = self.rect.move(self.v_x, self.v_y)
        for ally, sprite_group in Entity.sprite_groups.items():
            if ally == self.alliance:
                pass
                #continue
            collides = pygame.sprite.spritecollide(self, sprite_group, False)
            if len(collides) > 1:
                for i in collides:
                    print(i)
                    self.get_hit(i)
                #self.rect = self.rect.move(10, 10)

    def get_hit(self, other):
        if self is other:
            return
        self.rect = self.rect.move(1, 0)
        pass
        #for i in pygame.sprite.spritecollide(self, Entity.all_sprites, False):
        #    print(i)




