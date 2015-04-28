from random import choice, randint
# define ship class

class Ship(object):
	"""
	docstring for Ship class
	each ship has the following attributes
	ship_type: str
	size: int
	location: list of tuples, of int size
	"""
	def __init__(self, ship_type, size, location):
		super(Ship, self).__init__()
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

def board_fill(board_size):
	board = []
	first_col = []
	horiz_key = "+abcdefghij"

	for row in range(board_size + 1):
		if row == 0:
			for char in horiz_key[0:board_size + 1]:
				first_col.append(char)
			board.append(first_col)
		else:
			this_row = [str(row), ]
			this_row.extend(["O"] * board_size)
			board.append(this_row)
	return board

def print_board(board):
	for row in board:
		print " ".join(row)
