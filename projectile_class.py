from entity_class import Entity
from image_processing import load_image

class Projectile(Entity):
    """Класс снаряда"""
    projectile_name = 'bullet.png'
    image = None

    def __init__(self, *group, alliance: int = 0, x: int, y: int, v_x: int = 0, v_y: int = 0):
        if not self.__class__.image:
            self.__class__.image = load_image(self.__class__.projectile_name)
        super().__init__(*group, alliance=alliance, x=x, y=y, v_x=v_x, v_y=v_y)
        print(self.__class__)

