from bs_module import *
import os

os.system('clear')
print "Welcome to Battleship For One. Be the navy hero of your dreams--almost* guaranteed to win!"

# set up game board, prompt for game size (difficulty)
while True:
    try:
        print "What size ocean (in spaces) would you like to play on? (6-10 spaces)"
        size = int(raw_input("Enter size: "))
        if not size >= 6 and size <= 10:
            raise ValueError("Value out of bounds!")
            continue
        break
    except ValueError:
        print "That wasn't an number, try again!"

game1 = GameBoard(size)

# create ships and set their location
print "Setting ships in their location...\n \n"

ship0 = Ship("aircraft carrier")
ship1 = Ship("destroyer")
ship2 = Ship("battleship")
ship3 = Ship("submarine")
ship4 = Ship("patrol boat")

fleet = [ship0, ship1, ship2, ship3, ship4]
for ship in fleet:
    ship.set_location(game1.all_spaces)

# set menu for game play
missed_shots = 10
print "This is a war game of accuracy. You only have {} missed shots before the game ends. Do your best to sink the enemy fleet, Captain.".format(missed_shots)
print """\nThe fleet consists of:
         An aircraft carrier, 5 spaces;
         A battleship, 4 spaces;
         A submarine, 3 spaces;
         A destroyer, 3 spaces;
         A patrol boat, 2 spaces;
         ===============================\n"""

raw_input("Press Enter to continue...")
game_continue = True

while game_continue is True and missed_shots > 0:

    # start each iteration by editing and then drawing the game board
    os.system('clear')
    game1.board_edit()
    game1.print_board()
    print "\n "
    # print number of missed shots, then give option to either quit or shoot
    current_missed_shots = 10 - missed_shots
    print "We've missed {} shots.".format(current_missed_shots)
    raw_shot = raw_input("Enter the coordinates for your next shot in a letter number pair, eg 'B3' or 'quit' to end the game: ")
    if raw_shot.lower() == "quit":
        print "Thanks for taking part in fleet exercises, Captain! Dismissed!"
        break
    else:
        shot_tuple = shot_convert(raw_shot)

    # key if else decision tree for gameplay

    if shot_tuple not in game1.all_spaces:
        print "Captain: those coordinates are out of range. Our next munitions supply is days away! We must conserve shells!"
        missed_shots -= 1
    elif shot_tuple in game1.hits or shot_tuple in game1.misses:
        print "You've already fired on these coordinates! We must conserve munitions!"
        missed_shots -= 1
    elif shot_tuple in Ship.occupied_spaces:
        print "Hit! Enemy sustained damage!"
        game1.hits.append(shot_tuple)
        damage_checker(fleet, game1.hits)
    else:
        print "Miss! Take aim elsewhere, Captain."
        missed_shots -= 1
        game1.misses.append(shot_tuple)

    # check for game ending condition: too many missed shots
    if missed_shots <= 0:
        print "We're out of munitions, and there still enemy ships afield. Prepare to be court martialed for your performance. Dismissed!"
        game_continue = False

    # check for game ending condtions: all ships sunk
    for ships in fleet:
        if ships.is_sunk is False:
            print "Naval exercises continue! Battle on!"
            break
    else:
        game_continue = False
        print "Congratulations! You've completed the mission victoriously. All enemy ships have been sunk!"
        # break

    raw_input("Press Enter to continue...")
