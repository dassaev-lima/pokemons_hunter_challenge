import unittest
from src.models.game import Game


class TestGame(unittest.TestCase):

    def test_start(self):
        game = Game()
        self.assertEqual(
            game.start(''),
            'You not walked, but captured 1 pokemon in your current position',
        )
        self.assertEqual(game.start('L'), 2)
        self.assertEqual(game.start('NLSO'), 4)
        self.assertEqual(game.start('NSNSNSNSNS'), 2)
        self.assertEqual(game.start('NLSOONL'), 6)
