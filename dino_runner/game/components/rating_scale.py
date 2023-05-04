import pygame
from pygame.locals import *
from game.utils.constants import COLORS
from game.components.obstacle_builder import ObstacleBuilder
class RatingScale:
    def get_score(self, points):
        font = pygame.font.SysFont("Super Mario 64 DS", 25)
        text = font.render("Points: " + str(points), True, COLORS["Black"])
        text_rect = text.get_rect()
        text_rect.center = (1000, 40)
        return text, text_rect
    
    def get_centered_message(self, message, width = 1000, height = 100):
        font = pygame.font.SysFont("ArcadeClassic", 50)
        text = font.render(message, True, COLORS["Black"])
        text_rect = text.get_rect()
        text_rect.center = (width, height)
        return text, text_rect
   