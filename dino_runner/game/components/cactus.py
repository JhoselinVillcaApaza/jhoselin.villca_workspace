from game.components.obstacle import Obstacle
import random
# Representa a todos los cactus 
class Cactus(Obstacle):
    def __init__(self, image_list):
        self.type = random.randint(0, 2)
        super().__init__(image_list, self.type)
        self.rect.y = 325
