from entity_class import Entity
from image_processing import load_image
from constants import DEFAULT_ENEMY_SPEED, DEFAULT_HP, PLAYER_HP
from projectile_class import Projectile


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
                 v_y: int = DEFAULT_ENEMY_SPEED[1]):
        """alliance: какой команде принадлежит объект
        x, y: координаты исходной точки
        v_x, v_y: скорости
        hp: кол-во жизней самолёта,
        collision_damage: урон от столкновения"""
        if not self.__class__.projectile_image:
            self.__class__.projectile_image = load_image(self.__class__.projectile_name)
        super().__init__(*group, alliance=alliance,
                         x=x, y=y, v_x=v_x,
                         v_y=v_y, hp=hp, collision_damage=collision_damage)
        self.fire()

    def fire(self):
        Projectile(Entity.all_sprites, alliance=self.alliance, x=self.rect.x, y=self.rect.y)


class Player(Plane):
    image_name = 'player_plane.png'
    image = None

    def __init__(self, *group,
                 alliance: int = 1,
                 x: int,
                 y: int,
                 hp: int = PLAYER_HP,
                 collision_damage: int = 999,
                 v_x: int = 0,
                 v_y: int = 0):
        super().__init__(*group, alliance=alliance,
                         x=x, y=y, v_x=v_x,
                         v_y=v_y, hp=hp, collision_damage=collision_damage)