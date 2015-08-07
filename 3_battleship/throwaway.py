from modules.game import Game, Player, AiPlayer

test_game = Game()
print "This game has an id of {}.".format(test_game.id)

print "Making dummy board for Player 2"
# test_game.player_2 = AiPlayer()
# test_game.player_2.name = "Computer"
test_game.player_2.create_ships()
test_game.player_2.random_place_ships()

# test_game.player_1.name = "Phillip"
test_game.player_1.create_ships()

test_game.player_1.place_ships()

test_game.player_1.own_board.draw_ships(test_game.player_1.fleet)

test_game.player_1.game_display()

while True:
    test_game.player_2.fire_shot(test_game.player_1)
    test_game.player_1.fire_shot(test_game.player_2)
