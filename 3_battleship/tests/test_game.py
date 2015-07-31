import unittest
from modules.game import Game, Player
from modules.board import Ship


class GameModuleTest(unittest.TestCase):

    def setUp(self):
        self.game_1 = Game()

    def test_can_initialize_new_game(self):
        self.assertIsInstance(self.game_1, Game)

    def test_games_have_unique_ids(self):
        game_2 = Game()
        self.assertNotEquals(self.game_1.id, game_2.id)

    def test_game_has_turn_counter_attribute(self):
        self.assertEqual(self.game_1.turn_counter, 0)

    def test_game_has_default_false_is_online_attr(self):
        self.assertEqual(self.game_1.is_online, False)

    def test_incr_turn_counter(self):
        self.game_1.incr_turn_counter()
        self.game_1.incr_turn_counter()
        self.assertEqual(self.game_1.turn_counter, 2)

    def test_player_1_is_player(self):
        self.assertIsInstance(self.game_1.player_1, Player)

    def test_player_2_is_none(self):
        self.assertIsNone(self.game_1.player_2)


class PlayerModuleTest(unittest.TestCase):

    def setUp(self):
        self.player_1 = Player()

    def test_create_ships_in_fleet(self):
        self.player_1.create_ships()
        self.assertEqual(len(self.player_1.fleet), 5)

    def test_all_ship_types_in_fleet(self):
        self.player_1.create_ships()
        ship_list = [ship.ship_type for ship in self.player_1.fleet]
        self.assertItemsEqual(ship_list, Ship.SHIP_OPTIONS.keys())


if __name__ == '__main__':
    unittest.main()
