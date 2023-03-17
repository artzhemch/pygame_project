from entity_class import Entity
from image_processing import load_image
from constants import DEFAULT_ENEMY_SPEED, DEFAULT_HP, \
    PLAYER_HP, PROJ_SPEED, DEFAULT_RATE_OF_FIRE, HERO_RATE_OF_FIRE
from projectile_class import Projectile
from math import cos, sin


class Plane(Entity):
    """Класс самолёта. Передвигается и стреляет"""
    image_name = 'enemy_plane.png'
    projectile_name = 'bullet.png'
    projectile_image = None

    def __init__(self, *group,
                 alliance: int = 0,
                 x: int,
                 y: int,
                 hp: int = DEFAULT_HP,
                 collision_damage: int = 1,
                 v_x: int = DEFAULT_ENEMY_SPEED[0],
                 v_y: int = DEFAULT_ENEMY_SPEED[1],
                 bullet_speed: tuple[int, int] = (-PROJ_SPEED, 0),
                 fire_rate: int = DEFAULT_RATE_OF_FIRE,
                 creation_time: int = 0):
        """alliance: какой команде принадлежит объект
        x, y: координаты исходной точки
        v_x, v_y: скорости
        hp: кол-во жизней самолёта,
        collision_damage: урон от столкновения
        bullet_speed: скорость полёта снаряда
        fire_rate: скорострельность (выстрел раз в fire_rate кадров)"""
        if not self.__class__.projectile_image:
            self.__class__.projectile_image = load_image(self.__class__.projectile_name)
        super().__init__(*group, alliance=alliance,
                         x=x, y=y, v_x=v_x,
                         v_y=v_y, hp=hp, collision_damage=collision_damage,
                         creation_time=creation_time)
        self.bullet_speed = bullet_speed
        self.fire_rate = fire_rate
        # self.fire()

    def fire(self):
        """Выстрел перед собой"""
        x, y = self.rect.size
        try:
            proj_w, proj_h = Projectile.image.size
        except AttributeError:
            proj_w, proj_h = 24, 24
        proj_rect = self.rect.move(-30, y // 2 - proj_h // 2)
        Projectile(Entity.all_sprites,
                   alliance=self.alliance,
                   x=proj_rect.x,
                   y=proj_rect.y,
                   v_x=self.bullet_speed[0],
                   v_y=self.bullet_speed[1])

    def get_destroyed(self):
        Entity.score += 1
        super().get_destroyed()

    def update(self, t):
        super().update(t)
        if (t - self.creation_time) % self.fire_rate == 0:
            self.fire()


class Player(Plane):
    """Класс игрока"""
    image_name = 'player_plane.png'
    image = None

    def __init__(self, *group,
                 alliance: int = 1,
                 x: int,
                 y: int,
                 hp: int = PLAYER_HP,
                 collision_damage: int = 999,
                 v_x: int = 0,
                 v_y: int = 0,
                 bullet_speed: tuple[int, int] = (PROJ_SPEED, 0),
                 fire_rate: int = HERO_RATE_OF_FIRE,
                 creation_time: int = 0):
        super().__init__(*group,
                         alliance=alliance,
                         x=x,
                         y=y,
                         v_x=v_x,
                         v_y=v_y,
                         hp=hp,
                         collision_damage=collision_damage,
                         bullet_speed=bullet_speed,
                         fire_rate=fire_rate,
                         creation_time=creation_time)

    def fire(self):
        """Выстрел перед собой"""
        x, y = self.rect.size
        try:
            proj_w, proj_h = Projectile.image.size
        except AttributeError:
            proj_w, proj_h = 24, 24
        proj_rect = self.rect.move(100, y // 2 - proj_h // 2)
        Projectile(Entity.all_sprites,
                   alliance=self.alliance,
                   x=proj_rect.x,
                   y=proj_rect.y,
                   v_x=self.bullet_speed[0],
                   v_y=self.bullet_speed[1])


class TargetingPlane(Plane):
    """Самолёт, стреляющий в конкретный объект по диагонали"""
    image_name = 'enemy2_plane.png'
    projectile_name = 'bullet.png'
    projectile_image = None
    image = None

    def __init__(self, *group,
                 alliance: int = 0,
                 x: int,
                 y: int,
                 hp: int = DEFAULT_HP,
                 collision_damage: int = 1,
                 v_x: int = DEFAULT_ENEMY_SPEED[0],
                 v_y: int = DEFAULT_ENEMY_SPEED[1],
                 bullet_speed: tuple[int, int] = (PROJ_SPEED, 0),
                 fire_rate: int = DEFAULT_RATE_OF_FIRE * 4,
                 creation_time: int = 0,
                 target: Entity):
        """bullet_speed: модуль скорости снаряда
        target: цель, в которую будет осуществляться стрельба"""
        self.target = target
        super().__init__(*group, alliance=alliance,
                         x=x, y=y, v_x=v_x,
                         v_y=v_y, hp=hp, collision_damage=collision_damage,
                         fire_rate=fire_rate, bullet_speed=bullet_speed,
                         creation_time=creation_time)

    def fire(self):
        x, y = self.rect.size
        try:
            proj_w, proj_h = Projectile.image.size
        except AttributeError:
            proj_w, proj_h = 24, 24
        proj_rect = self.rect.move(-30, y // 2 - proj_h // 2)
        bullet_speed_abs = int(sum(x ** 2 for x in self.bullet_speed) ** 0.5)  # Модуль скорости снаряда
        target_x, target_y = self.target.get_coordinates()
        plane_x, plane_y = self.get_coordinates()
        dx = target_x - plane_x
        dy = target_y - plane_y
        v_x = min(-10, int(bullet_speed_abs * (dx / (dx ** 2 + dy ** 2) ** 0.5)))
        v_y = int(bullet_speed_abs * (dy / (dx ** 2 + dy ** 2) ** 0.5))

        Projectile(Entity.all_sprites,
                   alliance=self.alliance,
                   x=proj_rect.x,
                   y=proj_rect.y,
                   v_x=v_x,
                   v_y=v_y)
