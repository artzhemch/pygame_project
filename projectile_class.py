from entity_class import Entity
from image_processing import load_image


class Projectile(Entity):
    """Класс снаряда"""
    image_name = 'bullet.png'
    image = None

    def __init__(self,
                 *group,
                 alliance: int = 0,
                 x: int,
                 y: int,
                 v_x: int = -10,
                 v_y: int = 0,
                 collision_damage: int = 1):
        super().__init__(*group, alliance=alliance, collision_damage=collision_damage, x=x, y=y, v_x=v_x, v_y=v_y)
