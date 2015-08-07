import uuid
import os
from board import GameBoard, Ship


# helper functions

def shot_convert(letter_num):
    '''
    this function takes the 2 char letter_num board space
    (column row) and converts it to the int tuple (row, column)
    '''
    pre_tuple = list(letter_num)
    translation_key = {
        "a":1, "b":2, "c":3, "d":4, "e":5, "f":6, "g":7, "h":8, "i":9, "j":10,
    }
    return (int("".join(pre_tuple[1:])), translation_key[pre_tuple[0].lower()])


def damage_checker(ship_list, hits_coord_list):
        for ships in ship_list:
            for coord in ships.location:
                if coord not in hits_coord_list:
                    break
            else:
                if ships.is_sunk is False:
                    print "You've sunk the enemy {}. Huzzah! Battle on!".format(ships.ship_type)
                    ships.is_sunk = True


def clear_screen():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


def pause_until_enter():
    raw_input("Press Enter to try again")


class Game(object):
    """
    each instance of Game has the following attributes
    id, randomly assigned 8 char string
    is_online, bool indicating server_based game
    player_1, set to instance of Player
    player_2, default None, can be set to opponent Player or AI
    """
    def __init__(self):
        self.id = str(uuid.uuid4())[:8]
        self.turn_counter = 0
        self.is_online = False
        self.player_1 = Player()
        self.player_2 = None

    def incr_turn_counter(self):
        self.turn_counter += 1

    def server_methods(self):
        '''server methods will live here. someday'''
        pass


class Player(object):
    """
    each instance of Player has the following attributes:
    name, string identifying player name
    own_board, Gameboard instance containing player's ships
        and opponent's hits and misses
    other_board, Gameboard instance with player's hits and misses against
        the enemy
    """
    def __init__(self):
        self.name = None
        self.own_board = GameBoard()
        self.other_board = GameBoard()
        self.move_log = {}
        self.fleet = []
        self.occupied_spaces = []

    def game_display(self):
        print self.name + "'s turn"
        print "My Ocean"
        self.own_board.board_edit()
        self.own_board.print_board()
        print"\n\n Enemy Ocean"
        self.other_board.board_edit()
        self.other_board.print_board()

    def create_ships(self):
        self.fleet = [Ship(ship) for ship in Ship.SHIP_OPTIONS]
        return "Fleet of ships placed under your command, Captain."

    def random_place_ships(self):
        for ship in self.fleet:
            ship.random_set_location(self.own_board.all_spaces, self.occupied_spaces)
        self.own_board.draw_ships(self.fleet)
        self.game_display()

    def place_ships(self):
        '''
        this method iterates over ships in fleet
        and user assigns coordinates and direction to place ships on game board
        checks that coordinates are valid, prompts to re-enter if invalid
        '''
        for ship in self.fleet:
            clear_screen()
            self.own_board.draw_ships(self.fleet)
            self.game_display()
            while True:
                raw_starting_space = raw_input("Choose a starting space for the {} \
(format: letter number, e.g. B3): ".format(ship.ship_type))
                start_coord = shot_convert(raw_starting_space)

                if start_coord not in self.own_board.all_spaces:
                    print "Not a valid space!"
                    pause_until_enter()
                    continue
                elif start_coord in self.occupied_spaces:
                    print "This position already occupied!"
                    pause_until_enter()
                    continue
                else:
                    direction = raw_input("Choose the ship orientation: spanning either\
 {} spaces '(r)ight' or '(d)own' from starting space: ".format(ship.size - 1))
                    ship.choose_location(start_coord, direction)

                    for points in ship.location:
                        if points not in self.own_board.all_spaces:
                            print "Invalid placement: one or more coordinates doesn't exist"
                            pause_until_enter()
                            continue
                        elif points in self.occupied_spaces:
                            print "Invalid placement: one or more coordinates is taken"
                            pause_until_enter()
                            break
                    else:
                        for coord in ship.location:
                            self.occupied_spaces.append(coord)
                        print "{} location set.".format(ship.ship_type)
                        break
                    continue
        return "Fleet locations set, Captain."

    def fire_shot(self, other_player):
        clear_screen()
        self.game_display()
        while True:
            raw_shot = raw_input("Enter the coordinates for your next shot in a letter number pair, e.g. 'B3' ")
            shot_tuple = shot_convert(raw_shot)

            if shot_tuple not in other_player.own_board.all_spaces:
                print "Captain: those coordinates are out of range. Our next munitions supply is days away! We must conserve shells!"
                pause_until_enter()
                continue

            elif shot_tuple in other_player.own_board.hits or shot_tuple in other_player.own_board.misses:
                print "You've already fired on these coordinates! We must conserve munitions!"
                pause_until_enter()
                continue

            elif shot_tuple in other_player.occupied_spaces:
                print "Hit! Enemy sustained damage!"
                other_player.own_board.hits.append(shot_tuple)
                self.other_board.hits.append(shot_tuple)
                damage_checker(other_player.fleet, other_player.own_board.hits)
                pause_until_enter()
                break
            else:
                print "Miss! Take aim elsewhere, Captain."
                other_player.own_board.misses.append(shot_tuple)
                self.other_board.misses.append(shot_tuple)
                pause_until_enter()
                break
