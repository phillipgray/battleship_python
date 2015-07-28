import uuid
import board


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
        self.own_board = board.GameBoard()
        self.other_board = board.GameBoard()
        self.move_log = {}
        self.fleet = []

    def game_display(self):
        print "My Board"
        self.own_board.print_board()
        print"\n\n Enemy Board"
        self.other_board.print_board()
