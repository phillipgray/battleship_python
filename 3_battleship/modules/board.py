from random import choice

class GameBoard(object):
    """
    this class creates a new board, with these attributes
    board_size: int, length and width of board in spaces
    all_spaces: list of tuples, (row, column), of all spaces
    hits: list of tuples, (row, column), of all the hits
    misses: list of tuples, (row, column), of all the misses
    display_board: all_spaces as 2D list
    """
    def __init__(self, board_size=10):
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

    def draw_ships(self, ship_list):
        '''
        this method takes a ship list (Player.fleet)
        and draws the location of the ships on the board
        '''
        for boat in ship_list:
            boat_marker = boat.ship_type[0].upper()
            for coord in boat.location:
                self.display_board[coord[0]][coord[1]] = boat_marker

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

    SHIP_OPTIONS = {
        "aircraft carrier": 5,
        "battleship": 4,
        "submarine": 3,
        "destroyer": 3,
        "patrol boat": 2,
    }

    def __init__(self, ship_type):
        self.ship_type = ship_type
        self.size = self.SHIP_OPTIONS[ship_type]
        self.location = None
        self.is_sunk = False

    def ship_direction(self):
        '''
        returns a random direction
        '''
        return choice(["right", "left", "up", "down"])

    def random_set_location(self, board_list, occupied_spaces_list):
        ship_location = []
        direction = self.ship_direction()
        start_coord = choice(filter(lambda coord: coord not in occupied_spaces_list, board_list))

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
            if points not in board_list or points in occupied_spaces_list:
                return self.random_set_location(board_list)

        self.location = ship_location
        for coord in ship_location:
            occupied_spaces_list.append(coord)

    def choose_location(self, start_coord, direction):
        '''
        this method takes a start coord (row, col) and either 'right' or 'down'
        as a direction, and assigns the appropriate location to a ship
        note: does not check that any coords are valid/playable!
        '''
        ship_location = []
        ship_location.append(start_coord)
        if direction.lower() == "right" or direction.lower() == "r":
            for col_num in range(start_coord[1] + 1, start_coord[1] + self.size):
                ship_location.append((start_coord[0], col_num))
        elif direction.lower() == "down" or direction.lower() == "d":
            for row_num in range(start_coord[0] + 1, start_coord[0] + self.size):
                ship_location.append((row_num, start_coord[1]))
        self.location = ship_location
