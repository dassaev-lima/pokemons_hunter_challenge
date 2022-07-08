import time as time
from models.game import Game
from models.ash import Ash
if __name__ == "__main__":
    route = input("input the route made by Ash: \n")
    game = Game()
    print(game.start(route))