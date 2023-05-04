import random
from game.components.obstacle import Obstacle
class Bird(Obstacle):
    def __init__(self, image_list):
        super().__init__(image_list, 0)
        self.type = 0
        self.step_index = 0
        self.index = 0
        self.rect.y = 200 if random.randint(0, 1) == 0 else 300 if random.randint(0, 1) == 0 else 250
        
    def draw(self, screen):
        if self.index <= 5:
            self.type = 0
        else:
            self.type = 1
        screen.blit(self.image_list[self.type], self.rect)
        self.index += 1
        if self.index >= 10:
            self.index = 0

        
    

    
    