from modules.game import Game, Player
from modules.board import GameBoard, Ship

test_game = Game()
print "This game has an id of {}.".format(test_game.id)

test_game.player_1.create_ships()

test_game.player_1.place_ships()

test_game.player_1.own_board.draw_ships(test_game.player_1.fleet)