import random
from game.components.cactus import Cactus
from game.components.bird import Bird
from game.utils.constants import SMALL_CACTUS, LARGE_CACTUS, BIRD
from game.components.cactus import Cactus
class ObstacleBuilder:
    def __init__(self) :
        self.obstacles = []
        self.counter_cactus = 0
        self.counter_bird = 0
        self.point = 100

    def update(self, game):
        index = random.randint(0, 2)
        if len(self.obstacles) == 0:
            if index == 0:
                self.obstacles.append(Cactus(SMALL_CACTUS))
            elif index == 1:
                self.obstacles.append(Cactus(LARGE_CACTUS))
            elif index == 2:
                self.obstacles.append(Bird(BIRD))

        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)

            if game.dinosaur.image_position.colliderect(obstacle.rect):
                if type(obstacle) is Cactus:
                    self.counter_cactus += 1
                    self.obstacles = []
                    self.point = self.point - 5
                elif type(obstacle) is Bird:
                    self.counter_bird += 1
                    self.obstacles = []
                    self.point = self.point - 2.5
                    
    def draw(self,screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)

