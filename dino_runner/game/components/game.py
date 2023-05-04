import pygame, os
from game.utils.constants import BG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS, COLORS, GAMESTART, BACKGROUND1, START, BACKGROUND, RUNNING
from game.components.dinosaur import Dinosaur
from game.components.cloud import Cloud
from game.components.obstacle_builder import ObstacleBuilder
from game.components.rating_scale import RatingScale
class Game:
    def __init__(self):
        pygame.init()
        pygame.mixer.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.sound_explotion = pygame
        self.playing = False
        self.game_speed = 15
        self.x_pos_bg = 0
        self.y_pos_bg = 380
        self.dinosaur = Dinosaur("T-Rex", 80, 305, 342, 8.5)
        self.obstacle_builder = ObstacleBuilder()
        self.cloud = Cloud()
        self.points = 0
        self.text_utils = RatingScale()
        self.dinno_running = True
        pygame.mixer.init()
        self.sound = pygame.mixer.Sound(os.path.join(os.path.dirname(__file__), "sound.ogg"))
        pygame.mixer.Sound.play(self.sound)

    def run(self):
        print("starting the game loop")
        self.playing = True
        while self.playing:
            if self.obstacle_builder.point > 0:
                self.capture_events()
                self.update()
                self.draw()
            else:
                self.sound.stop()
                self.show_menu()
                break
        else:
            print("quit the game")

    def capture_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print("received event.type", event.type, "that indicates `quit` game")
                self.playing = False

    def update(self):
        user_input = pygame.key.get_pressed()
        self.dinosaur.update(user_input)
        self.obstacle_builder.update(self)
        self.cloud.update(self.game_speed)

    def draw(self):
        self.clock.tick(FPS)
        self.screen.blit(BACKGROUND, (SCREEN_WIDTH//2 - 700, SCREEN_HEIGHT//2 -500))
        self.draw_background()
        self.dinosaur.draw(self.screen)
        self.cloud.draw(self.screen)
        self.obstacle_builder.draw(self.screen)
        self.font_text = pygame.font.SysFont('Glamour Elephant', 35)
        self.message = "Dino TREX is : {} ".format(self.dinosaur.dinosaur_status)
        self.text_status = self.font_text.render(self.message, True, COLORS["Cyan"])
        self.screen.blit(self.text_status, (10, 500))
        self.text_cactus = self.font_text.render("Dino collide with Cactus: "+str(self.obstacle_builder.counter_cactus), True, COLORS["Red"])
        self.screen.blit(self.text_cactus, (410, 470))
        self.text_bird = self.font_text.render("Dino collide with Bird: "+str(self.obstacle_builder.counter_bird), True, COLORS["Pink"])
        self.screen.blit(self.text_bird, (410, 530))
        self.text_point= self.font_text.render("Total points: "+str(self.obstacle_builder.point), True, COLORS["Magenta"])
        self.screen.blit(self.text_point, (480, 50))
        pygame.display.update()
        pygame.display.flip()

    def draw_background(self):
        image_width = BG.get_width()
        self.screen.blit(BG, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
        if self.x_pos_bg <= -image_width:
            self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
            self.x_pos_bg = 0
        self.x_pos_bg -= self.game_speed
        
    def show_menu(self):
        self.dinno_running = True
        self.screen.fill(COLORS["Black"])
        self.show_parts()
        pygame.display.update()
        self.manage_events()
        pygame.time.delay(3000)
    def show_parts(self):
        self.screen.blit(BACKGROUND1, (SCREEN_WIDTH//2 - 700, SCREEN_HEIGHT//2 -500))
        text, text_rext = self.text_utils.get_centered_message("Score  0")
        self.screen.blit(text, text_rext)
        self.screen.blit(GAMESTART, (240, 170))
        self.screen.blit(START, (527, 520))
        self.screen.blit(RUNNING[0], (530, 100))
    def manage_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.dinno_running = False
                self.playing = False
                pygame.display.quit()
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                self.run()
    