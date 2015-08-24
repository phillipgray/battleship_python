from modules.game import Game, Player, AiPlayer, pause_until_enter, clear_screen

clear_screen()
print "Welcome to Battle.py Be the navy hero of your dreams--almost* guaranteed to win!"
current_game = Game()
print "This is a war game of accuracy. \
Do your best to sink the enemy fleet, {}.".format(current_game.player_1.name)
print """\nThe fleet consists of:
         An aircraft carrier, 5 spaces;
         A battleship, 4 spaces;
         A submarine, 3 spaces;
         A destroyer, 3 spaces;
         A patrol boat, 2 spaces;
         ===============================\n"""
print "This game has an id of {}.".format(current_game.id)
pause_until_enter()

# player 2 setup if/then tree
if isinstance(current_game.player_2, AiPlayer):
    print "Setting up {}'s board".format(current_game.player_2.name)
    current_game.player_2.create_ships()
    current_game.player_2.place_ships()
else:
    print "Pass to Player 2: {}".format(current_game.player_2.name)
    pause_until_enter("when ready to place ships")
    current_game.player_2.create_ships()
    current_game.player_2.place_ships()
    current_game.player_2.own_board.draw_ships(current_game.player_2.fleet)
    current_game.player_2.game_display()
    pause_until_enter("to pass to Player 1")
    clear_screen()


# player 1 setup
print "Player 1: {}".format(current_game.player_1.name)
current_game.player_1.create_ships()
current_game.player_1.place_ships()
current_game.player_1.own_board.draw_ships(current_game.player_1.fleet)
current_game.player_1.game_display()

# main game loop
game_continue = True
while game_continue:
    clear_screen()
    print "{}'s turn".format(current_game.player_2.name)
    if not isinstance(current_game.player_2, AiPlayer):
        pause_until_enter("after passing play to fire a shot")
    current_game.player_2.fire_shot(current_game.player_1)
    if current_game.player_2.is_game_over(current_game.player_1):
        game_continue = False
        winner = current_game.player_2.name
        continue
    pause_until_enter()

    clear_screen()
    print "{}'s turn".format(current_game.player_1.name)
    pause_until_enter("after passing play to fire a shot")
    current_game.player_1.fire_shot(current_game.player_2)
    if current_game.player_1.is_game_over(current_game.player_2):
        game_continue = False
        winner = current_game.player_1.name
    pause_until_enter()

else:
    print "Congratulations, {}! You have won the naval exercises.".format(winner)
