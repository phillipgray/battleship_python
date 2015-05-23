from random import choice

# define classes


class GameBoard(object):
    """
    this class creates a new board
    """
    def __init__(self, board_size):
        self.board_size = board_size
        self.all_spaces = None
        self.hits = []
        self.misses = []
        self.display_board = None

    def set_position_list(self):
        '''
        method takes attr board size
        returns list of tuples, where
        (row, column), which compose all the board spaces
        '''
        position_list = []
        for row in range(1, self.board_size + 1):
            for column in range(1, self.board_size + 1):
                position_list.append((row, column), )
        self.all_spaces = position_list


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
        self.display_board = board

    def board_edit(self):
        for coord in self.hits:
            self.display_board[coord[0]][coord[1]] = "X"
        for coord in self.misses:
            self.display_board[coord[0]][coord[1]] = "•"

    def print_board(self):
        for row in self.display_board:
            print " ".join(row)


class Ship(object):
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

class BattleshipGame():
    """
    docstring for BattleshipGame
    this class will create a new game
    the child classes are 
    """
    def __init__(self, board_size):
        # super(BattleshipGame, self).__init__()
        self.board_size = board_size

# helper functions








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

