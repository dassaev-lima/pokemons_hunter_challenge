"""
Este módulo é o ponto de entrada para o projeto e gerencia a execução do jogo.

Quando executado, o script solicita ao usuário que insira uma rota, cria uma
instância da classe `Game` importada de `models.game`, e inicia o jogo com a rota
fornecida. O resultado do jogo é então exibido no console.

Uso:
    Execute o script para iniciar o jogo e fornecer uma rota.

Exemplo:
    python main.py

O módulo espera que a classe `Game` esteja definida em `models` e que tenha
um método `start` que aceite uma rota como argumento.

Autor: Dassaev Lima
Data: 23/08/2024
Versão: 1.0
"""

from models import Game

if __name__ == "__main__":
    """
    Inclui as classes e chama as funções para inicialização do projeto.
    """
    route = input("input the route made by Ash: \n")
    game = Game()
    print(game.start(route))
