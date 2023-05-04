import pygame
from pygame.sprite import Sprite
from game.utils.constants import RUNNING, JUMPING, DUCKING
class Dinosaur(Sprite):
    def __init__(self, name, coord_x, coord_y, coord_y_ducking, velocity_jump):
        self.name = name
        self.image = RUNNING[0]
        self.coord_x = coord_x
        self.coord_y = coord_y
        self.coord_y_ducking = coord_y_ducking
        self.image_position = self.image.get_rect()
        self.image_position.x = self.coord_x
        self.image_position.y = self.coord_y
        self.velocity_jump = velocity_jump
        self.time_jump = velocity_jump
        self.selected_image_index = 0
        self.duck_dinosaur = False
        self.run_dinosaur = True
        self.jump_dinosaur = False
        self.dinosaur_status = "Running"
    
    def update(self, user_input):
        #States
        if self.run_dinosaur:
            self.run()
            self.dinosaur_status = "Running"
        elif self.duck_dinosaur:
            self.duck()
            self.dinosaur_status = "Ducking"
        elif self.jump_dinosaur:
            self.jump()
            self.dinosaur_status = "Jumping"
        if self.selected_image_index >= 12:
            self.selected_image_index = 0
        if user_input[pygame.K_UP] or user_input [pygame.K_x] and not self.jump_dinosaur:
            self.duck_dinosaur = False
            self.run_dinosaur = False
            self.jump_dinosaur = True
        elif user_input[pygame.K_DOWN] or user_input [pygame.K_a] and not self.jump_dinosaur:
            self.duck_dinosaur = True
            self.run_dinosaur = False
            self.jump_dinosaur = False
        elif not self.jump_dinosaur:
            self.duck_dinosaur = False
            self.run_dinosaur = True
            self.jump_dinosaur = False

    def draw(self, screen):
        screen.blit(self.image, self.image_position)

    def run(self):
        if self.selected_image_index < 6:
            self.image = RUNNING[0] 
        else:
            self.image = RUNNING[1]
        self.image_position = self.image.get_rect()
        self.image_position.x = self.coord_x
        self.image_position.y = self.coord_y
        self.selected_image_index += 1

    def jump(self):
        self.image = JUMPING
        if self.jump_dinosaur:
            self.image_position.y -= self.velocity_jump * 4
            self.velocity_jump -= 0.9
        if self.velocity_jump < -self.time_jump: 
            self.image_position.y = self.coord_y
            self.jump_dinosaur = False
            self.velocity_jump = self.time_jump

    def duck(self):
        if self.selected_image_index < 6:
            self.image = DUCKING[0]
        else:
            self.image = DUCKING[1]
        self.image_position = self.image.get_rect()
        self.image_position.x = self.coord_x
        self.image_position.y = self.coord_y_ducking
        self.selected_image_index += 1   