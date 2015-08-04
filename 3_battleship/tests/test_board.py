import unittest
from modules.board import GameBoard, Ship


class GameBoardTest(unittest.TestCase):
    def setUp(self):
        self.two_board = GameBoard(2)
        self.three_board = GameBoard(3)

    def test_set_position_list_assignment(self):
        test_list = [(1, 1), (1, 2), (2, 1), (2, 2)]
        self.assertItemsEqual(test_list, self.two_board.all_spaces)

class ShipTest(unittest.TestCase):
    def test_choose_ship_location(self):
        test_board = GameBoard(2)
        boat = Ship('patrol boat')
        boat.choose_location((1,1), 'right')
        self.assertItemsEqual(boat.location, [(1, 1), (1, 2)])




if __name__ == '__main__':
    unittest.main()
