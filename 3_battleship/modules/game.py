import uuid
from board import GameBoard, Ship


# helper method

def shot_convert(letter_num):
    '''
    this function takes the 2 char letter_num board space
    (column row) and converts it to the int tuple (row, column)
    '''
    pre_tuple = list(letter_num)
    translation_key = {"a":1, "b":2, "c":3, "d":4, "e":5, "f":6, "g":7, "h":8, "i":9, "j":10}
    return (int(pre_tuple[1]), translation_key[pre_tuple[0].lower()])


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
    docstring for Player
    """
    def __init__(self):
        self.name = None
        self.own_board = GameBoard()
        self.other_board = GameBoard()
        self.move_log = {}
        self.fleet = []
        self.occupied_spaces = []

    def game_display(self):
        print "My Ocean"
        self.own_board.print_board()
        print"\n\n Enemy Ocean"
        self.other_board.print_board()

    def create_ships(self):
        self.fleet = [Ship(ship) for ship in Ship.SHIP_OPTIONS]
        return "Fleet of ships placed under your command, Captain."

    def place_ships(self):
        '''
        this method iterates over ships in fleet
        and user assigns coordinates and direction to place ships on game board
        checks that coordinates are valid, prompts to re-enter if invalid
        '''
        for ship in self.fleet:
            while True:
                raw_starting_space = raw_input("Choose a starting space for the {} \
(format: letter number, e.g. B3): ".format(ship.ship_type))
                start_coord = shot_convert(raw_starting_space)

                if start_coord not in self.own_board.all_spaces:
                    print "Not a valid space!"
                    raw_input("Press any key to enter another coordinate.")
                    continue
                elif start_coord in self.occupied_spaces:
                    print "This position already occupied!"
                    raw_input("Press any key to enter another coordinate.")
                    continue
                else:
                    direction = raw_input("Choose the ship orientation: spanning either\
 {} spaces '(r)ight' or '(d)own' from starting space: ".format(ship.size - 1))
                    ship.choose_location(start_coord, direction)

                    for points in ship.location:
                        if points not in self.own_board.all_spaces:
                            print "Invalid placement: one or more coordinates doesn't exist"
                            raw_input("Press any key to try again")
                            continue
                        elif points in self.occupied_spaces:
                            print "Invalid placement: one or more coordinates is taken"
                            raw_input("Press any key to try again")
                            break
                    else:
                        for coord in ship.location:
                            self.occupied_spaces.append(coord)
                        print "{} location set.".format(ship.ship_type)
                        break
                    continue
        return "Fleet locations set, Captain."
