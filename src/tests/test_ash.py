import unittest
from src.models.ash import Ash

class TestAsh(unittest.TestCase):

    def test_walk(self):
        ash = Ash()
        self.assertEqual(ash.walk('N'), (2,[0,1]))
        self.assertEqual(ash.walk('L'), (3,[1,1]))
        self.assertEqual(ash.walk('S'), (4,[1,0]))
        self.assertEqual(ash.walk('O'), (4,[0,0]))
        self.assertEqual(ash.walk('0'), (5,[-1,0]))