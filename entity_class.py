import pygame
from image_processing import load_image
import random
from collections import defaultdict


class Entity(pygame.sprite.Sprite):
    """Класс для всех сущностей"""
    score = 0
    image = None  # Изображение для всех экземпляров класса
    image_name = 'player_plane.png'  # Имя изображения
    all_sprites = None  # Все спрайты
    sprite_groups = defaultdict(pygame.sprite.Group)  # Группы спрайтов по alliance

    def __init__(self,
                 *group,
                 alliance: int = 0,
                 x: int,
                 y: int,
                 v_x: int = 0,
                 v_y: int = 0,
                 hp: int = -1,
                 creation_time: int = 0,
                 collision_damage: int = 0):
        """alliance: какой команде принадлежит объект,
        x, y: координаты исходной точки,
        v_x, v_y: скорости,
        hp: сколько урона может выдержать,
        collision_dmg: урон от столкновения
        creation_time: время создания (в тиках)"""
        super().__init__(*group)
        if not self.__class__.image:
            self.__class__.image = load_image(self.__class__.image_name)
        self.add(Entity.sprite_groups[alliance])
        # if not Entity.all_sprites:
        #     Entity.all_sprites = pygame.sprite.Group(group)
        self.image = self.__class__.image
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = x, y
        self.v_x = v_x
        self.v_y = v_y
        self.alliance = alliance
        self.collision_damage = collision_damage
        self.hp = hp
        self.creation_time = creation_time

    def update(self, t: int):
        self.rect = self.rect.move(self.v_x, self.v_y)
        for ally, sprite_group in Entity.sprite_groups.items():
            if ally == self.alliance:
                continue
            collides = pygame.sprite.spritecollide(self, sprite_group, False)
            if len(collides) > 0:
                for i in collides:
                    self.get_hit(i)
        if self.rect.x < -100 or self.rect.x > 1000:
            self.recycle()

    def get_hit(self, other):
        """Столкновение с другим объектом"""
        if self is other:
            return
        self.rect = self.rect.move(1, 0)
        self.receive_damage(other.collision_damage)
        other.receive_damage(self.collision_damage)

    def receive_damage(self, damage: int):
        self.hp -= damage
        if self.hp <= 0:
            self.get_destroyed()

    def get_destroyed(self):
        """Уничтожение объекта (игроком)"""
        self.recycle()

    def get_coordinates(self) -> tuple[int, int]:
        return self.rect.x, self.rect.y

    def recycle(self):
        """Удаление объекта"""
        Entity.sprite_groups[self.alliance].remove(self)
        Entity.all_sprites.remove(self)
