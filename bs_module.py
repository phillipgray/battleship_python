from random import choice

# dict of ships

ship_options = {
    "aircraft carrier": 5,
    "battleship": 4,
    "submarine": 3,
    "destroyer": 3,
    "patrol boat": 2,
}

# helper function
def shot_convert(letter_num):
    '''
    this function takes the 2 char letter_num board space
    (column row) and converts it to the int tuple (row, column)
    '''
    pre_tuple = list(letter_num)
    translation_key = {"a":1, "b":2, "c":3, "d":4, "e":5, "f":6, "g":7, "h":8, "i":9, "j":10}
    return (int(pre_tuple[1]), translation_key[pre_tuple[0].lower()])

def damage_checker(ship_list, hits_coord_list):
        for ships in ship_list:
            for coord in ships.location:
                if coord not in hits_coord_list:
                    break
            else:
                if ships.is_sunk is False:
                    print "You've sunk the enemy {}. Huzzah! Battle on!".format(ships.ship_type)
                    ships.is_sunk = True
# define classes

# class GameCoord(object):
#     def __init__(self, letter_num):
#         self.letter_num = letter_num
#         self.row, self.column = self.translate(letter_num)

class GameBoard(object):
    """
    this class creates a new board, with these attributes
    board_size: int, length and width of board in spaces
    all_spaces: list of tuples, (row, column), of all spaces
    hits: list of tuples, (row, column), of all the hits
    misses: list of tuples, (row, column), of all the misses
    display_board: all_spaces as 2D list
    """
    def __init__(self, board_size):
        self.board_size = board_size
        self.all_spaces = self.set_position_list()
        self.hits = []
        self.misses = []
        self.display_board = self.board_fill()

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
        # self.all_spaces = position_list
        return position_list


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

    def board_edit(self):
        for coord in self.hits:
            self.display_board[coord[0]][coord[1]] = "X"
        for coord in self.misses:
            self.display_board[coord[0]][coord[1]] = "-"

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
    is_sunk: bool, is the ship sunk?
    """
    # list (of tuples) of all occupied spaces
    # needs to be reset for each new game!
    occupied_spaces = []

    def __init__(self, ship_type):
        self.ship_type = ship_type
        self.size = ship_options[ship_type]
        self.location = None
        self.is_sunk = False

    def ship_direction(self):
        '''
        returns a random direction
        '''
        return choice(["right", "left", "up", "down"])

    def set_location(self, board_list):
        ship_location = []
        direction = self.ship_direction()
        start_coord = choice(filter(lambda coord: coord not in Ship.occupied_spaces, board_list))

        if direction == "right":
            ship_location.append(start_coord)
            for col_num in range(start_coord[1] + 1, start_coord[1] + self.size):
                ship_location.append((start_coord[0], col_num))

        elif direction == "left":
            ship_location.append(start_coord)
            for col_num in range(start_coord[1] - 1, start_coord[1] - self.size, -1):
                ship_location.append((start_coord[0], col_num))

        elif direction == "down":
            ship_location.append(start_coord)
            for row_num in range(start_coord[0] + 1, start_coord[0] + self.size):
                ship_location.append((row_num, start_coord[1]))

        elif direction == "up":
            ship_location.append(start_coord)
            for row_num in range(start_coord[0] - 1, start_coord[0] - self.size, -1):
                ship_location.append((row_num, start_coord[1]))

        for points in ship_location:
            if points not in board_list or points in Ship.occupied_spaces:
                return self.set_location(board_list)

        self.location = ship_location
        for coord in ship_location:
            Ship.occupied_spaces.append(coord)

    
# test = GameBoard(8)
# print test.all_spaces
# print test.display_board
# test.print_board()
# ship0 = Ship('patrol boat')
# ship0.location = [(1,1), (1,2)]
# ship1 = Ship('patrol boat')
# ship1.location = [(1,3), (1,4)]
# group = [ship0, ship1]
# test_fire = []
# while True:
#     test = tuple(int(x.strip()) for x in raw_input("enter: ").split(','))
#     test_fire.append(test)
#     print test_fire
#     damage_checker(group, test_fire)

