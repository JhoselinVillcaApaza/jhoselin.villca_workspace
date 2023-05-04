# Create a pygame program that shows a bouncing ball(pelota rebotando)
# Game is a class that has methods to run the logic for the boucing ball

# main is reponsible of creating an is¿nstance of class Game
# then it call methods run for instance of class Game

# def -> Define or create function, methods class

from game import Game

if __name__=="__main__":
    # create instance (object) of class Game
    game = Game()
    # call method run using "game" object (instance or variable)
    game.run()
