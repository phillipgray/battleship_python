import unittest
from modules.game import Game


class GameModuleTest(unittest.TestCase):

    def test_can_initialize_new_game(self):
        game_1 = Game()
        self.assertIsInstance(game_1, Game)

if __name__ == '__main__':
    unittest.main()
