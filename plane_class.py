from entity_class import Entity


class Plane(Entity):
    image_name = 'enemy_plane.png'
    def __init__(self, *group, x: int, y: int, v_x: int = 0, v_y: int = 0):
        super().__init__(*group, x=x, y=y, v_x=v_x, v_y=v_y)

    def update(self):
        self.rect.x -= self.v_x
        self.rect.y -= self.v_y