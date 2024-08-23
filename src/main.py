from models.game import Game

if __name__ == "__main__":
    """
    Inclui as classes e chama as funções para inicialização do projeto.
    """
    route = input("input the route made by Ash: \n")
    game = Game()
    print(game.start(route))
    