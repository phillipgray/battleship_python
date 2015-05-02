from random import choice

# define classes

class BattleshipGame(object):
    """
    docstring for BattleshipGame
    this class will create a new board
    and
    """
    def __init__(self, board_size):
        # super(BattleshipGame, self).__init__()
        self.board_size = board_size

    def board_fill(self):
        '''
        this method takes the board size attribute and
        returns a 2d list of all spaces for display
        '''
        board = []
        first_col = []
        horiz_key = "+abcdefghij"

        for row in range(self.board_size + 1):
            if row == 0:
                for char in horiz_key[0:self.board_size + 1]:
                    if char == '+':
                        first_col.append(" " + char)  # this if/then is to fix spacing
                    else:
                        first_col.append(char)
                board.append(first_col)
            else:
                if row <= 9:  # this if/then is to fix spacing
                    this_row = [" " + str(row), ]
                else:
                    this_row = [str(row), ]
                this_row.extend(["O"] * self.board_size)
                board.append(this_row)
        return board

    def print_board(board):
        for row in board:
            print " ".join(row)


class Ship(BattleshipGame):
    """
    docstring for Ship class
    each ship has the following attributes
    ship_type: str
    size: int
    location: list of tuples, of int size
    """
    def __init__(self, ship_type, size, location):
        # super(Ship, self).__init__()
        self.ship_type = ship_type
        self.size = size
        self.location = location


# dict of ships

ship_options = {
    "aircraft carrier": 5,
    "battleship": 4,
    "submarine": 3,
    "destroyer": 3,
    "patrol boat": 2,
}

# helper functions






def generate_position_list(board_size):
    '''
    function takes board size as int
    returns list of tuples, where
    (row, column)
    '''
    position_list = []
    for row in range(1, board_size + 1):
        for column in range(1, board_size + 1):
            position_list.append((row, column), )
    # print position_list
    return position_list


def ship_start_space(available_space_list):
    '''
    takes a list of tuple coordinates and
    returns a random choice from the list
    '''
    start_coord = choice(available_space_list)
    return start_coord


def ship_direction():
    '''
    returns a random direction
    '''
    return choice(["right", "left", "up", "down"])

def generate_location(size, board_list, other_ships_list):
    location = []
    direction = ship_direction()
    start_coord = ship_start_space(board_list)
    if direction == "right":
        location.append(start_coord)
        for col_num in range(start_coord[1] + 1, start_coord[1] + size):
            location.append((start_coord[0], col_num))

    elif direction == "left":
        location.append(start_coord)
        for col_num in range(start_coord[1] - 1, start_coord[1] - size, -1):
            location.append((start_coord[0], col_num))

    elif direction == "down":
        location.append(start_coord)
        for row_num in range(start_coord[0] + 1, start_coord[0] + size):
            location.append((row_num, start_coord[1]))

    elif direction == "up":
        location.append(start_coord)
        for row_num in range(start_coord[0] - 1, start_coord[0] - size, -1):
            location.append((row_num, start_coord[1]))

    # print start_coord
    # print direction
    # print location

    for points in location:
        if points not in board_list or points in other_ships_list:
            # print "nope"
            return generate_location(size, board_list, other_ships_list)

    return location

