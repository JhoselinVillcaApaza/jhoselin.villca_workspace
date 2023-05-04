# define class Game
# __init --> inizializater method (initializes "atributes")
# Methods are special functions defined in a class: METHODS REQUIRE self arguments
# so i can call then from the object or instance

#Game has a pygame context
import pygame
class Game:
    # __init__ is initialization only MUST not contain an infinite loop
    def __init__(self, caption = "My first game", screen_width = 640, screen_height = 480):
        print("initializing game attributes")

        pygame.init()   
        #create the game Window(screen) 
        pygame.display.set_caption(caption)
        self.screen_width = screen_width
        self.screen_height = screen_height

        # this is the circle star position
         # this is the coordenads of circle

        self.circle_x = self.screen_height // 2
        self.circle_y = self.screen_width // 2
        self.circle_radius = 20
        self.circle_x_factor = 5
        self.circle_y_factor = 5

        # the window
        self.screen = pygame.display.set_mode((screen_width, screen_height))
        self.keep_screen_open = True

    #this method has the game screen open --> "game loop = while true"
    def run(self):
        print("This is the game run method")
        while self.keep_screen_open:
            print("The game is runing")

            # Here is calling the pattern
            self.capture_events()
            self.update()
            self.draw()
        else:
            print("Quit game because self.keep_screen_open is ",self.keep_screen_open)
            pygame.quit() # Cleaning pygame resources
    
    def capture_events(self):
        # Get events from pygame, and loop to get each event
        for event in pygame.event.get():
            # Ask pygame if QUIT event ocurred
            if event.type == pygame.QUIT:
                print("Received event.type",event.type,"that indicates close screen")
                self.keep_screen_open = False
            # PARA EVENTOS DE TECLADOS
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                   print("La tecla espacio ha sido presionada")

    # Cambia el estado interno del juego basado en input del jugador, logica interna del juego, etc
    def update(self):
        pass

    def draw_circle(self):
        # Move the circle before drawing it (CHANGE COORDINATES)
        self.circle_x += self.circle_x_factor
        self.circle_y += self.circle_y_factor

        # Verify if circle is inside the screen limits (top, botton, left, right)
        # and make decisions to avoid falling outside the limits
        if self.circle_x - self.circle_radius < 0 or self.circle_x + self.circle_radius > self.screen_width:
            self.circle_x_factor = -self.circle_x_factor

        if self.circle_y - self.circle_radius < 0 or self.circle_y + self.circle_radius > self.screen_height:
            self.circle_y_factor = -self.circle_y_factor
        # Draw the cicle
        circle_color = (255, 0, 0)
        pygame.draw.circle(self.screen, circle_color, (self.circle_x, self.circle_y), self.circle_radius)

    # Renderizar (dibujar o hacer que la pantalla se actualize)el cambio en la pantalla
    def draw(self):
        # change the screen panel to white
        self.screen.fill((255, 255, 255))

        self.draw_circle()
        pygame.display.flip()
        # 20 Miliseconds equivale mas o menos a 50 refresh de pantalla
        pygame.time.delay(20) # Nos dormimos durante 20 milisegundos antes de hacer el siguiente ciclo




